# Request user to enter three products
# Request user to enter prices of products
# Calculate sum of products
# Calculate Average

product1 = input("Enter name of first product:")
product2 = input("Enter name of second product:")
product3 = input("Enter name of third product:")

product1price = float(input("Enter price of first product:"))
product2price = float(input("Enter price of second product:"))
product3price = float(input("Enter price of third product:"))

sum = product1 + product2 + product3
print(sum)
average = print(round(sum , 2)/2)