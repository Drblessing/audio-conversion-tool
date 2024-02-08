from mutagen.flac import FLAC
from pydub import AudioSegment
from pathlib import Path
import ffmpeg
import re
import eyed3
from mutagen.id3 import ID3, TXXX, TCON
from mutagen.mp3 import MP3
import os
import sys


def get_song_name_from_flac(file_path: Path | str) -> str:
    """Get the song name from the flac file path.
    It will usually be the last part of the file path,
    and be in the format:
    [track number]. [artist] - [song name] [ISRC].flac
    We want to return:
    [track number]. [artist] - [song name]
    """
    # Get the file path as a Path object
    file_path = Path(file_path)
    # Get the stem of the file path
    song_name = file_path.stem
    # Remove everything in [square brackets]
    song_name = re.sub(r"\[.*?\]", "", song_name)
    # Remove file extension
    song_name = song_name.replace(".flac", "")
    # Remove leading 0's, i.e. 03 -> 3
    while song_name.startswith("0"):
        song_name = song_name[1:]

    # Strip whitespace
    song_name = song_name.strip()

    return song_name


def flac_to_mp3(flac_file: Path | str, genre: str) -> None:
    """Convert a flac file to mp3."""
    # Convert flac to mp3
    flac_file = Path(flac_file)
    song_dir = flac_file.parent

    flac_audio = AudioSegment.from_file(flac_file, "flac")

    # Get the song name
    song_name = get_song_name_from_flac(flac_file)
    # Create file path for mp3
    output_file = song_dir / f"{song_name}.mp3"

    # Export to mp3 in the same directory
    ffmpeg.input(str(flac_file)).output(
        str(output_file), ab="320k", id3v2_version=3
    ).overwrite_output().run()

    fix_textframe_metadata_mp3(output_file)
    set_genre_mp3(output_file, genre)


def fix_textframe_metadata_mp3(file_path: Path | str):
    """Get the textframe metadata from an mp3 file."""
    # Get the flac file as a Path object
    file_path = Path(file_path)
    # Load the mp3 file
    audiofile = MP3(file_path, ID3=ID3)

    # List of TXXX frames to remove
    txxx_frames_to_remove = []

    # Identify all TXXX frames
    for key in audiofile.tags.keys():
        if isinstance(audiofile.tags[key], TXXX):
            txxx_frames_to_remove.append(key)

    # Delete all TXXX except lyrics, USLT
    for frame in txxx_frames_to_remove:
        if frame != "TXXX:USLT":
            del audiofile.tags[frame]

    audiofile.save()


def set_genre_mp3(file_path: Path | str, genre: str):
    """Set the genre of an mp3 file."""
    # Get the flac file as a Path object
    file_path = Path(file_path)
    # Load the mp3 file
    audiofile = MP3(file_path, ID3=ID3)

    # Set the genre
    audiofile.tags.add(TCON(encoding=3, text=genre))

    audiofile.save()


def convert_flac_album_to_mp3(file_path: Path | str, genre: str):
    """Convert a flac album to mp3.
    This will convert all flac files in the directory to mp3.
    The bitrate is set to 320 kbps.
    The flac metadata will be copied to the mp3 file, as well.
    The mp3 metadta will be cleaned up, and the genre set to the genre of the album.
    The song names will be cleaned up, to format <track number>. <artist> - <song name>.mp3
    The album name will also be cleaned up to <artist> - <album name>
    """

    # Fix album name
    # Get album path
    album_path = Path(file_path)
    # Get album name
    album_name = album_path.name
    # Remove brackets
    album_name = re.sub(r"\[.*?\]", "", album_name)
    # Strip whitespace
    album_name = album_name.strip()
    # Get new album path
    new_album_path = album_path.parent / album_name
    # Move album to new path
    album_path = album_path.rename(new_album_path)

    # Convert all flac files to mp3
    flac_files = [flac_file for flac_file in album_path.glob("*.flac")]
    for flac_file in flac_files:
        flac_to_mp3(flac_file, genre)

    # Delete all flac files
    for flac_file in flac_files:
        flac_file.unlink()


if __name__ == "__main__":
    # test_album = ""
    # convert_flac_album_to_mp3(test_album)
