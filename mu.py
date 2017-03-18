#! /usr/bin/python3
import os
import mutagen.id3
from mutagen.flac import FLAC

for folderName, subfolders, filenames in os.walk('.'):
    for subfolder in subfolders:
        for filename in filenames:
            if filename.endswith('.mp3'):
                print(folderName + ' -- ' + subfolder + ' -- ' + filename)
                audio = mutagen.id3.ID3(filename)
            if filename.endswith('.flac'):
                print('found flac file: ' + filename)

                audio = FLAC("room.flac")
                print(audio['albumartist'][0])
                print(audio['title'][0])
                print(audio['album'][0])
                audio.pprint()