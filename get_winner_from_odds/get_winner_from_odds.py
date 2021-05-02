import random

home = 1 / float(input('home odds: '))
draw = 1 / float(input('draw odds: '))
away = 1 / float(input('away odds: '))

odds_total = home + draw + away
total = odds_total - 1
total = 1 - (total / odds_total)

home = round(home*total*100, 2)
draw = round(draw*total*100, 2)
away = round(away*total*100, 2)
total = home + draw + away
print(f'{home}%')
print(f'{draw}%')
print(f'{away}%')
print()

random_number = random.randint(1, total*100)

if random_number/100 <= home:
    print('home wins')
elif random_number/100 <= home + draw:
    print('draw')
else:
    print('away wins')







# **********************TEST**********************
# import random

# h = 0
# d = 0
# a = 0
# for i in range(1,100000):
#     home = 1 / 3
#     draw = 1 / 3.4
#     away = 1 / 2.7

#     odds_total = home + draw + away
#     total = odds_total - 1
#     total = 1 - (total / odds_total)

#     home = home*total*100
#     draw = draw*total*100
#     away = away*total*100

#     total = round((home + draw + away),2)

#     random_number = random.randint(1, total*1000)
#     if random_number/1000 <= home:
#         h+=1
#     elif random_number/1000 <= (home+draw):
#         d+=1
#     else:
#         a+=1

# print(f'Home: 1.25 {home}% {h}')
# print(f'Draw: 4.75 {draw}% {d}')
# print(f'Away: 12.0 {away}% {a}')