import sys
import re

path = sys.argv[1]
with open(path, 'r') as inFile:
    for email in inFile:
        if email in ['\n', '\r\n']:
            continue
        email = email.rstrip()

        if re.match(r'^"[a-z|A-Z|0-9|_|-|+|.|@]+"|[a-z|A-Z|0-9|_|-|+|.?]*@{1}[a-z|0-9]+\.{1}[a-z|0-9|-]+\.?[a-z|0-9|-]{2,}',
                    email):
            print("true")
        else:
            print("false")
