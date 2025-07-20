# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 300
}

portfolio = {}  # To store stock and quantity
total_investment = 0

print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# User input
while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
    except ValueError:
        print("Invalid quantity. Try again.")
        continue
    
    # Store in portfolio
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Calculate total investment
for stock, qty in portfolio.items():
    total_investment += stock_prices[stock] * qty

print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares at ${stock_prices[stock]} each")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: save to a file
save_option = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save_option == "yes":
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, "w") as f:
        f.write("Stock,Quantity,Price\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock},{qty},{stock_prices[stock]}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}")
    print(f"Portfolio saved to {filename}")