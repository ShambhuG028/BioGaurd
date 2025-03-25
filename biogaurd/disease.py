import streamlit as st

# Define a set of questions and their corresponding choices
questions = {
    "Q1": {
        "question": "How often do you feel sad or hopeless?",
        "choices": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    },
    "Q2": {
        "question": "Do you have trouble sleeping?",
        "choices": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    },
    "Q3": {
        "question": "Do you experience excessive worry or anxiety?",
        "choices": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    },
    "Q4": {
        "question": "Do you feel tired or fatigued most of the time?",
        "choices": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    },
    "Q5": {
        "question": "Do you have trouble concentrating or making decisions?",
        "choices": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    },
    "Q6": {
        "question": "How often do you experience irritability or anger?",
        "choices": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    },
    "Q7": {
        "question": "Do you isolate yourself from others frequently?",
        "choices": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    },
    "Q8": {
        "question": "Do you engage in self-destructive behaviors?",
        "choices": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    },
    "Q9": {
        "question": "Do you feel hopeless about the future?",
        "choices": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    },
    "Q10": {
        "question": "Have you lost interest in activities you once enjoyed?",
        "choices": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    },
    # Add more questions as needed
}


def generate_mcq_test():
    mcq_test = {}
    for q, data in questions.items():
        mcq_test[q] = {
            "question": data["question"],
            "choices": data["choices"]
        }
    return mcq_test


def analyze_responses(responses):
    # Analyze responses and provide status and solutions
    total_score = 0
    for q, response in responses.items():
        if response == "Often" or response == "Always":
            total_score += 1
    if total_score >= 4:
        status = "You may be experiencing significant mental health issues. It is advisable to seek professional help."

        solution = "Seek professional help and consider therapy or counseling."

    elif total_score == 2:
        status = "You may be experiencing mild mental health issues. Consider adopting self-care strategies and seeking support if needed."

        solution = "Practice self-care activities such as exercise, meditation, and spending time with loved ones. Consider seeking support from friends, family, or a therapist."


    else:
        status = "Your mental health seems to be in a stable condition. Keep practicing self-care and seeking support if needed."

        solution = "Continue practicing self-care activities and maintain a healthy lifestyle."

    return status, solution


# Streamlit interface

st.markdown("""
    <style>
        .background {
            background-image: url("https://media.tenor.com/VW7r4lcGlvMAAAAM/happy-hogging-thumbs-up.gif");
            background-size: cover;
            height: 100%;
            width: 100%;
            position: absolute;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="background">', unsafe_allow_html=True)

c1, c2 = st.columns([30,50])
c2.title("MindGuard: Psychological Condition Assessment Test")
c1.image("logo-removebg-preview.png")
# st.title("Psychological Condition Assessment Test")

test = generate_mcq_test()
responses = {}

for q, data in test.items():
    st.write(q + ": " + data["question"])
    response = st.radio("", data["choices"], key=q)  # Unique key for each radio button
    responses[q] = response

if st.button("Submit"):
    status, solution = analyze_responses(responses)
    st.write("\n## Status of Mental Health")
    st.write(status)

    st.write("\n## Solution")
    st.write(solution)
