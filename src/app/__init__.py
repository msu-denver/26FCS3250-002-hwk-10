'''
CS3250 - Software Development Methods and Tools - Fall 2026
Instructor: Thyago Mota
Student: 
Description: Homework 10 - Blackbox Testing
'''

from flask import Flask

app = Flask("Mortgage Calculator Web App")
#app.secret_key = os.environ['SECRET_KEY']
app.secret_key = 'you will never guess'

from app import routes