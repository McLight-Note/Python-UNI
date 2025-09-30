import random as rd

'''low = 1
high = 100
options = ('rock', 'paper', 'scissors')
cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

# number = rd.randint(low, high)

option = rd.choice(options)
print(option)

card = rd.shuffle(cards)
print(card)'''

low = 1
high = 100
answer = rd.randint(low, high)
guesses = 0
is_running = True

print('- - - - - Number Guessing Game - - - -')
print(f'Select a number btw {low} and {high}')

while is_running:
    guess = input("Enter a guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low | guess > high:
            print(f'{guess} is out of range')
        elif guess < answer:
            print('Too low! Try again!')
        elif guess > answer:
            print('Too high! Try again!')
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print('Invalid guess')
        print(f'Please select a number btw {low} and {high}')
