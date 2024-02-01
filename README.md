# Audio Conversion Tool

## Overview

This audio conversion tool is a Python module designed to simplify the process of converting audio files from various formats (like WAV, FLAC) to MP3, while also handling the embedding of correct metadata, including genre and album art.

## Features

- **Format Conversion**: Convert audio files to MP3 from various formats.
- **Metadata Handling**: Update the metadata of the MP3 files, including title, artist, album, genre, and more.
- **Album Art Embedding**: Attach album art to your MP3 files easily.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/audio-conversion-tool.git

# Navigate to the audio-conversion-tool directory
cd audio-conversion-tool

# Install required dependencies
pip install -r requirements.txt
```

Your enviornment also needs to have ffmpeg installed. You can install it using the following commands:

```bash
# For Ubuntu
sudo apt-get install ffmpeg

# For MacOS
brew install ffmpeg

# For Windows
# Download the ffmpeg installer from https://ffmpeg.org/download.html
```

## Usage

Here's a quick example to convert an audio file:

```python
from audio_conversion_tool import AudioConverter

# Initialize the converter
converter = AudioConverter()

# Convert an audio file
converter.convert_to_mp3('path/to/input.wav', 'path/to/output.mp3')

# Update metadata and album art
converter.update_metadata('path/to/output.mp3', genre='Rock', album_art='path/to/album_art.jpg')
```

For more detailed usage, please refer to the documentation.

## Repository Structure

- /src: The source code for the audio conversion tool.
- /tests: Unit tests and other test scripts to ensure the functionality works as expected.
- /docs: Documentation for the module, installation guide, and detailed usage examples.
- /examples: Example scripts showing how to use the audio conversion tool.
- requirements.txt: List of required dependencies for the module.
- /assets: Sample audio files and album art for testing and demonstration purposes.
