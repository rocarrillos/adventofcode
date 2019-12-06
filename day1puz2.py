from csvToList import readToList

dataList = []
readToList('day1.csv', dataList)

# we're gonna recurse this boi
def fuelCounter(amount, fuelList):
  requiredFuel = int(amount / 3) - 2
  if (requiredFuel > 0):
    fuelList.append(requiredFuel)
    fuelCounter(requiredFuel, fuelList)
  
def execute():
  fuelAmounts = []
  for item in dataList:
    fuelCounter(int(item), fuelAmounts)
  print(sum(fuelAmounts))

execute()