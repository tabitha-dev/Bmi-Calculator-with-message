weight_lbs = float(input("Enter your weight in pounds: "))
height_ft = float(input("Enter your height in feet: "))

# Convert weight from pounds to kg
weight_kg = weight_lbs / 2.205

# Convert height from feet to meters
height_m = height_ft / 3.281

# Calculate the BMI
bmi = round(weight_kg / (height_m ** 2))

# Check the BMI value and print the interpretation
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")