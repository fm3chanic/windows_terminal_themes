#this script merges all files with theme or scheme in their name
#within the same folder together in two files
#these than can be copied in windows terminal settings .json
#helpful if you want to apply multiple themes at once
import os

def read_file(file_name):
    tmpstr = ''
    f = open(file_name, 'r')
    tmpstr = f.read()
    f.close()
    return tmpstr

files = os.listdir()
content = ''

s = open('schemes.json', 'a')
t = open('themes.json', 'a')

for file in files:
    if file.find('theme') > 1:
        content = read_file(file)
        t.write(content + ',')
        t.write('\n')
    if file.find('scheme') > 1:
        content = read_file(file)
        s.write(content + ',')
        s.write('\n')
s.close()
t.close()