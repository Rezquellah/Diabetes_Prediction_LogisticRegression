# Diabetes Prediction wiith Logistic Regression

### Dataset link:https: //www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset?datasetId=3102947

This is a Flask app that predicts the likelihood of a person having diabetes based on their glucose level, blood pressure, BMI, age, and hypertension status. The app uses a logistic regression model to make the prediction.

-------------
Please consult the link below to check the different steps that i followed in order to create a logistic regression classifier that is 96% accurate 
[Model creation](https://github.com/Rezquellah/Diabetes_Prediction_LogisticRegression/blob/main/Diabetes_Prediction.ipynb)
-----------
# Getting Started

To run the app, first clone the repository to your local machine:

    git clone https://github.com/your_username/diabetes-prediction-flask-app.git

Then navigate to the app directory and install the [required](https://github.com/Rezquellah/Diabetes_Prediction_LogisticRegression/blob/main/requirements.txt) packages:

    cd diabetes-prediction-flask-app
    pip install -r requirements.txt
    
Finally, run the app with the following command:

    python app.py

The app will then be available at http://localhost:5000/ in your web browser.

------------

# Usage

To use the app, fill out the form on the home page with your glucose level, blood pressure, BMI, age, and hypertension status, and click the "Predict" button. The app will then display whether or not you are likely to have diabetes, along with the probability of the prediction.

----
# Model
The logistic regression model used in this app was trained on the [Diabetes prediction dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset?datasetId=3102947) from Kaggle.

The Logistic Regression model was trained using scikit-learn and achieved an accuracy of 96% on the test set.
-----
# Web app snipet

### Home page 
![image](https://user-images.githubusercontent.com/51273123/236902843-e36d4bfb-1ef6-4481-8c2a-78b56ecaf4d3.png)

### Result page 
![image](https://user-images.githubusercontent.com/51273123/236903073-e64ee5e0-d06b-4993-b154-6438a11c564b.png)
------
# Contact
If you have any questions or comments about this app, feel free to contact me :
Mohamed Rezquellah<br>
Contact: momed.rezquellah@gmail.com<br>
LinkedIn: [https://www.linkedin.com/in/rezquellah/](https://www.linkedin.com/in/rezquellah/)



