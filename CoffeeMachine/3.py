num = int(input("Write how many cups of coffee ou will need: "))
print("For", num, "cups of coffee you will need: ")
print(num * 200, "ml of water")
print(num * 50, "ml of milk")
print(num * 15, "g of coffee beans")

water = int(input("Write how many ml of water the coffee machine has: "))
milk = int(input("Write how many ml of milk the coffee machine has: "))
beans = int(input("Write how many grams of coffee beans the coffe machine has: "))
amount1 = water // 200
amount2 = milk // 50
amount3 = beans // 15
amount4 = min(amount1, amount2, amount3)
amount5 = amount4 - num

if (num * 200 <= water) and (num * 50 <= milk) and (num * 15 <= beans) and amount5 == 0:
    print("Yes, I can make that amount of coffee")
elif (num * 200 < water) and (num * 50 < milk) and (num * 15 < beans):
    print("Yes, I can make that amount of coffee (and even", amount5, "more than that)")
elif (num * 200 > water) or (num * 50 > milk) or (num * 15 > beans):
    print("No, I can make only", amount4, "cups of coffee")

input("Press Enter to start")

print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")

input("Press Enter to end")





print("The coffee machine has:")
water = 400
print(water, "of water")
milk = 540
print(milk, "of milk")
beans = 120
print(beans, "of coffee beans")
cups = 9
print(cups, "of disposable cups")
money = 550
print(money, "of money")

def espresso():
    global water
    global beans
    global money
    water = water - 250
    beans = beans - 16
    money = money + 4
    return "water \n milk \n beans \n money"



bft = input("Write action (buy, fill, take):")
if bft == "buy":
    elc = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino:"))
    if elc == 1:
        espresso()

elif bft == "fill":
    print("fill")

elif bft == "take":
    print("take")