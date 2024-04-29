print("This is a BMI calculator")

print(" ")

height = int(input("Enter your height in inches: "))
weight = int(input("Enter yout weight in pounds: "))
heightsq = height * height
bmi = weight / heightsq
metric = bmi * 703
print("Your BMI is: " + str(metric))

if metric <= 18.5:
  print("Your weight is in the under weight category.")
  
elif (metric > 18.5) & (metric <= 24.9):
  print("You are in the heathy category")
