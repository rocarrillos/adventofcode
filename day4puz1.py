dataRange = [382345, 843167]


def isEligible(number):
    stringNum = str(number)
    containsDup = False
    for i in range(len(stringNum) - 1):
        if stringNum[i + 1] < stringNum[i]:
            return False
        if stringNum[i] == stringNum[i + 1]:
            containsDup = True        
    return containsDup

possiblePasswords = []
for i in range(dataRange[0], dataRange[1] + 1):
    if isEligible(i):
        possiblePasswords.append(i)

print(len(possiblePasswords))