from os import listdir, mkdir
from os.path import isfile, join, exists
from shutil import rmtree

out_dir = 'chapters'
in_dir = 'verses'

onlyfiles = [f for f in listdir(in_dir) if isfile(join(in_dir, f))]

if exists(out_dir):
    rmtree(out_dir)

mkdir(out_dir)

dct = {}

for f in onlyfiles:
    fs = f.split('-')
    if len(fs) > 1 and fs[0].isdigit():
        if fs[0] in dct:
            dct[fs[0]].append(fs[1].split('.')[0])
        else:
            dct[fs[0]] = [fs[1].split('.')[0]]

for key in dct:
    with open(join(out_dir, str(int(key)) + '.txt'), 'w') as f:
        l = list(map(int, dct[key]))
        l.sort()
        for verse_num in l:
            vfn = str(verse_num) if verse_num > 99 else '0' + str(verse_num) if verse_num > 9 else '00' + str(verse_num)
            with open(join(in_dir, key + '-' + vfn + '.txt'), 'r') as rf:
                f.write(str(verse_num) + '. ' + rf.read() + '\n')
