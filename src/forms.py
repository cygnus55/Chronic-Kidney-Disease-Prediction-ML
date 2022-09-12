from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, IntegerField, SubmitField, SelectField, FloatField,)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, NumberRange


class SubmissionForm(FlaskForm):

    age=IntegerField('Age',validators=[DataRequired(),NumberRange(min=2,max=100)])
    bp=FloatField('Blood Pressure(mm/Hg)',validators=[DataRequired()])
    sg = SelectField('Specific gravity', choices=[(1.005, '1.005'), (1.010, '1.010'),(1.015, '1.015'),(1.020, '1.020')], validators=[DataRequired()])
    al = SelectField('Albumin', choices=[(0, '0'), (1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5')], validators=[DataRequired()])
    su = SelectField('Sugar', choices=[(0, '0'), (1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5')], validators=[DataRequired()])
    rbc = SelectField('Red Blood cells', choices=[(1, 'Normal'), (0, 'Abnormal')], validators=[DataRequired()])
    pus = SelectField('Pus cell', choices=[(1, 'Normal'), (0, 'Abnormal')], validators=[DataRequired()])
    pcc = SelectField('Pus cell clumps', choices=[(1, 'Present'), (0, 'NotPresent')], validators=[DataRequired()])
    bc = SelectField('Bacteria', choices=[(1, 'Present'), (0, 'NotPresent')], validators=[DataRequired()])
    bgr=FloatField('Blood Glucose random(mgs/dl)',validators=[DataRequired()])
    bu=FloatField('Blood Urea(mgs/dl)',validators=[DataRequired()])
    sc=FloatField('Serum Creatinine(mgs/dl)',validators=[DataRequired()])
    sod=FloatField('Sodium(mEq/L)',validators=[DataRequired()])
    pot=FloatField('Potassium',validators=[DataRequired()])
    hemo=FloatField('hemoglobin(gms)',validators=[DataRequired()])
    pc=FloatField('packed cell volume',validators=[DataRequired()])
    wbc=FloatField('white blood cell count(cell/cumm)',validators=[DataRequired()])
    rbcs=FloatField('Red blood cell count(millions/cmm)',validators=[DataRequired()])
    htn = SelectField('Hypertension', choices=[(1, 'Yes'), (0, 'No')], validators=[DataRequired()])
    dm = SelectField('Diabetes Melitius', choices=[(1, 'Yes'), (0, 'No')], validators=[DataRequired()])
    cad = SelectField('coronary arterty disease', choices=[(1, 'Yes'), (0, 'No')], validators=[DataRequired()])
    apt = SelectField('Appetite', choices=[(0, 'Good'), (1, 'Poor')], validators=[DataRequired()])
    pe = SelectField('Pedal Edema', choices=[(1, 'Yes'), (1, 'No')], validators=[DataRequired()])
    an = SelectField('Anemia', choices=[(1, 'Yes'), (1, 'No')], validators=[DataRequired()])
    
    



