import calendar
import sys
from datetime import date
from collections import namedtuple

def getTrueRange(rangelist):
    pos = 0
    nextsPos = pos + 1
    while nextsPos < len(rangelist):
        latest = rangelist[pos]
        nexts = rangelist[nextsPos]

        overlapDays = getOverlapDays(latest, nexts)
        if (overlapDays > 0):
            if nexts.end > latest.end:
                merged = [Range(start=latest.start, end=nexts.end)]
            else:
                merged = [Range(start=latest.start, end=latest.end)]
            rangelist[pos:nextsPos + 1] = merged
        else:
            pos += 1
            nextsPos = pos + 1

    return rangelist

def transMonth(word):
    monthMap = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    return monthMap[word]

def getRangeList(allList):
    rangelist = []
    for val in allList:
        begin, end = val.split('-')
        begin = begin.split()
        end = end.split()

        bYear, bMonth, bDays = (int(begin[1]), int(transMonth(begin[0])), 1)
        eYear, eMonth = (int(end[1]), int(transMonth(end[0])))
        eDays = calendar.monthrange(eYear, eMonth)[1]
        rangelist.append(Range(start=date(bYear, bMonth, bDays),
                               end=date(eYear, eMonth, eDays)))
    return rangelist

def getOverlapDays(latest, nexts):
    return min(latest.end - nexts.start, nexts.end - latest.start).days + 1

def diffMonth(ranges):
    d1 = ranges.end
    d2 = ranges.start
    return (d1.year - d2.year)*12 + d1.month - d2.month

path = sys.argv[1]
with open(path, 'r') as inFile:
    Range = namedtuple('Range', ['start', 'end'])
    for line in inFile:
        line = line.rstrip().split('; ')
        rangeList = getRangeList(line)
        rangeList.sort()
        trueRangeList = getTrueRange(rangeList)

        monthSum = 0
        for ranges in trueRangeList:
            monthSum += diffMonth(ranges) + 1
        result = int(monthSum / 12)
        print(result)
