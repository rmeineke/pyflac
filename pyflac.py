#! /usr/bin/python3

import mutagen.id3
from mutagen.flac import FLAC

print('pyflac.py')


def getMutagenTags(path):
    """"""
    audio = mutagen.id3.ID3(path)
 
    print ("Artist: %s" % audio['TPE1'].text[0])
    print ("Track: %s" % audio["TIT2"].text[0])
    print ("Release Year: %s" % audio["TDRC"].text[0])
    
    
getMutagenTags('need.mp3')

audio = FLAC("room.flac")
print(audio['albumartist'][0])
print(audio['title'][0])
print(audio['album'][0])
audio.pprint()
