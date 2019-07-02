""""
Test
"""
import sys
from lenders import Lenders
from loan import Loan


def main(lenders_info, amount):
    """
    Takes in data from user and feeds classes. Captures errors and prints to user
    :param lenders_info: csv file from user
    :param amount: amount to borrow input from user
    :return: Prints Request Amount, Rate, Total & Monthly Repayments to screen
    """
    try:
        lenders = Lenders(lenders_info)
        selected_lenders = lenders.get_lenders(amount)
        loan_offer = Loan(selected_lenders, amount)
        loan_offer.input_validation()
        loan_offer.calc_offer()
        loan_offer.print_output()
    except IOError:
        print("No market data found for file specified")
    except Exception as error:
        print(error)
    else:
        return loan_offer


if __name__ == '__main__':
    A = 'market.csv'  # sys.argv[1]
    B = 1000  # int(sys.argv[2])
    main(A, B)
