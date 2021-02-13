#!/usr/bin/env python

import  os
from os import walk
from shutil import copyfile

dir_1 = r'D:\\Testdir\\'
dir_2 = r'D:\\Dirtest\\'

f = []
d = []
for (dir_1, dirnames, filenames) in walk(dir_1):
    f.extend(filenames)
    d.extend(dirnames)

f2 = []
d2 = []
for (dir_2, dirnames, filenames) in walk(dir_2):
    f2.extend(filenames)
    d2.extend(dirnames)

print(f'Dirnames {d}')
print(f'Dirnames2 {d2}')

for file in f:
    if file in f2:
        f2_index = f2.index(file)
        filetime = os.path.getmtime(dir_1 + file)
        filetime_2 = os.path.getmtime(dir_2 + f2[f2_index])

        if filetime > filetime_2:
            print(f'Kopiere {file} von dir1 nach dir2')
            copyfile(dir_1 + file, dir_2 + file)
        elif filetime_2 > filetime:
            print(f'Kopiere {file} von dir2 nach dir1')
            copyfile(dir_2 + file, dir_1 + file)
        else:
            print(f'Files sind auf dem selben Stand')
    else:
        print(f'Kopiere {file} von dir1 nach dir2')
        copyfile(dir_1 + file, dir_2 + file)

for file in f2:
    if file in f:
        f_index = f.index(file)
        filetime_2 = os.path.getmtime(dir_2 + file)
        filetime = os.path.getmtime(dir_1 + f[f_index])

        if filetime_2 > filetime:
            print(f'Kopiere {file} von dir2 nach dir1')
            copyfile(dir_2 + file, dir_1 + file)
        elif filetime > filetime_2:
            print(f'Kopiere {file} von dir1 nach dir2')
            copyfile(dir_1 + file, dir_2 + file)
        else:
            print(f'Files sind auf dem selben Stand')
    else:
        print(f'Kopiere {file} von dir2 nach dir1')
        copyfile(dir_2 + file, dir_1 + file)