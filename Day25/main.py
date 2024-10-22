import csv
with open("Day25\weather_data.csv") as data_file:
    data=csv.reader(data_file)
    print(data)
    temprature=[]
    for row in data:
        if row[1]!="temp":
            temprature.append(row[1])
    print(temprature)