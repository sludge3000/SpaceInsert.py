# SpaceInsert.py
# Created by Luke Savage
#
# Script takes hex stream from 'data.txt' and inserts a space every two
# characters to make the file readable in Wiresharkself.
#
# Useage:
# Please hex stream in data.txt
# Run SpaceInsert.py in the same directory as data.txt


infile = open('data.txt')
outfile = open('test.txt', 'r+')
read_infile = infile.read()
# print(read_infile)
# 0123456789ABCDEF
new_data = ' '.join([read_infile[i:i+2] for i in range(0, len(read_infile), 2)])
outfile.write(new_data)
# 23
infile.close()
outfile.close()
