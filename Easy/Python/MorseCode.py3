import sys

codecss = (('A', ".-"), ('B', "-..."), ('C', "-.-."), ('D', "-.."),
           ('E', "."), ('F', "..-."), ('G', "--."), ('H', "...."),
           ('I', ".."), ('J', ".---"), ('K', "-.-"), ('L', ".-.."),
           ('M', "--"), ('N', "-."), ('O', "---"), ('P', ".--."),
           ('Q', "--.-"), ('R', ".-."), ('S', "..."), ('T', "-"),
           ('U', "..-"), ('V', "...-"), ('W', ".--"), ('X', "-..-"),
           ('Y', "-.--"), ('Z', "--.."),

           ('0', '-----'), ('1', '.----'), ('2', '..---'), ('3', '...--'),
           ('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'),
           ('8', '---..'), ('9', '----.'))

def decode(val):
    if not val: return ' '
    for letter, code in codecss:
        if code == val: return letter

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip().split(' ')
        result = ""
        for w in line:
            result += decode(w)
        print(result)
