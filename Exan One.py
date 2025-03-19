import random

print("Hello! What is your name?")
name = input()

print("\nWell, " + name + ", I am thinking of a number between 1 and 20.")
print("You have 5 guesses.\n")

secret_number = random.randint(1, 20)
guesses_taken = 0

while guesses_taken < 5:
    print("Take a guess:")
    guess = input()
    guess = int(guess)
    
    guesses_taken = guesses_taken + 1
    
    if guess > secret_number:
        print("Your guess is too high.\n")
    elif guess < secret_number:
        print("Your guess is too low.\n")
    else:
        print("Good job, " + name + "! You guessed my number in " + str(guesses_taken) + " guesses!")
        break

if guess != secret_number:
    print("Nope. The number I was thinking of was " + str(secret_number) + ".")