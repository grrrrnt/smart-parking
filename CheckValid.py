import re

pre = str()
num = str()
suf = str()

def sufValue(str):
    switcher = {
                "A": 0,
                "Z": 1,
                "Y": 2,
                "X": 3,
                "U": 4,
                "T": 5,
                "S": 6,
                "R": 7,
                "P": 8,
                "M": 9,
                "L": 10,
                "K": 11,
                "J": 12,
                "H": 13,
                "G": 14,
                "E": 15,
                "D": 16,
                "C": 17,
                "B": 18
    }

    return switcher.get(str)

def convertint(x):
    return ord(x)-96


print ("CHECK VALIDITY OF LICENSE PLATE\n")

# pre = input("Enter prefix: ").lower()
# num = input("Enter license plate numbers: ")
# suf = input("Enter suffix: ")



while True:
    prenumsuf = str()
    prenumsuf = input("Enter license plate: ")

    try:
        num = (re.findall('\d+', prenumsuf))[0]
    except:
        print("Error: The license plate is not valid.")
        continue

    numDef = num
    pre = (re.findall("[a-zA-Z]+", prenumsuf))[0].lower()
    suf = (re.findall("[a-zA-Z]+", prenumsuf))[1]

    if len(pre) == 3:
        preTrunc = str(pre[1:3])
    elif len(pre) == 2:
        preTrunc = pre
    elif len(pre) == 1:
        preTrunc = "`"+pre
    else:
        print("The license plate " + pre.upper() + num + suf.upper() + " is INVALID.")
        exit()


    if len(num) == 4:
        numTrunc = num
    elif len(num) == 3:
        numTrunc = "0"+num
    elif len(num) == 2:
        numTrunc = "00"+num
    elif len(num) == 1:
        numTrunc = "000"+num
    else:
        print("The license plate " + pre.upper() + num + suf.upper() + " is INVALID.")
        exit()

    preValue1 = int(convertint(preTrunc[0]))*9
    preValue2 = int(convertint(preTrunc[1]))*4

    numValue1 = int(numTrunc[0])*5
    numValue2 = int(numTrunc[1])*4
    numValue3 = int(numTrunc[2])*3
    numValue4 = int(numTrunc[3])*2

    sufValue1 = int((preValue1 + preValue2 + numValue1 + numValue2 + numValue3 + numValue4) % 19)

    if sufValue1 == sufValue(suf.upper()):
        print ("The license plate " + pre.upper() + num + suf.upper() + " is VALID.")
    else:
        print ("The license plate " + pre.upper() + num + suf.upper() + " is INVALID.")


    exitCmd = str()
    exitCmd = input("Exit? Y/N -- ")
    if exitCmd == "Y" or exitCmd == "y":
        break
    elif exitCmd == "N" or exitCmd == "n":
        continue