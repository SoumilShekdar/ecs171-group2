from flask import Flask
from flask import render_template
from flask import request
from tensorflow.keras.models import load_model
from joblib import dump, load
import tensorflow as tf
import numpy as np
from wtforms import (Form, TextField, validators, SelectField, SubmitField, BooleanField, IntegerField)
app = Flask(__name__)


class ReusableForm(Form):
    # sex
    sex = SelectField('Choose Sex', choices=['Male', 'Female'])
    # age
    age = IntegerField('Enter age:',
                         default=18, validators=[validators.InputRequired()])
    # patient_type
    patient_type = SelectField('Inpatient or Outpatient?', choices=['Inpatient', 'Outpatient'])
    # intubed
    intubed = SelectField('Received intubation?', choices=['Yes', 'No'])
    # pneumonia
    pneumonia = SelectField('Pneumonia?', choices=['Yes', 'No'])
    # pregnancy
    pregnancy = SelectField('Pregnant?', choices=['Yes', 'No'])
    # diabetes
    diabetes = SelectField('Diabetes?', choices=['Yes', 'No'])
    # copd
    copd = SelectField('COPD?', choices=['Yes', 'No'])
    # asthma
    asthma = SelectField('Asthma?', choices=['Yes', 'No'])
    # inmsupr
    inmsupr = SelectField('Immunosuppression?', choices=['Yes', 'No'])
    # hypertension
    hypertension = SelectField('Hypertension?', choices=['Yes', 'No'])
    # other_disease
    other_disease = SelectField('Other diseases not listed?', choices=['Yes', 'No'])
    # cardiovascular
    cardiovascular = SelectField('Cardiovascular issues?', choices=['Yes', 'No'])
    # obesity
    obesity = SelectField('Obesity?', choices=['Yes', 'No'])
    # renal_chronic
    renal_chronic = SelectField('Renal (kidney) chronic disease?', choices=['Yes', 'No'])
    # tobacco
    tobacco = SelectField('Tobacco use?', choices=['Yes', 'No'])
    # days_to_medical_help
    days_to_med = IntegerField('Enter days to receive medical help:',
                         default=0, validators=[validators.InputRequired()])

    # Submit button
    submit = SubmitField("Get Results")  # POST request

    # Messages appear in 'message' in html file when an error occurs

def convert_to_id(form):
    if form == 'Yes':
        return 1
    elif form == 'No':
        return 0

# Home page
@app.route("/", methods=['GET', 'POST'])
def home():
    """Home page of app with form"""
    # Create form
    form = ReusableForm(request.form)
    icu_model = load_model('icu.h5')
    lethal_model = load_model('lethal.h5')

    age_scaler = load('age_scaler.joblib')
    days_to_medical_help_scaler = load("days_to_medical_help_scaler.joblib")

    # print(model.predict(1,1,1,1))
    # Send template information to index.html

    lethal_prob = 0
    icu_prob = 0

    if request.method == 'POST' and form.validate():  # Validate if no errors occur
        data_to_predict = []
        sex = request.form['sex']
        sex_id = 0
        if sex == 'Female':
            sex_id = 1
        elif sex == 'Male':
            sex_id = 0
        data_to_predict.append(sex_id)
        patient_type = request.form['patient_type']
        patient_type_id = 0
        if patient_type == 'Outpatient':
            patient_type_id = 1
        elif patient_type == 'Inpatient':
            patient_type_id = 0
        data_to_predict.append(patient_type_id)
        data_to_predict.append(convert_to_id(request.form['intubed']))
        data_to_predict.append(convert_to_id(request.form['pneumonia']))
        data_to_predict.append(age_scaler.transform(np.array(int(request.form['age'])).reshape(1, -1))[0])
        data_to_predict.append(convert_to_id(request.form['pregnancy']))
        data_to_predict.append(convert_to_id(request.form['diabetes']))
        data_to_predict.append(convert_to_id(request.form['copd']))
        data_to_predict.append(convert_to_id(request.form['asthma']))
        data_to_predict.append(convert_to_id(request.form['inmsupr']))
        data_to_predict.append(convert_to_id(request.form['hypertension']))
        data_to_predict.append(convert_to_id(request.form['other_disease']))
        data_to_predict.append(convert_to_id(request.form['cardiovascular']))
        data_to_predict.append(convert_to_id(request.form['obesity']))
        data_to_predict.append(convert_to_id(request.form['renal_chronic']))
        data_to_predict.append(convert_to_id(request.form['tobacco']))
        data_to_predict.append(days_to_medical_help_scaler.transform(np.array(int(request.form['days_to_med'])).reshape(1, -1))[0])
        print(data_to_predict)
        print("ICU Prediction:")
        predictions_icu = icu_model.predict(np.array([data_to_predict,]).astype('float32'))
        icu_prob = predictions_icu[0][0]
        #print(predictions)
        print(predictions_icu[0][0]) # probability of icu?
        print("Lethal Predictions Prediction:")
        predictions_lethal = lethal_model.predict(np.array([data_to_predict,]).astype('float32'))
        lethal_prob = predictions_lethal[0][0]
        #print(predictions)
        print(predictions_lethal[0][0]) # probability of icu?
        #output = predictions_icu[0][0]
        
        
    return render_template('index.html', form=form, prediction_icu=icu_prob, prediction_lethal=lethal_prob)


app.run(host='0.0.0.0', port=50000, debug=False)
