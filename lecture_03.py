# arithmatic operations
# addition (+)
# base values 
num1 = 15
num2 = 25 
sum = num1 + num2
# print (f"sum , {num1} + {num2} = {sum}")
# subtraction (-)
diff = num1 - num2
# print (f"diff , {num1} - {num2} = {diff}")

# multiplication (*)
multiply =num1 * num2
# print (f"multiply , {num1} * {num2} = {multiply}")

# division (/)
division = num2 / num1 
# ?print (f"division , {num2} / {num1} = {division}")

# floor_division (//)
floor_division = num2 //num1
# print (f"floor_division , {num2} // {num1} = {floor_division}")

# modulus (%)
modulus =num2 % num1
# print (f"modulus , {num2} % {num1} ={modulus}")

# exponentiation (**)
exponentiation =num2 ** 2
# print (f"exponentiation , {num2} **2 = {exponentiation}")
exponentiation =3 ** 3
# print (f"{exponentiation}")

# input from user
# num3 = int(input("enter frist number: "))
# num4 = int(input("enter second number: "))
# sum1 = num3 + num4 
# print (f"sum , {num3} + {num4} = {sum1}")

# The program must calculate using arithmetic operators only:

# Total Income = sum of all income sources

# Total Expenses = sum of all expenses

# Monthly Savings = total income - total expenses

# Average Income per Member = total income / total_members

# Average Expense per Member = total expenses / total_members

# Saving per Member = monthly savings / total_members

# Percentage of Savings = (monthly_savings / total_income) * 100
# (This is allowed since / and * are arithmetic operators)

# Example Output:
# Enter father's income: 80000
# Enter mother's income: 40000
# Enter side business income: 15000
# Enter other income: 5000

# Enter house rent: 30000
# Enter utilities: 8000
# Enter groceries: 15000
# Enter transport: 5000
# Enter education: 6000
# Enter entertainment: 3000
# Enter miscellaneous: 2000

# Enter total family members: 4

# Total income: 140000.0
# Total expenses: 69000.0
# Monthly savings: 71000.0
# Average income per member: 35000.0
# Average expense per member: 17250.0
# Saving per member: 17750.0
# Percentage of savings: 50.71%

father_income = float(input("Enter father's income: "))
mother_income = float(input("Enter mother's income: "))
side_business_income = float(input("Enter side business income: "))
other_income = float(input("Enter other income: "))
total_income = father_income + mother_income + side_business_income + other_income
house_rent = float(input("Enter house rent: "))
utilities = float(input("Enter utilities: "))
groceries = float(input("Enter groceries: "))
transport = float(input("Enter transport: "))
education = float(input("Enter education: "))
entertainment = float(input("Enter entertainment: "))
miscellaneous = float(input("Enter miscellaneous: "))
total_expenses = house_rent + utilities + groceries + transport + education + entertainment + miscellaneous
monthly_savings = total_income - total_expenses
total_members = int(input("Enter total family members: "))
average_income_per_member = total_income / total_members
average_expense_per_member = total_expenses / total_members
saving_per_member = monthly_savings / total_members
percentage_of_savings = (monthly_savings / total_income) * 100
print (f"Total income: {total_income}")
print (f"Total expenses: {total_expenses}")
print (f"Monthly savings: {monthly_savings}")
print (f"Average income per member: {average_income_per_member}")
print (f"Average expense per member: {average_expense_per_member}")
print (f"Saving per member: {saving_per_member}")
print (f"Percentage of savings: {percentage_of_savings:.2f}%")
