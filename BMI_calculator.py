def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)."""


#calculate BMI
    BMI= weight/(height**2)
    return round(BMI, 2)

def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight", (
            """Advice: Increase your calorie intake by consuming nutrient-rich foods such as nuts, dairy, 
            whole grains, and healthy fats. Consider consulting a nutritionist for a personalized diet plan."""
        )
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", (
            """Advice: Maintain your current lifestyle by eating a balanced diet and staying physically active.
            Continue regular health check-ups to ensure you're on track."""
        )
    elif 25 <= bmi < 29.9:
        return "Overweight", (
            """Advice: Engage in regular physical activity, such as walking, jogging, or yoga.
            Focus on portion control and include more fruits and vegetables in your diet."""
        )
    else:
        return "Obese", (
            """Advice: Consider creating a structured weight-loss plan, including consulting a healthcare professional.
            Focus on reducing calorie intake, avoiding sugary and fried foods, and increasing physical activity."""
        )
def main():
    print("Welcome to the BMI Calculator!")

    # Input weight and height
    
    try:
       weight=int(input("enter your weight in kg: "))
       print("enter your height in feet:")
       heightInFeet=int(input("enter feet: "))
       heightInInches=int(input("enter inches: "))
          #covert height from feet to inches

       feetTOInches=(heightInFeet*12)+heightInInches
           #convert height from inches to meter

       inchesToMeter=feetTOInches*0.0254
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    if  inchesToMeter<= 0 or weight <= 0:
        print("Height and weight must be positive numbers.")
        return

    # Calculate and classify BMI
    bmi = calculate_bmi(weight,inchesToMeter)  
    category,advice= classify_bmi(bmi)
    print("=========================================================")
    print(f"Your BMI is {bmi}, which is considered {category}.")
    print(advice)
    print("=========================================================")

if __name__ == "__main__":
    main()
