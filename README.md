# Mildew Detector

This project focuses on developing an AI-powered system to detect mildew on cherry leaves. Using image processing and machine learning, the system identifies early signs of infection, allowing farmers to take timely action. The detector is trained on a dataset of healthy and infected leaves, leveraging computer vision techniques to classify and analyze mildew presence. The goal is to enhance agricultural efficiency, reduce pesticide use, and improve crop health through an accessible, automated detection method.

## Dataset Content
The dataset is **Cherry leaves** dataset from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)

## Business Requirements
The primary objective of this project is to develop a machine learning model for the  detection of Powdery Mildew in cherry leaves. The model should assist fermers in making quicker and more accurate diagnoses.

Requirements:

- The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
- The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. understand the relevant discoveries.
- The Streamlit Dashboard will be developed that will finally serve as a platform for the presentation of the results of first two business objectives, together with the interactive implementation of the prediction of the unseen MRI image.

**Business Requirement 1: Data Visualization**
- As a client, I can navigate easily through an interactive dashboard so that I can view and understand the data.
- As a client, I can view average images,image differences and variabilities between a healthy cherry leaf and the one with powdery mildew, so that I can identify which is which more easily.
- As a client, I can view an image montage of healthy cherry leaves and the one with Powdery Mildew, so I can make the visual differentiation.

**Business Requirement 2: Classification**
- As a client, I can upload images of the cherry leaves to the dashboard so that I can run the ML model and an immediate accurate prediction of the posible Powdery Mildew.
- As a client, I can save model predictions so that I can have a documented history of the made predictions.

## ML Business Case

- The client is focused on accurately predicting from a given cherry leaf image whether Powdery Mildew is present. This business objective will be achieved through the development and deployment of a TensorFlow deep learning pipeline, trained on a dataset of cherry leaves classified as either having Powdery mildew or not.
- This TensorFlow pipeline will employ a convolutional neural network (CNN), a type of neural network particularly effective at identifying patterns and key features in image data, utilizing convolution and pooling layer pairs.
- The ultimate goal of this machine learning pipeline is a binary classification model. The desired outcome is a model capable of successfully distinguishing cherry leaves as either having a Powdery mildew or not.
- The model's output will be a classification label indicating the presence or absence of Powdery Mildew, based on the probability calculated by the model.
- The primary metrics for evaluating the success of this machine learning model will be overall model accuracy (measured by the F1 score) and recall for correctly identifying Powdery Mildew.

## ML Model Development

This CNN model is designed for binary classification of images, likely distinguishing between healthy and mildew-infected cherry leaves. It consists of four convolutional blocks with increasing filter sizes (64, 128, 256, 256) to extract hierarchical features, each followed by batch normalization and max pooling for stability and downsampling. The extracted features are flattened and passed through two fully connected layers (512 and 256 neurons) with dropout (0.4 and 0.3) to prevent overfitting. The final output layer uses a sigmoid activation for binary classification. The model is compiled with binary cross-entropy loss, an Adam optimizer (learning rate 0.0001), and accuracy as the metric. Training is optimized with early stopping and learning rate reduction to improve generalization.

## Dashboard Design

- This project is presented through a Streamlit dashboard web application that consists of five app pages. The client can effortlessly navigate through these pages using the interactive menu located on the left side of the page.
- **Quick Project Summary** - The homepage of the project provides a fundamental overview of the business process that motivates the creation of this project.

- **Leaf Visualizer** - The first business objective of the project is addressed by the Leaf Visualizer page, which focuses on Data Analysis. This page includes plots that can be toggled on and off using the built-in toolbar.

* Additionally, this app page offers a tool for creating image montages. Users can select a label class (tumor or non-tumor) and view a montage generated through graphical presentation of random validation set images.

- **Model Performance** - The dataset size and label frequencies, which indicate the initial imbalance of the target, are documented on this page. Additionally, the history and evaluation of the project's machine learning model are provided. The paired graphs display the validation loss and accuracy per epoch, showcasing the model's progress over time.

- **Mildew Detector** - tool fulfills the second ML business objective of the project. It provides access to the original raw dataset, allowing users to download cherry leaves images. These images can then be uploaded to receive a class prediction output generated by the model.

- **Project Hypothesis**
This application page showcases written documentation of the project's hypotheses 

## Unfixed Bugs
* There are no unfixed bugs.

## Deployment
### Render

* The App live link is: [https://mildew-detector-54t8.onrender.com](https://mildew-detector-54t8.onrender.com)
* The project was deployed to Render using the following steps.

1. Log in to Render and create an App
2. Connect you app to Git Hub
3. Introduce the running commmand "streamlit run app.py"
5. click on deploy

## TESTING
### Manual Testing

 As a client, I can navigate easily through an interactive dashboard so that I can view and understand the data.

**MRI Visualizer Page**
- As a client, I can view visual graphs of average images,image differences and variabilities between images of a healthy leaves and the ones with Powdery Mildew, so that I can identify which is which more easily.

- As a client, I can view an image montage of the images of the healthy leaves and the one with Powdery Mildew, so I can make the visual differentiation.

**Brain Tumor Detection Page**
-  As a client, I can upload image(s) of the cherry leaves to the dashboard so that I can run the ML model and an immediate accurate prediction of the posible Powdery Mildew.

- As a client, I can save model predictions in a timestamped CSV file so that I can have a documented history of the made predictions.

### Automated Unit Tests
- There were no automated unit testing. It is planned for the future development.

### Validation
- Python Code was validated as conforming to PEP8 standards using: [https://pep8ci.herokuapp.com/]

## Credits 

* Through the whole project I was following particularly the CI's Malaria Detection walkthrough and example.


## Acknowledgements
* To my mentor, Mo Shami, for his invaluable suggestions and guidance throughout this project. His expertise and insights have been instrumental in shaping the direction and success of this project.