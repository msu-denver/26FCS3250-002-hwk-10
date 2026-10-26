'''
CS3250 - Software Development Methods and Tools - Fall 2026
Instructor: Thyago Mota
Student:
Description: Homework 10 - Blackbox Testing
'''

from app import app
from app.forms import LoanForm
from flask import render_template

def monthly_payment(principal: float, annual_rate: float, years: int) -> float:
    n = years * 12
    if annual_rate == 0:
        return principal / n
    r = annual_rate / 100 / 12
    return principal * r * (1 + r) ** n / ((1 + r) ** n - 1)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    form = LoanForm()
    if form.validate_on_submit():
        price = form.price.data
        down_payment = form.down_payment.data
        rate = form.rate.data
        years = form.years.data
        if price <= 0:
            error = 'Home price must be greater than zero'
        elif down_payment < 0 or down_payment >= price:
            error = 'Down payment must be at least zero and less than the home price'
        elif rate < 0:
            error = 'Interest rate cannot be negative'
        elif years <= 0:
            error = 'Loan term must be at least one year'
        else:
            principal = price - down_payment
            payment = monthly_payment(principal, rate, years)
            return render_template('result.html', principal=f'${principal:,.2f}', payment=f'${payment:,.2f}')
        return render_template('index.html', form=form, error=error)
    return render_template('index.html', form=form)
