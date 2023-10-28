import random

names = input('Enter names separated by a comma: ')

names_list = names.split(',')

random_int = random.randint(0, len(names_list))

print(f'{names_list[random_int]} is going to pay the bill')