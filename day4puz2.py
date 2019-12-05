dataRange = [382345, 843167]

def isEligible(number):
    stringNum = str(number)
    containsDup = False
    duplicates = set()
    for i in range(len(stringNum) - 1):
        if stringNum[i + 1] < stringNum[i]:
            return False
        if stringNum[i] == stringNum[i + 1]:
            containsDup = True 
            duplicates.add(stringNum[i])
    for i in range(len(stringNum) - 2):
        if stringNum[i] == stringNum[i + 1] and stringNum[i] == stringNum[i + 2]:
            if stringNum[i] in duplicates:
                duplicates.remove(stringNum[i])
    return len(duplicates) > 0

possiblePasswords = []
for i in range(dataRange[0], dataRange[1] + 1):
    if isEligible(i):
        possiblePasswords.append(i)

print(len(possiblePasswords))