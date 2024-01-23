# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 5 * 12
extra_payment_end_month = 9 * 12
extra_payment = 1000

while principal > 0:
    month = month + 1

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if extra_payment_start_month <= month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal < 0:
        overpayment = abs(principal)
        principal = principal + overpayment
        total_paid = total_paid - overpayment

    print(f'{month} ${total_paid:,.2f} ${principal:,.2f}')
    
print(f'Total paid: ${total_paid:,.2f}')
print(f'Months: {month}')