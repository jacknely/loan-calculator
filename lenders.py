import pandas as pd


class Lenders:

    def __init__(self, lenders_info):
        self.lenders = pd.read_csv(lenders_info)

    def get_lenders(self, amount):
        """
        Gets a pandas dataframe of lenders with lowest interest rate to make up loan amount
        :param amount: input from user
        :return: filtered list of lenders
        """
        loan = pd.DataFrame(columns=['Lender', 'Rate', 'Available', 'monthly'])
        lenders = self.lenders.sort_values(by='Rate', ascending=True)
        i = 0
        if amount < lenders['Available'].sum():
            while amount > loan['Available'].sum():
                loan = loan.append(lenders.iloc[i])
                i = i + 1
            return loan
