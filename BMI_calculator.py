def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)."""
    bmi = weight / (height ** 2) 
    return round(bmi, 2)

def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")

    # Input weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate and classify BMI
    bmi = calculate_bmi(weight, height)  
    category = classify_bmi(bmi)
    print(f"Your BMI is {bmi}, which is considered {category}.")

if __name__ == "__main__":
    main()
