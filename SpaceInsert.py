# SpaceInsert.py
# Created by Luke Savage
#
# Script takes hex stream from 'data.txt' and inserts a space every two
# characters to make the file readable in Wiresharkself.
#
# Useage:
# Please hex stream in data.txt
# Run SpaceInsert.py in the same directory as data.txt

while True:
    try:
        open('data.txt')
        break
    except FileNotFoundError:
            print('data.txt is not present in the working directory')
            break


infile = open('data.txt')
outfile = open('test.txt', 'w+')
read_infile = infile.read()
# print(read_infile)
# 0123456789ABCDEF
new_data = ' '.join(
    [read_infile[i:i+2] for i in range(0, len(read_infile), 2)]
    )
outfile.write('0000 00 00 00 00 00 00 00 00 00 00 00 00 08 00 ' + new_data)
infile.close()
outfile.close()
