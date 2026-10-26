'''
CS3250 - Software Development Methods and Tools - Fall 2026
Instructor: Thyago Mota
Student:
Description: Homework 10 - Blackbox Testing
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class MortgageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.get('http://127.0.0.1:5000')

    def tearDown(self) -> None:
        self.browser.quit()

    # pre-condition: price=300000, down_payment=60000, rate=6.5, years=30
    # post-condition: monthly payment is displayed as $1,516.96
    def testThirtyYearLoan(self):
        # TODO: fill in the form with the pre-condition values, click submit, and assert the post-condition
        raise ValueError()

    # pre-condition: price=300000, down_payment=60000, rate=6.5, years=15
    # post-condition: monthly payment is displayed as $2,090.66
    def testFifteenYearLoan(self):
        # TODO: fill in the form with the pre-condition values, click submit, and assert the post-condition
        raise ValueError()

    # pre-condition: price=450000, down_payment=90000, rate=7.25, years=30
    # post-condition: monthly payment is displayed as $2,455.83
    def testFractionalInterestRate(self):
        # TODO: fill in the form with the pre-condition values, click submit, and assert the post-condition
        raise ValueError()

    # pre-condition: price=120000, down_payment=0, rate=0, years=10
    # post-condition: monthly payment is displayed as $1,000.00
    def testZeroInterestRate(self):
        # TODO: fill in the form with the pre-condition values, click submit, and assert the post-condition
        raise ValueError()

    # pre-condition: price=300000, down_payment=300000, rate=6.5, years=30
    # post-condition: message "Down payment must be at least zero and less than the home price" is displayed
    def testDownPaymentEqualsPrice(self):
        # TODO: fill in the form with the pre-condition values, click submit, and assert the post-condition
        raise ValueError()

    # pre-condition: price=300000, down_payment=60000, rate=-1, years=30
    # post-condition: message "Interest rate cannot be negative" is displayed
    def testNegativeInterestRate(self):
        # TODO: fill in the form with the pre-condition values, click submit, and assert the post-condition
        raise ValueError()

if __name__ == '__main__':
    unittest.main()
