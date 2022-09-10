from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, IntegerField, SubmitField, SelectField, DateField,
                     FileField, Label, TimeField, MultipleFileField, TextAreaField)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, NumberRange


class SubmissionForm(FlaskForm):
    age = IntegerField(
        'Age', validators=[
            DataRequired(), NumberRange(
                min=2, max=100)])
    bp = IntegerField('Blood pressure', validators=[DataRequired()])
    sg = IntegerField('Specific gravity', validators=[DataRequired()])
    al = SelectField(
        'Albumin', choices=[
            (0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], validators=[
            DataRequired()])
    su = SelectField(
        'Sugar', choices=[
            (0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], validators=[
            DataRequired()])
    rbc = SelectField(
        'Red Blood cell', choices=[
            ('normal', 'Normal'), ('abnormal', 'Abnormal')], validators=[
            DataRequired()])
    pus = SelectField(
        'pus cell', choices=[
            ('normal', 'Normal'), ('abnormal', 'Abnormal')], validators=[
            DataRequired()])
    bc = SelectField(
        'Bacteria', choices=[
            ('present', 'Present'), ('notpresent', 'NotPresent')], validators=[
            DataRequired()])
    bgr = IntegerField('blood glucose random', validators=[DataRequired()])
    bu = IntegerField('blood urea', validators=[DataRequired()])
    sc = IntegerField('Serum creatnine', validators=[DataRequired()])
    sod = IntegerField('Sodium', validators=[DataRequired()])
    pot = IntegerField('Potassium', validators=[DataRequired()])
    hemo = IntegerField('hemoglobin', validators=[DataRequired()])
    pc = IntegerField('packed cell volume', validators=[DataRequired()])
    wbc = IntegerField('white blood cell', validators=[DataRequired()])
    rbcs = IntegerField('Red blood cell count', validators=[DataRequired()])
    htn = SelectField(
        'Red Blood cell count', choices=[
            ('yes', 'Yes'), ('no', 'No')], validators=[
            DataRequired()])
    dm = SelectField(
        'Diabetes Melitius', choices=[
            ('yes', 'Yes'), ('no', 'No')], validators=[
            DataRequired()])
    cad = SelectField(
        'coronary arterty disease', choices=[
            ('yes', 'Yes'), ('no', 'No')], validators=[
            DataRequired()])
    apt = SelectField(
        'Appetite', choices=[
            ('good', 'Good'), ('poor', 'Poor')], validators=[
            DataRequired()])
    pe = SelectField(
        'Pedal Edema', choices=[
            ('yes', 'Yes'), ('no', 'No')], validators=[
            DataRequired()])
    an = SelectField(
        'Anemia', choices=[
            ('yes', 'Yes'), ('no', 'No')], validators=[
            DataRequired()])
