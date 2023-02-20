import random
menu = input("Welcome to the cafe 'Monti'! Please, type what you would like to order using comma \n").split(", ")

print('-------"Monti"-------')

total_price = 0
for item in menu:
    price = random.randint(40, 1200)
    total_price += price
    print(f'{item}............{price} hrn')

print(f'Total price: {total_price} hrn')
