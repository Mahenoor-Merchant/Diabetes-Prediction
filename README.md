# Diabetes Prediction Model

This is a machine learning model that predicts whether a person has diabetes or not based on several input features. The model uses a dataset containing information such as Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, and Age.

# lab-flask

<!-- ![image](https://user-images.githubusercontent.com/115451707/196919992-edcfea8b-e3f6-4f35-9398-43be66b5622d.png) -->


To run flask application 

```
python app.py
```


To access the flask application open new tab in and paste the url:
```
http://deployment-env.eba-bcqvpk6j.us-east-1.elasticbeanstalk.com
```



## Dataset

The dataset used for training and evaluation consists of records of individuals, with each record containing the following features:

- Pregnancies: Number of times pregnant
- Glucose: Plasma glucose concentration in an oral glucose tolerance test
- Blood Pressure: Diastolic blood pressure (mm Hg)
- Skin Thickness: Triceps skinfold thickness (mm)
- Insulin: 2-Hour serum insulin (mu U/ml)
- BMI: Body mass index (weight in kg/(height in meters)^2)
- Diabetes Pedigree Function: Diabetes pedigree function
- Age: Age (years)

The target variable is:

- Outcome: 1 if the person has diabetes, 0 otherwise

## Model

The model used for prediction is a logistic regression model. Logistic regression is a commonly used algorithm for binary classification tasks. It estimates the probability of an instance belonging to a certain class.

The logistic regression model is trained on the dataset using labeled examples, where the input features are used to predict the diabetes outcome. Once the model is trained, it can be used to make predictions on new, unseen data.

## Usage

To use this model, you need to provide the values for the input features:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

You can use the trained model to predict whether a person is diabetic or not based on these input values.

## Contributing

Contributions to this project are welcome. If you have suggestions for improvements or find any issues, feel free to create a pull request or submit an issue.
