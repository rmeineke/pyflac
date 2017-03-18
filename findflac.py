#!/usr/bin/python3

# Import the os module, for the os.walk function
import os, sys
from mutagen.flac import FLAC, Picture
from mutagen import File


#from mutagen import File

#file = File('some.mp3') # mutagen can automatically detect format and type of tags
#artwork = file.tags['APIC:'].data # access APIC frame and grab the image
#with open('image.jpg', 'wb') as img:
   #img.write(artwork) # write artwork to new image
   
   
   
def extract_pic(input):
    file = File(input)
    print('--------------------------------------------')
    print(file)
    print('--------------------------------------------')

    #artwork = file.tags['APIC:'].data
    #with open(input, 'wb') as img:
        #img.write(artwork)

   
def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts



def pict_test(audio):
    try: 
        x = audio.pictures
        if x:
            return True
    except Exception:
        pass  
    if 'covr' in audio or 'APIC:' in audio:
        return True
    return False
 
 

# Set the directory you want to start from
rootDir = '/home/robertm'
for dirName, subdirList, fileList in os.walk(rootDir):
    
    a = splitall(dirName)
    
    for fname in fileList:
        
        if fname.endswith('.flac'):
            print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
            
            print('%s\t%s' % (a[len(a) - 1], fname))
            audio = FLAC(dirName + '/' + fname)
            print(audio['albumartist'][0])
            print(audio['tracknumber'][0])
            print(audio['title'][0])
            print(audio['album'][0])
            if pict_test(audio):
                print('*** pic found ***')
                print(audio.pictures)
                #pic = Picture(dirName + '/' + fname)
                extract_pic(dirName + '/' + fname)
            else:
                print('------------------------------------- no pic')

