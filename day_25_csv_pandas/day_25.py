# data = []
# with open("weather_data.csv", mode='r') as file:
#     for day in file.readlines():
#         data.append(day.strip())
# print(data)
# import csv
#
# # opening the csv file
# with open("weather_data.csv") as data_files:
#     data = csv.reader(data_files)
#     list_of_forecast = []
#     temperatures = []
#     # extracting from 'data' obj to 'list_of_forecast' list
#     for row in data:
#         list_of_forecast.append(row)
#     # converting the temps from 'str' to 'int'
#     for day in list_of_forecast[1:]:
#         temperatures.append(int(day[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data['temp'])
# converting to a dictionary
data_dict = data.to_dict()

sum_of_temps = 0
temp_list = data["temp"].to_list()

for d in temp_list:
    sum_of_temps += d

average_temp = int(sum_of_temps / len(temp_list))

print(average_temp)
# these two do the same thing
print(data["temp"].mean())

print(data["temp"].max())
# get data in columns
print(data["condition"])
print(data.condition)

print(data[data.day == 'Monday'])

print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
temp_in_f = (monday.temp * 1.8) + 32
print(temp_in_f)

# create a dataframe from scratch

data_dict = {
    'students': ['James', 'Ben', 'Logan'],
    'scores': [12, 43, 54]
}

data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')
print(data)
