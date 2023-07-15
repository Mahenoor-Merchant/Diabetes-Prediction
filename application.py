from flask import Flask, request, app, render_template
from flask_cors import cross_origin
import pickle
import numpy as np
import pandas as pd

application = Flask(__name__)

scaler = pickle.load(open('Model/standardScalar.pkl','rb'))
model = pickle.load(open('Model/modelforprediction.pkl','rb'))

@cross_origin
@application.route("/")
def index():
    return render_template('index.html')

## Route for single data prediction
@cross_origin
@application.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    result=''

    if request.method=='POST':

        Pregnancies = int(request.form.get('Pregnancies'))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        new_data = scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        model=pickle.load(open('/config/workspace/Diabetes-Deployment/Model/modelforprediction.pkl','rb'))
        predict=model.predict(new_data)


        if predict[0] ==1:
            result = 'Diabetic'
        else:
            result = 'Non Diabetic'

        return render_template('single_prediction.html',result = result)

    else : 
        return render_template('home.html')

if __name__=="__main__":
    application.run(host="0.0.0.0",port=5000)
