import eyed3
from eyed3 import id3

from eyed3.id3 import ID3_V1_1


audiofile = eyed3.load("assets/motivational-symphony-music.mp3", tag_version=ID3_V1_1)
audiofile.initTag(version=ID3_V1_1)
audiofile.tag.artist = "Token Entry"
audiofile.tag.album = "Free For All Comp LP"
audiofile.tag.album_artist = "Various Artists"
audiofile.tag.title = "The Edge!"
audiofile.tag.track_num = 3

audiofile.tag.save()
