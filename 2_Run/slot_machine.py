import random

def spin_row():
    symbols = ['😎', '📚', '🌙', '☁️︎', '🛠']

    '''
    result = []
    for symbol in range(3):
        result.append(random.choice(symbols))
    return result
    '''

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print('* * * * * * *')
    print(' | '.join(row))
    print('* * * * * * *')

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '😎':
            return bet * 150
        elif row[0] == '📚':
            return bet * 250
        elif row[0] == '🌙':
            return bet * 10
        elif row[0] == '☁️︎':
            return bet * 20
        elif row[0] == '🛠':
            return bet * 30
    return 0
        

def main():
    balance = 100
    print('* * * * * * * * * * *')
    print('Welcome to Python Slots')
    print('Symbols: 😎 📚 🌙 ☁️︎ 🛠')
    print('* * * * * * * * * * *')

    while balance > 0:
        print(f'Your current balance: ${balance}')

        bet = input('Place your bet amount: ')

        if not bet.isdigit():
            print('Please enter a valid number')
            continue

        bet = int(bet)

        if bet > balance:
            print('Insufficient funds')
            continue

        if bet <= 0:
            print('Bet must be greater than 0')
            continue

        balance -= bet

        row = spin_row()
        print('Spinning...\n')
        print_row(row)

        payout = 0
        payout = get_payout(row, bet)

        if payout > 0:
            print(f'You won ${payout}')
        else:
            print('Sorry, you lost this round')

        balance += payout
        

if __name__ == '__main__':
    main()