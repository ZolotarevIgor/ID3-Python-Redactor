from os import getcwd
from os.path import basename
from glob import glob
from mutagen.mp3 import MP3
from mutagen.id3 import TPE1, TIT2

fpath = f"{getcwd()}/*.mp3"
files = glob(fpath)

for fname in files:
    temp_fname = basename(fname)[:-4]
    while temp_fname.find("_") != -1:
        print(f"Type symbol instead of '_' in {temp_fname}")
        symb = input()
        temp_fname = temp_fname.replace('_', symb, 1)
    name_list = temp_fname.split(' - ')
    if len(name_list) > 2:
        print(f"Error parsing file name: {fname}")
        continue
    artist, song_name = name_list
    try:
        mp3 = MP3(fname)
    except BaseException as e:
        print(f"{fname} loading error: {e}")
        continue
    if mp3.tags is None:
        mp3.add_tags()
    tag = mp3.tags

    if not "artist" in tag:
        tag.add(TPE1(encoding=3, text=artist))
    if not "title" in tag:
        tag.add(TIT2(encoding=3, text=song_name))
    try:
        mp3.save(v2_version=3)
    except BaseException as e:
        print(f"{fname} saving error: {e}")