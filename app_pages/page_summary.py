import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a parasitic infection of cherry leaves "
        f"* A cherry leaf image is collected and examinated."
        f"Visual criteria are used to detect powdery mildew.\n"
        f"* According to [SienceDirect](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/powdery-mildew), "
        f"in 2020, there were an estimated  400 million cases of powdery mildew worldwide and"
        f"estimated 409 thousand tons of cherry production was lost due to this disease. "
        f"**Project Dataset**\n"
        f"* The available dataset contains images taken from different Farmers")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Cosmin2002Trusca/mildew-detector).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"a parasitized and uninfected cherry leaf visually.\n"
        f"* 2 - The client is interested in telling whether a given leaf contains a powdery mildew or not. "
        )