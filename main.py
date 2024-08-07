import random

MAX_NUMBER = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
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

def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_mechine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_mechine(columns):
    for row in range(len(columns)):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row],end="")
        print()
    print(columns)

def deposit():
    while True:
        amount = input("What would you like to deposit?: $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0: 
                break
            else:
                print("amount should be greater than 0")
        else:
            print("please enter valid digit only!")
    return amount

def get_num_of_lines():
    while True:
        lines = input("Enter Number of lines to bet on (1-"+ str(MAX_NUMBER)+") ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_NUMBER:
                break
            else:
                print("lines should be between 1 to " + str(MAX_NUMBER))
        else:
            print("please enter valid digit only!")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET: 
                break
            else:
                print(f"amount should be between {MIN_BET} - {MAX_BET}")
        else:
            print("please enter Number!")
    return amount

def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"you don't have enough deposit to bet. your balance is {balance}")
        else: 
            break
    print(f"You are betting ${bet} on {lines} lines and the total bet is: {total_bet}")

    slots = get_slot_mechine_spin(3,3, symbol_count)
    print_slot_mechine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_values)
    print(f"you won: {winnings}")
    print(f"you won on lines: ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"your current balance is ${balance}")
        anwser = input("press enter to play (q to Quit)")
        if anwser == "q":
            break
        balance += spin(balance)

main()
# print(get_slot_mechine_spin(3,3, symbol_count))