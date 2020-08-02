water = 400
milk = 540
beans = 120
cups = 9
money = 550

def print_coffee(water, milk, beans, cups, money):
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")

print_coffee(water, milk, beans, cups, money)

def espresso():
    global water
    global beans
    global money
    global milk
    global cups
    water -= 250
    beans -= 16
    money += 4
    cups -= 1
    print_coffee(water, milk, beans, cups, money)

def latte():
    global water
    global beans
    global money
    global milk
    global cups
    water -= 350
    milk -= 75
    beans -= 20
    money += 7
    cups -= 1
    print_coffee(water, milk, beans, cups, money)

def cappuccino():
    global water
    global beans
    global money
    global milk
    global cups
    water -= 200
    milk -= 100
    beans -= 12
    money += 6
    cups -= 1
    print_coffee(water, milk, beans, cups, money)

def fill():
    global water
    global beans
    global money
    global milk
    global cups
    plus_water = int(input("Write how many ml of water do you want to add: "))
    plus_milk = int(input("Write how many ml of milk do you want to add: "))
    plus_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    plus_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    water += plus_water
    milk += plus_milk
    beans += plus_beans
    cups += plus_cups
    print_coffee(water, milk, beans, cups, money)

def take():
    global water
    global beans
    global money
    global milk
    global cups
    print("I gave you $", money)
    money -= money
    print_coffee(water, milk, beans, cups, money)

bft = input("Write action (buy, fill, take): ")
if bft == "buy":
    elc = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino:")
    if elc == "1":
        espresso()
    elif elc == "2":
        latte()
    elif elc == "3":
        cappuccino()
elif bft == "fill":
    fill()
elif bft == "take":
    take()