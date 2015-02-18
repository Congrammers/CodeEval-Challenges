import sys
import time
import datetime as dt

def extractTime(value):
    hour, minute, second = value.split(':')
    hour = int(hour)
    minute = int(minute)
    second = int(second)
    return time.struct_time(dt.datetime(1, 1, 1, hour, minute, second)
                            .timetuple())

def calculateTime(first, second):
    first = time.mktime(first)
    second = time.mktime(second)
    if first > second:
        return first - second
    elif first < second:
        return second - first
    else:
        return 0

def printResult(result):
    result = int(result)
    hours = int(result / 3600) % 24
    minutes = int(result / 60) % 60
    seconds = result % 60

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)
    print(hours + ':' + minutes + ':' + seconds)

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        begin, end = line.rstrip().split()
        begin = extractTime(begin)
        end = extractTime(end)
        printResult(calculateTime(begin, end))
