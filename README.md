# Mildew Detector

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
  - [Business Requirement 1: Data Visualization](#business-requirement-1-data-visualization)
  - [Business Requirement 2: Classification](#business-requirement-2-classification)
- [ML Business Case](#ml-business-case)
- [ML Model Development](#ml-model-development)
- [Dashboard Design](#dashboard-design)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Automated Unit Tests](#automated-unit-tests)
  - [Validation](#validation)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

---

## Project Overview
This project focuses on developing an **AI-powered system** to detect **Powdery Mildew** on cherry leaves. By using **image processing and machine learning**, the system can identify early signs of infection, allowing farmers to take timely action. The model is trained on a dataset of **healthy and infected leaves** and leverages **computer vision techniques** to classify mildew presence. The primary objectives are to:

- Enhance **agricultural efficiency**.
- Reduce **pesticide use**.
- Improve **crop health** with an **automated detection method**.

## Dataset Content
The dataset used is the **Cherry Leaves** dataset from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves), containing labeled images of **healthy and mildew-infected cherry leaves**.

## Business Requirements
### Business Requirement 1: Data Visualization
- Users should be able to **navigate** through an **interactive dashboard** to explore the dataset.
- The system should provide **visual differentiations** using:
  - **Average images**
  - **Image differences**
  - **Variabilities** between healthy and infected leaves
- Users should be able to generate an **image montage** for better visual comparison.

### Business Requirement 2: Classification
- Users can **upload images** to the dashboard for **real-time mildew detection**.
- Predictions should be **stored and saved**, allowing for record-keeping.

## ML Business Case
- A **binary classification model** is developed to classify cherry leaves as **healthy or infected**.
- A **TensorFlow-based Convolutional Neural Network (CNN)** is used to extract meaningful image features.
- The model output is a **classification label** (Healthy or Powdery Mildew) with an associated probability score.
- Performance is measured using **F1-score** and **recall**, ensuring accurate mildew detection.

## ML Model Development
- The **CNN model** consists of **four convolutional layers**:
  - 64, 128, 256, and 256 filters
  - Each layer includes **batch normalization** and **max pooling**
- Features are passed through **two fully connected layers** (512 and 256 neurons) with **dropout layers** (0.4 and 0.3) to prevent overfitting.
- The final output layer uses **sigmoid activation** for binary classification.
- The model is compiled with:
  - **Binary cross-entropy loss**
  - **Adam optimizer (learning rate: 0.0001)**
  - **Accuracy** as the evaluation metric
- **Early stopping** and **learning rate reduction** are used for optimization.

## Dashboard Design
The **Streamlit web application** includes five pages:

1. **Quick Project Summary** - Overview of the project.
2. **Leaf Visualizer** - Data analysis with **image averages, differences, and variability comparisons**.
3. **Model Performance** - Dataset distribution, training progress, and model evaluation.
4. **Mildew Detector** - Users can **upload leaf images** for real-time classification.
5. **Project Hypothesis** - Written documentation of key hypotheses.

## Unfixed Bugs
- **No known unfixed bugs**.

## Deployment
### Deploying on Render
The application is deployed on **Render** following these steps:

1. Log in to **Render** and **create a new app**.
2. Connect the app to **GitHub**.
3. Enter the start command: `streamlit run app.py`.
4. Click **Deploy**.

The live application is available here: [Mildew Detector](https://mildew-detector-54t8.onrender.com)

## Testing
### Manual Testing
- Users can **navigate the interactive dashboard** with ease.
- **Leaf Visualizer Page**:
  - Displays **graphs of average images, image differences, and variability**.
  - Generates **image montages** for easy visual differentiation.
- **Mildew Detector Page**:
  - Allows **image uploads** for mildew detection.
  - Saves **model predictions** in a timestamped CSV file.

### Automated Unit Tests
- **No automated tests** have been implemented yet but are planned for future development.

### Validation
- **Python code** was validated using [PEP8 standards](https://pep8ci.herokuapp.com/).

## Credits
- This project was inspired by **CI's Malaria Detection walkthrough**, which guided CNN implementation and Streamlit deployment.

## Acknowledgements
- Special thanks to my mentor, **Mo Shami**, for valuable insights and guidance throughout the project.