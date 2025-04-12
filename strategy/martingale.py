from .base import Strategy

class MartingaleStrategy(Strategy):
    def __init__(self, base_bet):
        super().__init__(base_bet)
        self.current_bet = base_bet

    def get_next_bet(self, last_result):
        return self.current_bet
    
    def update(self, result):
        if result:
            self.current_bet = self.base_bet  # Reset to base bet on win
        else:
            self.current_bet *= 2