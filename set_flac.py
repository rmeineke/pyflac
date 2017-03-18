#! /usr/bin/python3

import glob
import os
from mutagen.flac import FLAC, Picture
import logging
import sys


def get_flac_file_list():
    return sorted(glob.glob('*.flac'))
    pass


def get_cover_filename():
    files = glob.glob('*.jpg')
    if files:
        return files[0]


def set_flac_tags():
    pass


def parse_template_file(template_filename):
    head = []
    tail = []
    if os.path.exists(template_filename):
        with open(template_filename) as fin:
            head = [next(fin).strip() for x in range(3)]
            for entry in fin.readlines():
                tail.append(entry.strip().title())
        print(head)
        print(tail)
    return head, tail


def process_file(**kwargs):
    # print(kwargs['fn'])
    # print(kwargs)
    print('{:02d} - {}.flac'.format(int(kwargs['idx'] + 1), kwargs['songtitle']))
    kwargs['logger'].debug(kwargs['title'])
    print('cover art: {}'.format(kwargs['albumart']))
    # logger.debug(head)

def parse_data(field):
    item = field.split(':')
    return item[1].strip()


def main():

    # set up for logging
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL,
              }
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level)

    logger = logging.getLogger()
    logger.debug('Entering main')

    cover_filename = get_cover_filename()
    if cover_filename:
        print(cover_filename)
    else:
        print("Can't seem to find cover art ... exiting")
        exit(1)

    template_filename = 'temp.txt'
    head, tail = parse_template_file(template_filename)
    albumartist = parse_data(head[0])
    artist = parse_data(head[1])
    albumtitle = parse_data(head[2])

    logger.debug(head)
    logger.debug(tail)
    logger.debug(len(tail))

    flacfilelist = get_flac_file_list()

    # this needs to match the number
    # of file names in the template file
    num_files_found = len(flacfilelist)
    num_tracks_in_template = len(tail)
    total_num_tracks = num_tracks_in_template

    if num_files_found != num_tracks_in_template:
        print('Number of flac files does not match list in template file.')
        print('Exiting . . . ')
        exit(2)

    for idx, fn in enumerate(flacfilelist):
        track_num = idx + 1
        new_file_name = '{:02d} - {}.flac'.format(track_num, tail[idx])
        track_name = tail[idx]
        print()
        print('{}'.format(albumartist))
        print('{}'.format(artist))
        print('{}'.format(albumtitle))
        print('{}'.format(track_name))
        print('{} of {}'.format(track_num, total_num_tracks))

        audio = FLAC(fn)
        audio.clear()
        audio.clear_pictures()
        audio['artist'] = artist
        audio['albumartist'] = albumartist
        audio['album'] = albumtitle
        audio['title'] = track_name
        audio['tracknumber'] = '{0}/{1}'.format(track_num, total_num_tracks)

        image = Picture()
        image.type = 3
        if cover_filename.endswith('png'):
            image.mime = 'image/png'
        else:
            image.mime = 'image/jpeg'
        with open(cover_filename, 'rb') as f:  # better than open(albumart, 'rb').read() ?
            image.data = f.read()
        audio.add_picture(image)
        audio.save()
        print('Move: {} --> {}'.format(fn, new_file_name))
        os.rename(fn, new_file_name)


if __name__ == '__main__':
    main()

"""
audio = FLAC("test.flac")
    print(type(audio))
    print(audio['albumartist'][0])
    print(audio['title'][0])
    print(audio['album'][0])
    print(audio['artist'][0])
    print(audio['date'][0])

    print(audio['tracknumber'][0])

    print(audio['tracktotal'][0])
    print(audio['genre'][0])

    print(audio['composer'][0])
    print(audio['description'][0])
    print(audio.pictures)
    print(audio.info.sample_rate)
    print(audio.info.channels)
    print(audio.info.length)
    print(audio.tags)
    print(audio.info.pprint())
    # audio.pprint()

"""
