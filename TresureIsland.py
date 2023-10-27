print('Welcome to Treasure Island.\nYour mission is to find the treasure.')

direction = input('Do you want to go Left or Right? ').lower()

if direction == 'right':
    print('Game Over!')
elif direction == 'left':
    activity = input('Do you want to Swim or Wait?').lower()
    if activity == 'wait':
        door = input('Choose a door between Red, Blue or Yellow.').lower()
        if door != 'yellow':
            print('Game Over!')
        else:
            print('You Win!')
    else:
        print('Game Over!')