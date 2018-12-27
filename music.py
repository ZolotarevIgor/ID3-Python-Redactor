from os import getcwd
import glob
from mutagen.easyid3 import EasyID3

fpath = f'{getcwd()}/*.mp3'
files = glob.glob(fpath)

for fname in files:
    if fname.find('_') != -1:
        print(f'Error in file {fname}')
        continue
    name_list = fname.split('-')
    if len(name_list) > 2:
        print(f'Error in file {fname}')
        continue
    artist, song_name = name_list
    tag = EasyID3(fname)
    try:
        tag['artist']
    except KeyError:
        tag['artist'] = artist
    try:
        tag['title']
    except KeyError: 
        tag['title'] = song_name
    tag.save(v2_version=3)