import streamlit as st
import google.generativeai as genai

# Configure Google Generative AI (provide your own API key)
genai.configure(api_key="AIzaSyARaKdiG56-K2pYRPsMG3ijyDgo-3Rfr9c")


# Function to get emergency loan information from Gemini
def get_loan_info(hospital_name):
    model = genai.GenerativeModel('models/gemini-1.5-pro')

    # Formulate the query for the AI model
    query = (f"I need emergency loan services because I'm at {hospital_name} and need funds for treatment. "
             f"Please provide the following information: 1. Private Money Lenders, 2. Quick Loan Services, "
             f"3. Information and contact details of the Owners and Deans of {hospital_name}, "
             f"4. Quick Credit Card Services.")

    # Get AI-generated content
    response = model.generate_content(query)
    return response.text


# Main Emergency Loan Services function
def emergency_loan_services_main():
    c1, c2 = st.columns([30, 50])
    c2.title("FundGuard:  Offers Quick Loan Services For Emergencies")
    c1.image("logo-removebg-preview.png")





    # Input field for hospital name
    hospital_name = st.chat_input("Enter the name of the Nearby Hospital:")


    if hospital_name:
            # Get loan information from the Gemini model
        loan_info = get_loan_info(hospital_name)

        # Display the recommendations
        st.subheader("Emergency Loan Information:")
        st.write(loan_info)



if __name__ == "__main__":
    emergency_loan_services_main()
