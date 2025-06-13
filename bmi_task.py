# Request user to enter weight in (kg) and height in (m)
# Store weight and height into variables
# BMI is equal to weight divided by height
# State if statements for user

Weight = float(input("Enter your  weight in kg : "))
Height = float(input("Enter your height in m:"))

BMI= Weight/Height
if BMI >= 30:
    print("You are obese")
if BMI >= 25:
    print("You are normal")
if BMI >= 18.5:
    print("You are normal")
if BMI < 18.5:
    print("You are underweight")
