print ('img.py')

from mutagen import File

file = File('room.flac')
artwork = file.tags['APIC:'].data # access APIC frame and grab the image
with open('image.jpg', 'wb') as img:
   img.write(artwork) # write artwork to new image

