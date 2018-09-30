# data manipulation
import csv

with open("manufacturingData.csv", newline = '') as data:
    reader = csv.reader(data, delimiter = ',')
    for row in reader:
        print(row[4])
