print("investment -to calculate the amount of interest you will earn on your investment")
print("bond-to calculate the amount youwill have to pay on a home loan")

import math
financial_calculator = input("Enter either investment or bond to proceed:")
#investment calculator
principal = 0
interest = 0
time = 0
while principal <= 0:
    principal = float(input("Enter the amount of money deposited:"))
    if principal <= 0:
        print("principal amount cannot be less than or equal to zero")


while interest <= 0:
    interest = float(input("Enter the interest rate:"))
    if interest <= 0:
        print("interest cannot be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the number of years:"))
    if time <= 0:
        print("number of years cannot be less than or equal to zero")


print(principal)
print(interest)
print(time)
interest_rate = input("Enter simple or compound interest:")
if simple:
    print(total = principal*(1+interest*time))
if compound:
    print(total=principal*(1+interest*time))


#bond calculator
principal = 0
interest = 0
time = 0


while principal <= 0:
    principal = float(input("Enter the amount of money deposited:"))
    if principal<= 0:
        print("principal amount cannot be less than or equal to zero")

while interest <= 0:
    interest = float(input("Enter the interest rate:"))
    if interest<= 0:
        print("interest cannot be less than or equal to zero")


while time <= 0:
    time = int(input("Enter the number of years:"))
    if time<= 0:
        print("number of years cannot be less than or equal to zero")


repayments = (interest*principal)/(1-(1+i)*(-time))
print(repayments)