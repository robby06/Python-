import sys
import re

phone_num = sys.argv[1]

patterns = ['1?[\s-]?\(?(\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}']

valid = False 

for p in patterns:
    match = re.search(p, phone_num)
    valid = valid or match
    
if valid:
    print('valid phone number')
else:
    print('invalid phone number')