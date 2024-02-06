"""
audio-conversion-tool temporary template file
"""

import os
import sys
from pathlib import Path
import shutil
from mutagen.easyid3 import EasyID3
from mutagen.oggvorbis import OggVorbis
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from pydub import AudioSegment
import logging


class AudioConversion:
    """
    Converts audio files to mp3.
    """

    def __init__(
        self,
        directory: str,
        artist: str,
        album: str,
        cover_filepath: str = "AlbumArt.jpg",
        genre: str = "Pop",
    ):
        self.artist = artist
        self.album = album
        self.cover_filepath = cover_filepath
        # Convert directory int a path object
        self.directory = Path(directory)

    def get_files(self):
        """
        Get all the files in the directory
        """
        files = list(self.directory.glob("*"))
        return files
