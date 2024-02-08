"""
Temporary module to fix metadata in existing files.
"""

from pathlib import Path
from eyed3 import id3
import eyed3


def get_songs_from_album(file_path: str) -> list[Path]:
    """
    Get all the songs from an album
    :param file_path: str
    :return: list[str]
    """
    album = Path(file_path)
    songs = list(album.glob("*.mp3"))
    return songs


def get_song_metadata(file_path: Path):
    """A debug function to get the metadata of a song"""

    audiofile = eyed3.load(file_path)
    print(file_path)
    print(audiofile.tag.artist)
    print(audiofile.tag.album)
    print(audiofile.tag.title)
    print(audiofile.tag.track_num)
    print(audiofile.tag.genre)


def set_song_genre(file_path: Path, genre: str):
    """Set the genre of a song."""

    audiofile = eyed3.load(file_path)
    audiofile.tag.genre = genre
    audiofile.tag.save()


def set_song_title(file_path: Path, title: str):
    """Set the title of a song."""

    audiofile = eyed3.load(file_path)
    audiofile.tag.title = title
    audiofile.tag.save()


if __name__ == "__main__":
    album_path = 

    songs = get_songs_from_album(album_path)
    for song in songs:
        set_song_genre(song, "Reggae")
