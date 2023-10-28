import random

names = input('Enter names separated by a comma: ')

names_list = names.split(',')

random_num = random.randint(0, len(names_list - 1))

print(f'{names_list[random_num]} is going to pay the bill')