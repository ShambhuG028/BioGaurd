import streamlit as st
import google.generativeai as genai

c1, c2 = st.columns([30,50])
c2.title("PredictGuard: Predicting the disease based on symptoms")
c1.image("logo-removebg-preview.png")
# st.title("SymptomScan: Predicting the disease based on symptoms")
# st.write(" ")
# st.write(" ")
# st.write(" ")
# st.write(" ")
genai.configure(api_key="AIzaSyAM4tBqJzZ3Dxa7tSTXy94BxHQewyomcF8")
var = ""
var2=""


def create_gen_model():
    return genai.GenerativeModel('models/gemini-1.5-pro')


def main():
    query = st.chat_input("Enter the Symptoms:")
    # st.write(" ")
    # st.write(" ")
    if query:
        model = create_gen_model()
        var = f"I'm experiencing some symptoms like {query} While I can't expect a diagnosis from you, can you help me find disease name from some reliable resources online? If you found disease name only give that name. Not give resource name. Give answer in one line. Also give me suggestions that what can be the causes, suggest some precautions to be taken by the patient"
        response = model.generate_content(var)
        st.header("Disease Predicted:")
        st.header(response.text)

        var2=f"I am infected with disease known as {response.text}While I can't expect a diagnosis from you,can you help me to suugest propable medications related to this from some reliable sources online?"

        response2=model.generate_content(var2)
        st.header("Predicted Solution:")
        st.header(response2.text)


if __name__ == "__main__":
    main()
