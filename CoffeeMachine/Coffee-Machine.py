water = 400
milk = 540
beans = 120
cups = 9
money = 550

def print_coffee(water, milk, beans, cups, money):
    print("\nThe coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")

def espresso():
    global water
    global beans
    global money
    global milk
    global cups
    watere = water - 250
    beanse = beans - 16
    moneye = money - 4
    cupse = cups -  1
    if water >= 250 and beans >= 16 and cups >= 1:
        print("I have enough resources, making you a coffee!")
        water -= 250
        beans -= 16
        money += 4
        cups -= 1
    elif watere < 250:
        print("Sorry, not enough water!")
    elif beanse < 16:
        print("Sorry, not enough beans!")
    elif cupse < 1:
        print("Sorry, not enough cups!")
    
def latte():
    global water
    global beans
    global money
    global milk
    global cups
    waterl = water - 350
    milkl = milk - 75
    beansl = beans - 20
    moneyl = money - 7
    cupsl = cups - 1
    if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
        print("I have enough resources, making you a coffee!")
        water -= 350
        milk -= 75
        beans -= 20
        money += 7
        cups -= 1
    elif waterl < 350:
        print("Sorry, not enough water!")
    elif milkl < 75:
        print("Sorry, not enough milk!")
    elif beansl < 20:
        print("Sorry, not enough beans!")
    elif cupsl < 1:
        print("Sorry, not enough cups!")

def cappuccino():
    global water
    global beans
    global money
    global milk
    global cups
    waterc = water - 200
    milkc = milk - 100
    beansc = beans - 12
    moneyc = money + 6
    cupsc = cups - 1
    if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
        print("I have enough resources, making you a coffee!")
        water -= 200
        milk -= 100
        beans -= 12
        money += 6
        cups -= 1
    elif waterc < 200:
        print("Sorry, not enough water!")
    elif milkc < 100:
        print("Sorry, not enough milk!")
    elif beansc < 12:
        print("Sorry, not enough beans!")
    elif cupsc < 1:
        print("Sorry, not enough cups!")
    
def fill():
    global water
    global beans
    global money
    global milk
    global cups
    plus_water = int(input("Write how many ml of water do you want to add: \n"))
    plus_milk = int(input("Write how many ml of milk do you want to add: \n"))
    plus_beans = int(input("Write how many grams of coffee beans do you want to add: \n"))
    plus_cups = int(input("Write how many disposable cups of coffee do you want to add: \n"))
    water += plus_water
    milk += plus_milk
    beans += plus_beans
    cups += plus_cups

def take():
    global water
    global beans
    global money
    global milk
    global cups
    print("\nI gave you $", money)
    money -= money
    
def remaining():
    global water
    global beans
    global money
    global milk
    global cups
    print_coffee(water, milk, beans, cups, money)

while True:
    bft = input("\nWrite action (buy, fill, take, remaining, exit):\n")
    if bft == "buy":
        elc = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino:\n")
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
    elif bft == "fill":
        fill()
    elif bft == "remaining":
        remaining()
    elif bft == "exit":
        break
