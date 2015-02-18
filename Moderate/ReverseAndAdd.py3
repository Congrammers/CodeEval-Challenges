import sys

def reverse(num):
    return int(str(num)[::-1])
def palindrome(num):
    return str(num) == str(num)[::-1]

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        currNum = int(line.strip())
        counter = 0
        while not palindrome(currNum):
            currNum += reverse(currNum)
            counter += 1
        print(str(counter) + " " + str(currNum))
