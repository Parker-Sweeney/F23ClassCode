# Area of a square
side = int(input('How long is one side of the square? '))
print('The area is',side * side, 'units')

#Loan calculation
loan_amt = input(('What is your loan amount? '))
interest_rate = input('What is your interest rate for this loan (input as a decimal)?')
balance = float(loan_amt) * float(interest_rate)
print('Your student loan balance after one year is', balance)
