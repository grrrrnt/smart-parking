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

pre = input("Enter prefix: ").lower()
num = input("Enter 3 visible numbers: ")
suf = input("Enter suffix: ")

if len(pre) == 3:
    preTrunc = str(pre[1:3])
elif len(pre) == 2:
    preTrunc = pre
elif len(pre) == 1:
    preTrunc = "`"+pre
else:
    print("Error: Please ensure your prefix is correct.")
    exit()

if len(num) > 4 or len(num) < 1:
    print("Error: Please ensure your plate numbers are correct.")
    exit()

if len(suf) != 1:
    print("Error: Please ensure your suffix is correct.")
    exit()

preValue1 = int(convertint(preTrunc[0]))*9
preValue2 = int(convertint(preTrunc[1]))*4

# Values if first digit is missing
numFirstValue1 = int(num[0])*4
numFirstValue2 = int(num[1])*3
numFirstValue3 = int(num[2])*2

# Values if second digit is missing
numSecondValue1 = int(num[0])*5
numSecondValue2 = int(num[1])*3
numSecondValue3 = int(num[2])*2

# Values if third digit is missing
numThirdValue1 = int(num[0])*5
numThirdValue2 = int(num[1])*4
numThirdValue3 = int(num[2])*2

# Values if fourth digit is missing
numFourthValue1 = int(num[0])*5
numFourthValue2 = int(num[1])*4
numFourthValue3 = int(num[2])*3

totalValue1 = preValue1 + preValue2 + numFirstValue1 + numFirstValue2 + numFirstValue3
totalValue2 = preValue1 + preValue2 + numSecondValue1 + numSecondValue2 + numSecondValue3
totalValue3 = preValue1 + preValue2 + numThirdValue1 + numThirdValue2 + numThirdValue3
totalValue4 = preValue1 + preValue2 + numFourthValue1 + numFourthValue2 + numFourthValue3

# If first digit is missing

arbValue = list(range(1,20))
numList1 = list()
numList1 = [19*i + sufValue(suf.upper()) - totalValue1 for i in arbValue]

for i in numList1:
    if (i%5 == 0) and (i/5 <= 9) and (i/5 >= 0):
        # print("The possible missing first digit is " + )
        if (i/5 != 0):
            print ("The license plate may be: " + pre.upper() + str( int(i/5) ) + num + suf.upper() + ". Missing digit was the first digit.")
        else:
            print ("The license plate may be: " + pre.upper() + num + suf.upper())
    else:
        i=i+1


# If second digit is missing

numList2 = list()
numList2 = [19 * i + sufValue(suf.upper()) - totalValue2 for i in arbValue]

for i in numList2:
    if (i % 4 == 0) and (i / 4 <= 9) and (i / 4 >= 0):
        # print("The possible missing second digit is " + str(int(i / 4)))
        print("The license plate may be: " + pre.upper() + num[:1] + str(int(i / 4)) + num[1:] + suf.upper() + ". Missing digit was the second digit.")
    else:
        i = i + 1


# If third digit is missing

numList3 = list()
numList3 = [19 * i + sufValue(suf.upper()) - totalValue3 for i in arbValue]

for i in numList3:
    if (i % 3 == 0) and (i / 3 <= 9) and (i / 3 >= 0):
        # print("The possible missing third digit is " + str(int(i / 3)))
        print("The license plate may be: " + pre.upper() + num[:2] + str(int(i / 3)) + num[2:] + suf.upper() + ". Missing digit was the third digit.")

    else:
        i = i + 1


# If fourth digit is missing

numList4 = list()
numList4 = [19 * i + sufValue(suf.upper()) - totalValue4 for i in arbValue]

for i in numList4:
    if (i % 2 == 0) and (i / 2 <= 9) and (i / 2 >= 0):
        # print("The possible missing fourth digit is " + str(int(i / 2)))
        print("The license plate may be: " + pre.upper() + num[:3] + str(int(i / 2)) + num[3:] + suf.upper() + ". Missing digit was the fourth digit.")
    else:
        i = i + 1


exitCmd = str()
exitCmd = input("Exit? Y/N -- ")
while True:
    if exitCmd == "Y":
        exit
    elif exitCmd == "N":
        break
