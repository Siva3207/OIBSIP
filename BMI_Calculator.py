def calculate(weight, height):
    bmi= weight/height**2
    return bmi
def classify(bmi):
    if bmi<18.5:
        return "Underweight"
    elif 18.5<=bmi < 24.9:
        return "Normal weight"
    elif 25<=bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
def main():
    try:
        weight = float(input("Enter your weight in kg:"))
        height = float(input("Enter your height in meters:"))
        bmi = calculate(weight,height)
        category = classify(bmi)
        print(f"Your BMI is:{bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Please enter valid numbers for weight and height.")

if __name__ == "_main_":
    main()
