from .base import Strategy

class FlatBettingStrategy(Strategy):
    def get_next_bet(self, last_result):
        return self.base_bet

'''

A strategy that:

    Always returns the same bet size (e.g., $10)

    Doesn’t care if you win or lose — it’s predictable

    Can now be passed into your future simulation engine

'''