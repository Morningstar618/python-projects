# with open('weather_data.csv') as weather_data:
#     data = weather_data.readlines()

# print(data)

# import csv

# with open('weather_data.csv') as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data['temp'])
# print(type(data['temp']))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()

# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data['temp'].mean())

# print(data['temp'].max())


######### Get data in the columns ##############
# print(data['condition'])
# print(data.condition)

######## Get data in row ################
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

####### Create dataframe from Scratch #####
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65],
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv('new_data.csv')

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
red_count = data[data['Primary Fur Color'] == 'Cinnamon']['Primary Fur Color'].to_list().count('Cinnamon')
gray_count = data[data['Primary Fur Color'] == 'Gray']['Primary Fur Color'].to_list().count('Gray')
black_count = data[data['Primary Fur Color'] == 'Black']['Primary Fur Color'].to_list().count('Black')

data_dict = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [gray_count, red_count, black_count],
}

squirrel_count = pandas.DataFrame(data_dict)
squirrel_count.to_csv('squirrel_count.csv')

