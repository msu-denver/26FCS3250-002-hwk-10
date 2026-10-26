'''
CS3250 - Software Development Methods and Tools - Fall 2026
Instructor: Thyago Mota
Student:
Description: Homework 10 - Blackbox Testing
'''

from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, IntegerField
from wtforms.validators import InputRequired

class LoanForm(FlaskForm):
    price = FloatField('Home Price ($)', validators=[InputRequired()])
    down_payment = FloatField('Down Payment ($)', validators=[InputRequired()])
    rate = FloatField('Annual Interest Rate (%)', validators=[InputRequired()])
    years = IntegerField('Loan Term (years)', validators=[InputRequired()])
    submit = SubmitField('Calculate')
