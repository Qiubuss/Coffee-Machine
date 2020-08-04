import random

print("------------------")
print("M&M guessing game!")
print("------------------\n")

mm_count = random.randint(1, 100)

print("Guess the number of M&Ms and you get lunch on the house!\n")

n = 0

while n < 5:
    guess = int(input("How many M&Ms are in the jar?\n"))
    n += 1
    if guess == mm_count:
        print("Right answer")
        break
    elif guess > mm_count:
        print("Too HIGH")
    else:
        print("Too LOW")

print(f"You're done in {n} attempts!")