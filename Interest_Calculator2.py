# INTEREST RATE CALCULATOR

# AVERAGE DAILY BALANCE

avgDailyBalance = 0

# INPUT BALANCE SHOWN ON BILL FROM USER

netBalance = float(input('Please enter balance shown on bill: \n'))

# INPUT PAYMENT MADE FROM USER

payment = float(input('Please enter payment amount: \n'))

# INPUT NUMBER OF DAYS IN BILLING CYCLE FROM USER

d1 = int(input('Please enter number of day(s) in billing cycle: \n'))

# INPUT NUMBER OF DAYS PAYMENT WAS MADE BEFORE BILLING CYCLE

d2 = int(input('Please enter number of day(s) payment was made before billing cycle: \n'))

# INPUT MONTHLY RATE OF INTEREST FROM USER

monthly_interest = float(input('Please enter monthly interest: \n'))

# CALCULATE THE INTEREST 

avgDailyBalance = (netBalance * d1 - payment * d2) / d1

# REVIEW RESULT OF AVGDAILYBALANCE CALCULATION

avgDailyBalance

interest =  avgDailyBalance * monthly_interest

# REVIEW RESULT OF INTEREST CALCULATION

interest 

# OUTPUT INTEREST TO USER

print('Calculating....10%')

print('Calculating 20%')

print('Calculating 30%')

print('Calculating 40%')

print('Calculating 50%')

print('Calculating 60%')

print('Calculating 70%')

print('Calculating 80%')

print('Calculating 90%')

print('Calculating 100%')
print()
print('Your interest is: $', end = '')
print('{0:.2f}'.format(interest))
