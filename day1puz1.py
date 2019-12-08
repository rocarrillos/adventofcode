from csvtolist import csv_to_list

dataList = []
csv_to_list('day1.csv', dataList)
print(sum([(int(int(i) / 3) - 2) for i in dataList]))
