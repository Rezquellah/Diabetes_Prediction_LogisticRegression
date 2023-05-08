from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('lr_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    glucose = float(request.form['glucose'])
    blood_pressure = float(request.form['blood_pressure'])
    bmi = float(request.form['bmi'])
    age = int(request.form['age'])
    insulin = int(request.form['insulin'])
    data = np.array([[glucose, blood_pressure, bmi, age, insulin]])
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)[0]
    probability = model.predict_proba(data_scaled)[0][1] * 100
    if prediction == 0:
        return render_template('result.html', prediction='You do not have diabetes.', probability=f'Probability of having diabetes: {probability:.2f}%')
    else:
        return render_template('result.html', prediction='You have diabetes.', probability=f'Probability of having diabetes: {probability:.2f}%')

if __name__ == '__main__':
    app.run(debug=True)
