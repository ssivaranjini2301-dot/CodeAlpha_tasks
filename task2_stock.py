stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "MSFT": 300
}

print("📈 Stock Portfolio Tracker")

stock = input("Enter Stock Name (AAPL/TSLA/GOOGLE/MSFT): ").upper()

if stock in stock_prices:
    quantity = int(input("Enter Quantity: "))

    total = stock_prices[stock] * quantity

    print("\nStock Name :", stock)
    print("Price per Share :", stock_prices[stock])
    print("Quantity :", quantity)
    print("Total Investment : $", total)

    file = open("portfolio.txt", "w")
    file.write("Stock Portfolio Report\n")
    file.write("Stock Name: " + stock + "\n")
    file.write("Price: $" + str(stock_prices[stock]) + "\n")
    file.write("Quantity: " + str(quantity) + "\n")
    file.write("Total Investment: $" + str(total))
    file.close()

    print("\n✅ Report saved as portfolio.txt")

else:
    print("❌ Invalid Stock Name")

input("\nPress Enter to exit...")