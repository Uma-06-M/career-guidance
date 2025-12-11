
import streamlit as st
import pandas as pd
import numpy as np
# In a real application, you would load your trained model and any necessary preprocessors here.
# For demonstration, we'll use dummy logic.

st.set_page_config(page_title="Student Career Guidance", page_icon=":graduated_cap:", layout="centered")

st.title("Student Career and Scholarship Guidance")
st.write("### Enter student details to get career and scholarship recommendations.")

st.markdown("--- ")

# Input fields for student characteristics based on your dataset columns
interests = st.selectbox('Interests', ['Maths', 'Arts', 'Science', 'Business', 'Medicine', 'Sports', 'Technology', 'Design'])
strengths = st.selectbox('Strengths', ['Communication', 'Analysis', 'Problem Solving', 'Public Speaking', 'Logical Thinking', 'Creativity'])
skills = st.selectbox('Skills', ['Java', 'Biology', 'Drawing', 'Physics', 'Public Speaking', 'Statistics', 'Marketing', 'Data Analysis'])
marks = st.slider('Marks (out of 100)', 50, 100, 75)
personality = st.selectbox('Personality', ['Introvert', 'Extrovert', 'Ambivert'])
goals = st.selectbox('Goals', ['Start a business', 'Develop new skills', 'Higher studies', 'Get a good job'])
budget = st.selectbox('Budget', ['Low', 'Medium', 'High'])

st.markdown("--- ")

if st.button('Get Recommendation'):
    # In a real scenario, you would pre-process these inputs
    # (e.g., one-hot encode categorical features) and feed them to your trained model.
    # The current model in the notebook was trained using 'Student_ID' as input, which is
    # not suitable for user-provided features like 'Interests', 'Skills', etc.
    # You would need to train a new model using these input features (e.g., using OneHotEncoder on categorical data).

    # Dummy prediction for demonstration
    # This part should be replaced with actual model inference logic
    possible_careers = ['Software Engineer', 'Doctor', 'Data Analyst', 'Entrepreneur', 'Graphic Designer', 'Marketing Specialist', 'Mechanical Engineer']
    possible_scholarships = ['National Merit Scholarship', 'Need-based Aid', 'STEM Scholarship', 'Arts Talent Scholarship']

    # Simple deterministic dummy logic based on inputs for consistent demo
    seed_val = hash(f"{interests}{strengths}{skills}{marks}{personality}{goals}{budget}") % (2**32 - 1)
    rng = np.random.default_rng(seed_val)

    suggested_career = rng.choice(possible_careers)
    scholarship_option = rng.choice(possible_scholarships)

    st.subheader("Your Recommendations:")
    st.success(f"**Suggested Career:** {suggested_career}")
    st.info(f"**Scholarship Option:** {scholarship_option}")

    st.warning("Note: This application currently provides dummy recommendations.* For accurate results, a machine learning model needs to be trained on relevant student features (Interests, Strengths, Skills, Marks, Personality, Goals, Budget) and integrated here.")

