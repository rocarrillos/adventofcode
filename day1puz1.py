from csvToList import readToList

dataList = []
readToList('day1.csv', dataList)
print(sum([(int(int(i) / 3) - 2) for i in dataList]))
