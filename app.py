import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_leaf_visualizer import page_leaf_visualizer_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics

app = MultiPage(app_name="Mildew Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Leaf Visualiser", page_leaf_visualizer_body)
app.add_page("Mildew Detection", page_mildew_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

app.run()  # Run the app