import streamlit as st
import google.generativeai as genai


c1, c2 = st.columns([30,50])

c2.title("MedGuard: Medicine Information & Alternative Suggestions")
c1.image("logo-removebg-preview.png")
genai.configure(api_key="AIzaSyA-Q_oWOSu8fHygFWhQhqfkpLdtpYfTUS8")
var = ""
var2 = ""




def create_gen_model():
    return genai.GenerativeModel('models/gemini-1.5-pro')

def main():
    medicine_name = st.chat_input("Enter the Medicine Name:")

    # if st.button("Get Medicine Info and Alternatives"):
    if medicine_name:
        model = create_gen_model()

        # Query to get information about the medicine
        var = f"Can you provide detailed information about the medicine called {medicine_name}? Include the uses, side effects, and any important information related to the medicine."

        response = model.generate_content(var)

        # Display the medicine information
        if response and response.candidates:
            st.header("Medicine Information:")
            st.write(response.text)

            var2 = f"Please provide a list of alternative medicines that share the same active ingredients as {medicine_name}. Ensure that the alternatives have the similar medicinal content , suggest the antibiotics first and then go for any other Ayurvedic alternatives"
            response2 = model.generate_content(var2)

            # Check if the response contains valid candidates
            if response2 and response2.candidates:
                candidate = response2.candidates[0]  # Access the first candidate

                # Check if the candidate contains valid text
                if hasattr(candidate, 'text') and candidate.text:
                    st.header("Alternative Medicines:")
                    st.write(candidate.text)
                else:
                    st.write(response2.text)

if __name__ == "__main__":
    main()
