print('Welcome to love calculator!')
name1 = input('What is your name? \n').lower()
name2 = input('What is her name? \n').lower()

joined = name1 + name2

t = joined.count('t')
r = joined.count('r')
u = joined.count('u')
e = joined.count('e')

l = joined.count('l')
o = joined.count('o')
v = joined.count('v')

true = t + r + u + e
love = l + o + v

love_score = str(true) + str(love)

if int(love_score) < 10 or int(love_score) > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif int(love_score) in range(40, 51):
    print(f'your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}')