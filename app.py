from flask import Flask, render_template, request
import joblib
# Import your heart disease prediction model here (e.g., a trained scikit-learn model)
loaded_model = joblib.load('heart_disease_model.joblib')
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the user inputs from the form
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    cp = int(request.form['cp'])
    trestbps = int(request.form['trestbps'])
    chol = int(request.form['chol'])
    fbs = int(request.form['fbs'])
    restecg = int(request.form['restecg'])
    thalach = int(request.form['thalach'])
    exang = int(request.form['exang'])
    oldpeak = int(request.form['oldpeak'])
    slope = int(request.form['slope'])
    ca = int(request.form['ca'])
    thal = int(request.form['thal'])
    # Add code to get other inputs

    # Perform the prediction using your machine learning model
    # Replace 'your_model' with the variable name of your loaded model
    prediction = loaded_model.predict([[age,sex,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

    # Process the prediction and display the result on the web page
    result = "Heart Disease: " + ("Present" if prediction[0] == 1 else "Absent")

    return render_template('index1.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)
