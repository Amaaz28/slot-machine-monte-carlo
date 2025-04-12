import streamlit as st
from strategy.flat import FlatBettingStrategy
from strategy.martingale import MartingaleStrategy
from strategy.fibonacci import FibonacciStrategy
from simulation import Simulation

st.set_page_config(page_title="Slot Machine Simulator", layout="centered")

st.title("🎰 Slot Machine Strategy Simulator")

st.markdown("""
Welcome to the **Monte Carlo simulator** for slot machine betting strategies.

This tool lets you experiment with three popular strategies:
- 🎯 **Flat Betting** — simple, same bet every time
- 🔁 **Martingale** — doubles bet after each loss
- 🔺 **Fibonacci** — bets follow the Fibonacci sequence

You can:
- Adjust starting balance, base bet, and number of spins
- Visualize your balance over time
- Track win/loss rate, streaks, and final outcome
""")

# Sidebar for user inputs
strategy_type = st.sidebar.selectbox("Choose a Strategy", ["Flat", "Martingale", "Fibonacci"])
starting_balance = st.sidebar.number_input("Starting Balance", min_value=100, value=1000, step=100)
base_bet = st.sidebar.number_input("Base Bet", min_value=1, value=10, step=1)
num_spins = st.sidebar.number_input("Number of Spins", min_value=1, value=100, step=10)

# Button to run simulation
if st.sidebar.button("Run Simulation"):
    # Strategy selection

    if strategy_type == "Flat":
        strategy = FlatBettingStrategy(base_bet)
    elif strategy_type == "Martingale":
        strategy = MartingaleStrategy(base_bet)
    elif strategy_type == "Fibonacci":
        strategy = FibonacciStrategy(base_bet)
    else:
        st.error("Invalid strategy selected")
        st.stop()

    sim = Simulation(strategy=strategy, num_spins=num_spins, starting_balance=starting_balance)
    history, wins, losses, max_wins, max_losses, final_balance = sim.run()

    # Results
    st.subheader("📈 Balance Over Time")
    st.line_chart(history)

    st.subheader("📊 Simulation Stats")
    st.write(f"**Total Spins**: {len(history)}")
    st.write(f"**Wins**: {wins}")
    st.write(f"**Losses**: {losses}")
    st.write(f"**Win Rate**: {wins / len(history) * 100:.2f}%")
    st.write(f"**Longest Win Streak**: {max_wins}")
    st.write(f"**Longest Loss Streak**: {max_losses}")
    st.write(f"**Final Balance**: ${final_balance}")

