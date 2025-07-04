def stock_tracker():
    prices = {"AAPL": 180, "TSLA": 250, "GOOG": 130, "MSFT": 310}
    portfolio = {}

    print("Enter your stock holdings (type 'done' to finish):")
    while True:
        stock = input("Stock symbol: ").upper()
        if stock == "DONE":
            break
        if stock not in prices:
            print("Stock not found.")
            continue
        quantity = int(input("Quantity: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity

    total = 0
    for stock, qty in portfolio.items():
        value = prices[stock] * qty
        print(f"{stock}: {qty} x {prices[stock]} = ${value}")
        total += value

    print("\nTotal investment value: $", total)

    # Optional: Save to file
    with open("portfolio_summary.txt", "w") as f:
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} x {prices[stock]} = ${prices[stock] * qty}\n")
        f.write(f"\nTotal: ${total}")

if __name__ == "__main__":
    stock_tracker()
