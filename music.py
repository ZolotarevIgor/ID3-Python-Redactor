import os
from glob import glob
from mutagen.mp3 import MP3
from mutagen import MutagenError

fpath = f"{os.getcwd()}/*.mp3"
files = glob(fpath)

for fname in files:
    temp_fname = os.path.basename(fname)[:-4]
    while temp_fname.find("_") != -1:
        print(f"Type symbol instead of '_' in {fname}")
        symb = None
        type(symb)
        temp_fname.replace('_', symb, 1)
    name_list = temp_fname.split(' - ')
    if len(name_list) > 2:
        print(f"Error parsing file name: {fname}")
        continue
    artist, song_name = name_list
    try:
        mp3 = MP3(fname)
    except MutagenError:
        print(f"File loading error: {fname}")
        continue
    if mp3.tags is None:
        mp3.add_tags()
    tag = mp3.tags
    try:
        tag["artist"]
    except KeyError:
        tag["artist"] = artist
    try:
        tag["title"]
    except KeyError: 
        tag["title"] = song_name
    try:
        tag.save(v2_version=3)
    except MutagenError:
        print(f"File saving error: {fname}")
        continue