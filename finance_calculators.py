import math
'''It is a program that allows the user to access two different financial calculators an investment calculator and a home loan repayment calculator.
The output is the total amount based on their input option.'''

print('=' * 80)
print('Finance Calculators')
print('=' * 80)

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

''' At least one of the conditions needs to be met <break> otherwise the else statement will be printed, and while loop will ask again for the user input.'''
while True:
  print('=' * 80)
  user_input = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower().strip()
  if user_input == 'investment': # user_input is equal a investment
    print('=' * 80)
    money_amount = float(input('Enter the amount of money that you are depositing: '))
    print('=' * 80)
    interest_r = int(input('Enter only the NUMBER of the interest rate: '))
    print('=' * 80)
    investment_time = int(input('Enter number of years you plan to invest: '))
    print('=' * 80)
    interest = int(input("Do you want the 'simple' or 'compound'?\n Enter [1] for Simple and [2] Compound: ")
    )
    print('=' * 80)
    interest_rate = interest_r / 100
    if interest == 1: # user_input is equal a Simple
      # Simle formula
      amount_simple = money_amount * (1 + interest_rate * investment_time)
       # The output is the total amount
      print('Total amount once the interest has been applied is £{:.2f}'.format(amount_simple))
      break
    elif interest == 2: # user_input is equal a Compound
      # Compound formula
      amount_compound = money_amount * math.pow((1 + interest_rate), investment_time)
      print('Total amount once the interest has been applied is £{:.2f}'.format(amount_compound))
      break
  elif user_input == 'bond': # user_input is equal a bond
    print('=' * 80)
    house_value = float(input('What is the present value of the house? '))
    print('=' * 80)
    interest_r_bond = int(input('Enter only the NUMBER of the interest rate: '))
    print('=' * 80)
    repay_time = int(input('Enter the number of months you plan to repay the bond? '))
    month_inv_rate = (interest_r_bond / 100) / 12
    # Bond formula
    repayment = (month_inv_rate * house_value) / (1 - (1 + month_inv_rate) ** (- repay_time))
    print('=' * 80)
     # The output for the total amount
    print('The amount that you will have to be repaid on a house loan each month is £{:.2f}'.format(repayment))
    print('=' * 80)
    break
  else:
    print('Invalid option. Try again!')

print('Thanks for using our services!')


  

