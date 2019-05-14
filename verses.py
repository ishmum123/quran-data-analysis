from os import listdir, mkdir
from os.path import isfile, join, exists
import itertools

onlyfiles = [f for f in listdir('verses') if isfile(join('verses', f))]

if not exists('chapters'):
    mkdir('chapters')

dct = {}

for f in onlyfiles:
    fs = f.split('-')
    if len(fs) > 1 and fs[0].isdigit():
        if fs[0] in dct:
            dct[fs[0]].append(fs[1].split('.')[0])
        else:
            dct[fs[0]] = [fs[1].split('.')[0]]

for key in dct:
    with open(join('chapters', str(int(key)) + '.txt'), 'w') as f:
        l = list(map(int, dct[key]))
        l.sort()
        for verse_num in l:
            vfn = str(verse_num) if verse_num > 99 else '0' + str(verse_num) if verse_num > 9 else '00' + str(verse_num)
            with open(join('verses', key + '-' + vfn + '.txt'), 'r') as rf:
                f.write(str(verse_num) + '. ' + rf.read() + '\n')
