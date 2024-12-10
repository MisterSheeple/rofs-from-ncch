import os
import sys

if len( sys.argv ) > 1 and "-h" not in sys.argv and "--help" not in sys.argv:
    file_path = sys.argv[1]
    directory = os.path.dirname(os.path.abspath(file_path))
    if not os.path.exists(file_path):
        print('File not found.')
        exit()
else:
    print('Usage: python3 rofs-from-ncch.py [options] (infile)\n\nOptions:\n  -h, --help         Display this message.')
    exit()

with open(file_path, 'rb') as file:
    content = file.read()

position = content.find(bytes([0x52, 0x4F, 0x46, 0x53]))

if position != -1:
    with open(directory + "/" + "rofs.bin", 'wb') as file:
        file.write(content[position:])
else:
    print('ROFS not found.')
