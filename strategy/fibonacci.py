from .base import Strategy

class FibonacciStrategy(Strategy):
    def __init__(self, base_bet):
        super().__init__(base_bet)
        self.sequence = [1, 1]
        self.index = 0

    def get_next_bet(self, last_result):
        return self.sequence[self.index] * self.base_bet

    def update(self, result):
        if result:
            self.index = max(0, self.index - 2) # Win: Move back two steps in the sequence if possible
        else:
            #loss: Move forward in the sequence
            self.index += 1
            if self.index >= len(self.sequence):
                next_val = self.sequence[-1] + self.sequence[-2]
                self.sequence.append(next_val)

