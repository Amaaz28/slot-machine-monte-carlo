class Strategy:
    def __init__(self, base_bet):
        self.base_bet = base_bet

    def get_next_bet(self, last_result):
        """
        Returns the next bet amount.
        `last_result` is optional info from the last spin (e.g., win/loss).
        """
        raise NotImplementedError("Subclasses must implement this method")

    def update(self, result):
        """
        Called after each spin to update strategy's state.
        `result` should be True for a win, False for a loss.
        """
        pass