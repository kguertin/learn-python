print("***** BMI Calculator *****")

height = float(input("Please enter your height (inches): "))
weight = float(input("Please enter your you weight (pounds): "))

bmi = round((weight * 703) / (height * height), 1)

if bmi < 16.0:
    print(f"Your BMI is {bmi}. You are severely underweight.")
elif bmi < 18.4:
        print(f"Your BMI is {bmi}. You are underweight.")
elif bmi < 24.9:
        print(f"Your BMI is {bmi}. You are a normal weight.")
elif bmi < 29.9:
        print(f"Your BMI is {bmi}. You are overweight.")
elif bmi < 34.9:
        print(f"Your BMI is {bmi}. You are moderately obese.")
elif bmi < 39.9:
        print(f"Your BMI is {bmi}. You are severely obese.")
else: 
        print(f"Your BMI is {bmi}. You are morbidly obese.")