# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")#Runtime error as they were no brackets 

print("n")#Syntax error as grammar was incorrect

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "I am 24 years old"
#runtime error as integer was classified as string
age = "24"
#logical error 
print(age_Str )
#runtime error as int function not included

    # Variables declaring additional years and printing the total years of age
years_from_now = "3"
#syntax error ,no brackets
total_years = len(age + years_from_now )
print(total_years)
#logical erroe as int function not used


#syntax error - no brackets
      
# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = age * 12 + years_from_now
#logical error as computer cannot read code
#This should then be 24*12+36+6
print(total_months)#Logical error - calculation will not run


#HINT, 330 months is the correct answer

