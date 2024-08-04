import random

number_min_range = int(input("Min Number: ")) # Get user input number of minimum range
number_max_range = int(input("Max Number: ")) # Get user input number of maximum range
number_result = random.randint(number_min_range, number_max_range) # Generate result number with random from range

user_guessed = []
guess_status = False

def guess(number_result):
    count_guess = 0

    while True:
        user_guess = int(input("Guess the number ({}): ".format(count_guess + 1))) # Get user input of the guess number
        user_guessed.append(user_guess) # Store the guessed number to array

        count_guess += 1 # Count of guesses add 1 every guess

        if user_guess == number_result: # Check if user guess equal to result number
            break

    print()

    return count_guess

print()

print("Guess Count: {}".format(guess(number_result))) # Print how much guess
print("Guessed Number: {}".format(user_guessed)) # Print guessed number