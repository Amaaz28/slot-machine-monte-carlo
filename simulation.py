from slot_Machine import SlotMachine
from strategy.flat import FlatBettingStrategy

class Simulation:
    def __init__(self, strategy, num_spins, starting_balance):
        self.strategy = strategy
        self.num_spins = num_spins
        self.balance = starting_balance

        self.machine = SlotMachine(
        rows=3,
        cols=3,
        symbol_count={"A": 2, "B": 4, "C": 6, "D": 8},
        symbol_values={"A": 5, "B": 4, "C": 3, "D": 2}
        )

        self.total_wins = 0                     # Counts how many spins were wins
        self.total_losses = 0                   # Counts how many spins were losses
        self.current_streak = 0                 # Positive for win streak, negative for loss streak
        self.max_win_streak = 0                 # Highest number of wins in a row
        self.max_loss_streak = 0                # Highest number of losses in a row
    
    def run(self):
        history = []

        for _ in range(self.num_spins):
            bet = self.strategy.get_next_bet(None)

            if self.balance  < bet:
                break
            self.balance -= bet
            columns = self.machine.spin()

            winnings, _ = self.machine.check_winnings(columns, lines=1, bet=bet)

            self.balance += winnings
            if winnings > 0:
                self.total_wins += 1
                self.current_streak = self.current_streak + 1 if self.current_streak >= 0 else 1
                self.max_win_streak = max(self.max_win_streak, self.current_streak) 
            else:
                self.total_losses += 1
                self.current_streak = self.current_streak - 1 if self.current_streak <= 0 else -1
                self.max_loss_streak = max(self.max_loss_streak, abs(self.current_streak))

            self.strategy.update(winnings > 0)
            history.append(self.balance)
        
        # In simulation.py
        return history, self.total_wins, self.total_losses, self.max_win_streak, self.max_loss_streak, self.balance


