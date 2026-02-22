print("hello adity")

a = 2
b = 4

c = a*b

print(c)

for i in range (1, 100):
    print(i%2==5)


seq  = range(1,10,2)
for i in seq:
    print(i)


import random

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number
secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
        break
    
print("hello aditya kasaudhan")