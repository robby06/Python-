import sys
import re

time = sys.argv[1]

pattern = '^(0?[1-9]|1[0-2]):([0-5][0-9]) ?([AP]M|[ap]m)$'
([01]?[0-9]|2[0-3]):[0-5][0-9]

match = re.search(pattern, time)

if match:
    print('valid time')

else:
    print('invalid time')