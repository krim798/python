# Paste your code into this box
balance=float(input("Enter balance amount"))
rate=float(input("Enter annual interest rate:"))
mPay=float(input("Enter min amount to be paid per month(in %):"))
monthlyInterestRate=(rate/100)/12
monthlyPaymentRate=mPay/100
for i in range(1,13):
    minimum_monthly_payment=balance*monthlyPaymentRate
    Monthly_Unpaid_Balance=balance-minimum_monthly_payment
    updated_balance=Monthly_Unpaid_Balance+(monthlyInterestRate*Monthly_Unpaid_Balance)
    balance=updated_balance
print('Remaining Balance:',round(balance,2))
