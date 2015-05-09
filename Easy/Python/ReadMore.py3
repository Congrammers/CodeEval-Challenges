import sys

def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip()
        if len(line) > 55:
            if (len(line.split()[0]) <= 39 and len(line.split()) > 1):
                line = smart_truncate(line, 39, '')
            else:
                line = line[:40]
            line = line.rstrip()
            line += '... <Read More>'
        print(line)
