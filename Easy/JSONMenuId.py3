import sys
import json

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        if line in ['\n', '\r\n']:
            continue
        line = json.loads(line.rstrip())
        if line["menu"]:
            line = line["menu"]

        if "items" not in line: continue
        item = line["items"]

        total = 0
        for data in item:
            if not data:
                continue
            if "label" not in data:
                continue
            total += int(data["id"])

        print(total)
