# Request  user t enter their year of birth
# if they are 18 or above, use if > then print "Congrats you are old enough"

year_born = int(input("Enter year of birth:"))
if year_born <= 2006:
    print("congrats you are old enough")
elif year_born >= 2006:
    print("You are not old enough")
else:
    ("Incorrect selection,please try again")      
    year_born = int(input("Enter year of birth:"))
    
   
   