import random

MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1

ROWS = 5
COLS = 5

Symbol_count = {
    "A": 2, 
    "B": 4,
    "C": 6,
    "D": 8 
} 

symbol_values = {
    "A": 5, 
    "B": 4,
    "C": 3,
    "D": 2 
} 

def check_winnings(columns, lines, bet, values):
    winnings = 0 
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check: 
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines
            

def get_spins(rows, cols, symbols): 
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols =  all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row], end="")
        print()


def deposit(): 
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): 
            amount = int(amount) 
            if amount > 0: 
                break
            else: 
                print("amount must be greater than 0")
        else: 
            print("Please enter a number")
    return amount     


def get_number_of_lines():
     while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():  
            lines = int(lines) 
            if 1 <= lines <= MAX_LINES: 
                break
            else: 
                print("Enter a valid number of lines")
        else: 
            print("Please enter a number")
     return lines

def get_bet():
    while True: 
        amount = input("what would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")
    return amount


def game_spins(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()

        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, you current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    spins = get_spins(ROWS, COLS, Symbol_count)
    print_slot_machine(spins)
    winnings, winning_lines = check_winnings(spins, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += game_spins(balance)
        if balance == 0:
            deposit_again = input("Your balance is $0. Would you like to deposit again? (Y/N) ")
            if deposit_again == "Y":
                balance += deposit()
            elif deposit_again == "N":
                break

    print(f"You left with ${balance}")
    
main()