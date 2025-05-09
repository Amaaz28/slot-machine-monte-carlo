import random

class SlotMachine:
    def __init__(self, rows, cols, symbol_count, symbol_values):
        self.rows = rows
        self.cols = cols
        self.symbol_count = symbol_count
        self.symbol_values = symbol_values

    def spin(self):
        all_symbols = []
        for symbol, count in self.symbol_count.items():
            all_symbols += [symbol] * count

        columns = []
        for _ in range(self.cols):
            column = []
            current_symbols = all_symbols[:]
            for _ in range(self.rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
            columns.append(column)

        return columns

    def check_winnings(self, columns, lines, bet):
        winnings = 0
        winning_lines = []

        for line in range(lines):
            symbol = columns[0][line]
            if all(column[line] == symbol for column in columns):
                winnings += self.symbol_values[symbol] * bet
                winning_lines.append(line + 1)

        return winnings, winning_lines

    def print_columns(self, columns):
        for row in range(self.rows):
            for i, column in enumerate(columns):
                end_char = " | " if i != len(columns) - 1 else ""
                print(column[row], end=end_char)
            print()






    
    
        
