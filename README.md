# Overview

The goal of this assignment is to assess your understanding of how to perform automated black-box testing.

The web app in this repository is a **mortgage calculator**. It asks for the following information about a loan:

| Field | Id | Description |
|---|---|---|
| Home Price ($) | `price` | purchase price of the home |
| Down Payment ($) | `down_payment` | amount paid up front; must be at least zero and less than the home price |
| Annual Interest Rate (%) | `rate` | e.g., `6.5` for 6.5%; cannot be negative |
| Loan Term (years) | `years` | e.g., `15` or `30` |

When the form is submitted with valid information, the app displays the estimated monthly payment (principal and interest) in an element with id `payment`, formatted like `$1,516.96`. If the information is invalid, an error message is displayed in an element with id `error`.

The monthly payment is computed with the standard amortization formula:

$$M = P \cdot \frac{r(1+r)^n}{(1+r)^n - 1}$$

where $P$ is the loan amount (home price minus down payment), $r$ is the **monthly** interest rate (annual rate / 100 / 12), and $n$ is the number of monthly payments (years × 12). When the interest rate is zero, $M = P / n$.

# Running the App

```
pip install -r requirements.txt
flask --app src/app run
```

Run these commands from the root of the repository (the app looks for `templates/` and `static/` in the current directory). Leave the app running at http://127.0.0.1:5000 while you run the tests.

# Instructions

Treat the app as a black box: your tests must interact with it **only through the browser** (using Selenium), never by importing or calling the app's code.

The first test case (`testThirtyYearLoan`) is already implemented for you as an example. Finish the remaining five test cases in [tests/MortgageTest.py](tests/MortgageTest.py) according to the pre- and post-conditions. Each test should:

1. fill in the form fields with the values given in the pre-condition;
2. click the `submit` button;
3. assert that the page displays exactly what the post-condition says.

Run your tests with:

```
python tests/MortgageTest.py
```

# Rubric 

+1 point for each test completed successfully.
