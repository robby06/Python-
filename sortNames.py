import sys
import re
import os

if len(sys.argv[1:]) != 1:
    print('Invalid arguments ')
    sys.exit(0)

filename = sys.argv[1]

if not os.path.isfile(filename):
    print('File not found')
    sys.exit(0)

infile = open(filename)
names = []
pattern = '([A-Za-z]+(?: [A-Za-z]+| [A-Z]\.)?) ([A-Za-z]+)'

for line in infile:
    match = re.search(pattern, line)
    if match:
        first_middle, last = match.groups()
        names.append("{}, {}".format(last, first_middle))

infile.close()
sorted_names = sorted(names)
script_dir = os.path.dirname(os.path.realpath(__file__))
outfilename = os.path.join(script_dir, 'sortedNames.txt')
outfile = open(outfilename, 'w')

for name in sorted_names:
    outfile.write(name + '\n')
outfile.close()
print('Done.')