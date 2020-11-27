from flask import Flask
from flask import render_template
from flask import request
from keras.models import load_model
import tensorflow as tf
import numpy as np
from wtforms import (Form, TextField, validators, SelectField, SubmitField, BooleanField, IntegerField)
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "<h1>Not Much Going On Here</h1>"

class ReusableForm(Form):
    """User entry form for entering specifics for generation"""
    # Starting seed
    # seed = TextField("Enter a seed string or 'random':", validators=[
    #                  validators.InputRequired()])
    # # Diversity of predictions
    # diversity = DecimalField('Enter diversity:', default=0.8,
    #                          validators=[validators.InputRequired(),
    #                                      validators.NumberRange(min=0.5, max=5.0,
    #                                      message='Diversity must be between 0.5 and 5.')])

    # sex
    sex = SelectField('Choose Sex', choices=['Male', 'Female'])
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
        return 2
    elif form == 'No':
        return 1

# Home page
@app.route("/", methods=['GET', 'POST'])
def home():
    """Home page of app with form"""
    # Create form
    form = ReusableForm(request.form)
    model = load_model('best.h5')
    # print(model.predict(1,1,1,1))
    # Send template information to index.html
    if request.method == 'POST' and form.validate():  # Validate if no errors occur
        data_to_predict = []
        sex = request.form['sex']
        sex_id = 0
        if sex == 'Female':
            sex_id = 1
        elif sex == 'Male':
            sex_id = 2
        data_to_predict.append(sex_id)
        patient_type = request.form['patient_type']
        patient_type_id = 0
        if patient_type == 'Outpatient':
            patient_type_id = 1
        elif patient_type == 'Inpatient':
            patient_type_id = 2
        data_to_predict.append(patient_type_id)
        data_to_predict.append(int(request.form['days_to_med']))
        data_to_predict.append(convert_to_id(request.form['intubed']))
        data_to_predict.append(convert_to_id(request.form['pneumonia']))
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
        print(data_to_predict)
        predictions = model.predict(np.array([data_to_predict,]))
        print(predictions)
        print(predictions[0][0]) # probability of death?
        output = predictions[0][0]
        



    return render_template('index.html', form=form, output=output)


app.run(host='0.0.0.0', port=50000, debug=False)