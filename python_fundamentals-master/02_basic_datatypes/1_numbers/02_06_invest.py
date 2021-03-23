'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
investment_amount = float(input("Enter the amount of your investment: "))
interest_rate_percent = float(input("Enter your interest rate as a percent: "))
investment_length = float(input("Enter the length of your investment in years: "))

interest_rate_decimal = 1 + (interest_rate_percent / 100)
total_return = (investment_amount * interest_rate_decimal**investment_length)

print(f"Investment Amount: ${investment_amount:,}\nInterest Rate: {interest_rate_decimal}\nInvestment Length: {investment_length} years\n")
print(f"Total Return: ${total_return:.2f}")