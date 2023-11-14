h = float(input("Enter your height in cm: "))
w = float(input("Enter your weight in kg: "))
bmi = w / (h / 100) ** 2
print("Your BMI is:", bmi)

if bmi <= 18.4:
    print('Underweight')
elif 18.5 <= bmi <= 24.9:
    print('Normal')
elif 25 <= bmi <= 29.9:
    print('Overweight')
elif 30 <= bmi <= 34.9:
    print('Obese class 1')
elif 35 <= bmi <= 39.9:
    print('Obese class 2')
else:
    print('Obese class 3')
