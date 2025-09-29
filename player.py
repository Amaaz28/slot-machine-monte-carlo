#betting rules

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

class Player:
    #ititializes starting balance
    def __init__(self, balance=0):
        self.balance = balance

    #Asks the player to deposit money, must be positive integer. loops until valip input is entered.
    def deposit(self):
        while True:
            amount = input("Enter the amount you want to deposit: $")
            if amount.isdigit() and int(amount) > 0:
                self.balance = int(amount)
                break
            print("Please enter a valid amount greater than 0.")
            

    #lets payers bet on how many lines they want to bet on
    def get_number_of_lines(self):
        while True:
            lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
            if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
                return int(lines)
            print("Please enter a valid number of lines.")

    #Players choose bet per line
    def get_bet(self):
        while True:
            bet = input(f"Enter the bet per line (${MIN_BET}-${MAX_BET}): $")
            if bet.isdigit() and MIN_BET <= int(bet) <= MAX_BET:
                return int(bet)
            print("Please enter a valid bet amount.")
