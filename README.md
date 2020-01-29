# Loan Calculator

A rate calculation system allowing prospective borrowers to obtain a quote from our pool of lenders for 36 month loans. This system will
take the form of a command-line application.

Specify a file containing a list of all the offers being made by the lenders within the system in CSV format. The application will then 
provide as low a rate to the borrower as is possible. The application will then print infomation for borrower with the details of the
monthly repayment amount and the total repayment amount. Borrowers are able to request a loan of any £100 increment between £1000 and £15000 inclusive. If the market does not have sufficient offers from lenders to satisfy the loan then the system should inform the borrower that it is not possible to provide a quote at that time.

## Requirements

- Python 3.7
- Pytest
- Pandas

Install from requirements.txt

## Usage

Running the web app.

The application should take arguments in the form:
```
cmd> [application] [market_file] [loan_amount]
```

Example:
```
cmd> app.py market.csv 1500
```

The application should produce output in the form:
```
Requested amount: £XXXX

Rate: X.X%

Monthly repayment: £XXXX.XX

Total repayment: £XXXX.XX
