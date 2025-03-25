import streamlit as st
import google.generativeai as genai

c1, c2 = st.columns([30,50])
c2.title("FitGuard: Calculates BMI & Suggests Fitness Plan")
c1.image("logo-removebg-preview.png")
# Configure Google Generative AI (provide your own API key)
genai.configure(api_key="AIzaSyBzPWEwPR-RMJNkhMWFsrCRHIlIRP2fqxw")


# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


# Function to suggest a basic plan based on BMI
def suggest_plan(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


# Function to interact with the Gemini model for detailed recommendations
def get_gemini_recommendation(bmi_status, health_condition):
    model = genai.GenerativeModel('models/gemini-1.5-pro')

    # Formulate the query for the AI model
    query = (f"My BMI status is {bmi_status}, and I have underlying diseases like {health_condition}. "
             f"Can you suggest a personalized diet plan and fitness strategy for me based on these inputs? "
             "Make sure the suggestions are easy to follow and realistic.")

    # Get AI-generated content
    response = model.generate_content(query)
    return response.text


# Main FitGuard function
def fitguard_main():

    # Input fields
    height = st.number_input("Enter your height (in meters):", min_value=0.5, max_value=2.5, step=0.01)
    weight = st.number_input("Enter your weight (in kilograms):", min_value=10.0, max_value=200.0, step=0.1)
    health_condition = st.text_input("Enter any prior health conditions like blood pressure, diabetes, etc.:")

    if st.button("Calculate BMI & Get Plan"):
        if height > 0 and weight > 0:
            bmi = calculate_bmi(weight, height)
            bmi_status = suggest_plan(bmi)

            # Display BMI
            st.subheader(f"Your BMI: {bmi:.2f} ({bmi_status})")

            # Get AI-generated diet and fitness plan
            gemini_recommendation = get_gemini_recommendation(bmi_status, health_condition)

            # Display the recommendations
            st.subheader("Recommended Plan (AI Generated):")
            st.write(gemini_recommendation)
        else:
            st.warning("Please enter valid height and weight values.")


if __name__ == "__main__":
    fitguard_main()
