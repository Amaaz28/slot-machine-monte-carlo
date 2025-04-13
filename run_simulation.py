from strategy.flat import FlatBettingStrategy
from strategy.martingale import MartingaleStrategy
from simulation import Simulation
from strategy.fibonacci import FibonacciStrategy
import matplotlib.pyplot as plt

# Step 1: Get user input
strategy_type = input("Choose strategy (flat / martingale / fibonacci): ").strip().lower()
starting_balance = int(input("Enter starting balance: "))
base_bet = int(input("Enter base bet: "))
num_spins = int(input("Enter number of spins: "))

# Step 2: Create strategy
if strategy_type == "flat":
    strategy = FlatBettingStrategy(base_bet)
elif strategy_type == "martingale":
    strategy = MartingaleStrategy(base_bet)
elif strategy_type == "fibonacci":
    strategy = FibonacciStrategy(base_bet)
else:
    print("Invalid strategy.")
    exit()


sim = Simulation(strategy=strategy, num_spins=num_spins, starting_balance=starting_balance)

# Step 3: Run simulation
history, wins, losses, max_wins, max_losses, final_balance = sim.run()

# Step 4: Print stats
print(f"\n--- Simulation Stats ---")
print(f"Total Spins: {len(history)}")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Win Rate: {wins / len(history) * 100:.2f}%")
print(f"Longest Win Streak: {max_wins}")
print(f"Longest Loss Streak: {max_losses}")
print(f"Final Balance: ${final_balance}")

# Step 5: Plot the result
plt.plot(history, label=f"{strategy_type.capitalize()} Betting")
plt.title(f"{strategy_type.capitalize()} Strategy Performance")
plt.xlabel("Spin Number")
plt.ylabel("Balance ($)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()



