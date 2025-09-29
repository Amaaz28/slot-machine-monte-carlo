from slot_Machine import SlotMachine
from player import Player

#defines a 3X3 slot machine
#each symbol is a payout multiplier

ROWS = 3
COLS = 3
SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
SYMBOL_VALUES = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

class Game:
    def __init__(self):
        self.slot_machine = SlotMachine(ROWS, COLS, SYMBOL_COUNT, SYMBOL_VALUES)
        self.player = Player()

    #starts by asking the player to deposit money
    def play(self):
        self.player.deposit()

        while True:
            print(f"\nCurrent balance: ${self.player.balance}")
            choice = input("Press Enter to play or 'q' to quit: ").lower()
            if choice == "q":
                break

            #player chooses how many lines to bet on and bet per line
            lines = self.player.get_number_of_lines()
            bet = self.player.get_bet()
            total_bet = bet * lines

            if total_bet > self.player.balance:
                print(f"Insufficient balance. You need ${total_bet}, but have ${self.player.balance}.")
                continue

            self.player.balance -= total_bet
            print(f"\nSpinning... You bet ${bet} on {lines} lines. Total: ${total_bet}")

            columns = self.slot_machine.spin()
            self.slot_machine.print_columns(columns)

            winnings, winning_lines = self.slot_machine.check_winnings(columns, lines, bet)
            self.player.balance += winnings

            print(f"\nYou won ${winnings}")
            if winning_lines:
                print("Winning on line(s):", ", ".join(map(str, winning_lines)))
            else:
                print("No winning lines this time.")

        print(f"\nThanks for playing! You left with ${self.player.balance}")


if __name__ == "__main__":
    game = Game()
    game.play()
