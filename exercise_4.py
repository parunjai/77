#4
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / height**2
print("BMI is %.1f" %bmi)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obesity")

