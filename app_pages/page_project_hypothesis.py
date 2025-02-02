import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
    f"* We suspect that powdery mildew-infected leaves have a distinct white powder. "
    f"Typically, these leaves also show signs of damage, which can help differentiate them from healthy leaves.\n\n"
    f"* An image montage suggests that powdery mildew-infected leaves exhibit white powder. "
    f"However, studies using Average Image, Variability Image, and Difference Between Averages "
    f"did not reveal a clear pattern for differentiation.\n\n"
    f"* Furthermore, environmental factors such as humidity and temperature might influence the severity "
    f"of powdery mildew, potentially affecting the visual characteristics of infected leaves."
)

    st.write("#### Validate the Hypothesis")
    hypothesis_confirmed = st.radio(
        "Does this observation match your experience with powdery mildew?",
        ("Yes", "No")
    )

    if hypothesis_confirmed == "Yes":
        st.success("Great! Your observation supports the hypothesis.")
    else:
        st.warning("This might need further investigation or a re-evaluation of the hypothesis.")