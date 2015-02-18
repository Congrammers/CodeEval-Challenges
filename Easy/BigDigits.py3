import re
import sys

def drawZero():
    return ["-**--",
            "*--*-",
            "*--*-",
            "*--*-",
            "-**--",
            "-----"]
def drawOne():
    return ["--*--",
            "-**--",
            "--*--",
            "--*--",
            "-***-",
            "-----"]
def drawTwo():
    return ["***--",
            "---*-",
            "-**--",
            "*----",
            "****-",
            "-----"]
def drawThree():
    return ["***--",
            "---*-",
            "-**--",
            "---*-",
            "***--",
            "-----"]
def drawFour():
    return ["-*---",
            "*--*-",
            "****-",
            "---*-",
            "---*-",
            "-----"]
def drawFive():
    return ["****-",
            "*----",
            "***--",
            "---*-",
            "***--",
            "-----"]
def drawSix():
    return ["-**--",
            "*----",
            "***--",
            "*--*-",
            "-**--",
            "-----"]
def drawSeven():
    return ["****-",
            "---*-",
            "--*--",
            "-*---",
            "-*---",
            "-----"]
def drawEight():
    return ["-**--",
            "*--*-",
            "-**--",
            "*--*-",
            "-**--",
            "-----"]
def drawNine():
    return ["-**--",
            "*--*-",
            "-***-",
            "---*-",
            "-**--",
            "-----"]

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.strip()
        digitized = re.compile(r"\D")
        digit = digitized.sub('', line)

        result = []
        for n in digit:
            if n == "0":
                result.append(drawZero())
            elif n == "1":
                result.append(drawOne())
            elif n == "2":
                result.append(drawTwo())
            elif n == "3":
                result.append(drawThree())
            elif n == "4":
                result.append(drawFour())
            elif n == "5":
                result.append(drawFive())
            elif n == "6":
                result.append(drawSix())
            elif n == "7":
                result.append(drawSeven())
            elif n == "8":
                result.append(drawEight())
            elif n == "9":
                result.append(drawNine())
            else:
                raise(ValueError)

        pseudoGraphic = ""
        currDigit = result[0]
        for y in range(len(currDigit)):
            for x in range(len(result)):
                pseudoGraphic += result[x][y]
            pseudoGraphic += "\n"

        sys.stdout.write(pseudoGraphic)
