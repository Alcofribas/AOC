#!/usr/bin/python

import operator
import os
import re
import sys

def decryptRoomName(name, offset):
    decrypted = ''
    offset = offset % 26
    for letter in name:
        if letter == "-":
            decrypted += " "
        else:
            decrypted += chr(97 + ((ord(letter)-97+offset) % 26))
    return decrypted

# Arbeitsverzeichnis setzen
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# load data
infile = open('AOC1604_input.txt')
roomlist = [line.rstrip('\n') for line in infile]
infile.close()

# print roomlist

orig_stdout = sys.stdout
outfile = open("AOC1604_output.txt","w")
sys.stdout = outfile

real = 0
for room in roomlist:
    # parse room details
    sectorID = re.findall(r'\d+', room)[0]
    code, checksum = room.split(sectorID)

    # check fro real room
    count = {x:code.count(x) for x in code if x != '-'}
    check = [(c, l) for l, c in count.iteritems()]
    check = sorted(check, key=lambda x: x[1])
    check = sorted(check, key=lambda x: x[0], reverse=True)
    check = ''.join([x[1] for x in check[:5]])
    name = 'NOT EXISTENT'
    offset = int(sectorID)
    if check == checksum[1:-1]:
        real += offset
        # decrypt name
        name = decryptRoomName(code,offset)
    print room, check, real, name
    if re.search("north", name):
        npos = offset

print "---------------"
print "Sum of real rooms' checksums: %d" % real
print "Sector ID of north polar object storage: %d" % npos

# write travel protocol
#
# output.writelines([str(x)+"\n" for x in path])
sys.stdout = orig_stdout
outfile.close()
