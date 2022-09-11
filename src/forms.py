from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, IntegerField, SubmitField, SelectField, DateField,
                    FileField, Label, TimeField, MultipleFileField, TextAreaField)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length,NumberRange


class SubmissionForm(FlaskForm):
    age=IntegerField('Age',validators=[DataRequired(),NumberRange(min=2,max=100)])
    bp=IntegerField('Blood Pressure(mm/Hg)',validators=[DataRequired()])
    sg = SelectField('Specific gravity', choices=[(1.005, '1.005'), (1.010, '1.010'),(1.015, '1.015'),(1.020, '1.020')], validators=[DataRequired()])
    al = SelectField('Albumin', choices=[(0, '0'), (1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5')], validators=[DataRequired()])
    su = SelectField('Sugar', choices=[(0, '0'), (1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5')], validators=[DataRequired()])
    rbc = SelectField('Red Blood cells', choices=[('normal', 'Normal'), ('abnormal', 'Abnormal')], validators=[DataRequired()])
    pus = SelectField('Pus cell', choices=[('normal', 'Normal'), ('abnormal', 'Abnormal')], validators=[DataRequired()])
    pcc = SelectField('Pus cell clumps', choices=[('present', 'Present'), ('notpresent', 'NotPresent')], validators=[DataRequired()])
    bc = SelectField('Bacteria', choices=[('present', 'Present'), ('notpresent', 'NotPresent')], validators=[DataRequired()])
    bgr=IntegerField('Blood Glucose random(mgs/dl)',validators=[DataRequired()])
    bu=IntegerField('Blood Urea(mgs/dl)',validators=[DataRequired()])
    sc=IntegerField('Serum Creatinine(mgs/dl)',validators=[DataRequired()])
    sod=IntegerField('Sodium(mEq/L)',validators=[DataRequired()])
    pot=IntegerField('Potassium',validators=[DataRequired()])
    hemo=IntegerField('hemoglobin(gms)',validators=[DataRequired()])
    pc=IntegerField('packed cell volume',validators=[DataRequired()])
    wbc=IntegerField('white blood cell count(cell/cumm)',validators=[DataRequired()])
    rbcs=IntegerField('Red blood cell count(millions/cmm)',validators=[DataRequired()])
    htn = SelectField('Hypertension', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    dm = SelectField('Diabetes Melitius', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    cad = SelectField('coronary arterty disease', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    apt = SelectField('Appetite', choices=[('good', 'Good'), ('poor', 'Poor')], validators=[DataRequired()])
    pe = SelectField('Pedal Edema', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    an = SelectField('Anemia', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    
    



