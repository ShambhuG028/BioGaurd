import streamlit as st
import google.generativeai as genai
import requests

# Configure Google Generative AI (provide your own API key)
genai.configure(api_key="AIzaSyA6OoC5r1E2tV4cyRxRwU2NLxIROImY0fw")


# Function to get emergency information from Gemini
def get_emergency_info(keyword, location):
    model = genai.GenerativeModel('models/gemini-1.5-pro')

    # Formulate the query for the AI model
    query = (f"I am experiencing a medical emergency related to {keyword}. "
             f"My current location is {location}. Can you provide the cell phone numbers of the minimum 5 nearest hospitals, "
             "ambulances, and the location of the hospital, along with an estimate of the time it will take to reach help?")

    # Get AI-generated content
    response = model.generate_content(query)
    return response.text


# Main Emergency Services function
def emergency_services_main():
    c1, c2 = st.columns([30, 50])
    c2.title("RescueGuard:  Provides Emergency Contacts & Locations")
    c1.image("logo-removebg-preview.png")
    st.write("Please provide the details of your emergency below.")

    # Input fields
    keyword = st.text_input("Enter the type of emergency (e.g., accident, pregnancy, etc.):")
    location = st.text_input("Enter your current location (e.g., address or coordinates):")

    if st.button("Get Emergency Help"):
        if keyword and location:
            # Get emergency information from the Gemini model
            emergency_info = get_emergency_info(keyword, location)

            # Display the recommendations
            st.subheader("Emergency Help Information:")
            st.write(emergency_info)
        else:
            st.warning("Please enter both the type of emergency and your location.")


if __name__ == "__main__":
    emergency_services_main()
