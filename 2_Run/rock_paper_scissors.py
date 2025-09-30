import random

options = ('rock', 'paper', 'scissors')
running = True

while running:

    player = None
    computer = random.choice(options)
    
    player = input('Enter a choice (rock, paper, scissors): ')

    while player not in options:
        player = input('Enter a choice (rock, paper, scissors): ')

    if player == computer:
        print('Tie')
    elif player == 'rock' and computer == 'scissors':
        print('You win!')
    elif player == 'scissors' and computer == 'paper':
        print('You win!')
    elif player == 'paper' and computer == 'rock':
        print('You win!')
    else:
        print('You lost bro!')
    
    if not input('Play again? (y/n): ').lower() == 'y':
        running = False

print('Thanks for playing!')