#welcome to stock portfolio tracker system
print("Welcome to the Stock Portfolio Tracker System!")
import csv

# Stock prices
stock_prices = {
    "AAPL": 180, "TSLA": 250,"GOOGL": 140,"MSFT": 420,"AMZN": 190,"META": 550,
    "NFLX": 700,"NVDA": 145,"AMD": 165,"INTC": 35,
    "ORCL": 280,"IBM": 250,"UBER": 95,"DIS": 110, "PYPL": 80
}

total_investment = 0
portfolio = []

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    portfolio.append([stock, quantity, price, investment])

    print(f"{stock}: ${price} x {quantity} = ${investment}")

print("\n=== Portfolio Summary ===")

for item in portfolio:
    print(
        f"Stock: {item[0]} | "
        f"Quantity: {item[1]} | "
        f"Price: ${item[2]} | "
        f"Investment: ${item[3]}"
    )

print(f"\nTotal Investment: ${total_investment}")

# Save portfolio to CSV file
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Stock",
        "Quantity",
        "Price",
        "Investment"
    ])

    for row in portfolio:
        writer.writerow(row)

print("Portfolio saved to portfolio.csv")