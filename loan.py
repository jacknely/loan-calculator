"""
Contains Loan class and associated variables, properties and methods
"""


class Loan:
    """
    Class variables from Loan: Period, maximum loan, minimum loan and loan increment
    """
    period = 36
    max_loan = 15000
    min_loan = 1000
    increase = 100

    def __init__(self, selected_lenders, amount):
        """
        Initialises a pd dataframe of selected lenders
        :param selected_lenders: dataframe passed from lenders
        :param amount: loan amount requested, input by user
        """
        self.results = selected_lenders
        self.amount = amount

    def calc_offer(self):
        """
        Calculates interest rate of offer for each lender dataframe
        :return: dataframe with montly payments in
        """
        self.results['Rate'].iloc[-1] = self.delta_rate  # Calculates new rate for portioned value
        self.results['Available'].iloc[-1] = self.delta_amount  # Calculates new available for portioned value
        a = self.results['Available']  # amount
        n = self.period  # Number of Periodic Payments (n)
        i = self.results.Rate / 12  # Annual rate divided by number of payment periods (i)
        d = (((1 + i)**n) - 1) / (i * (1 + i)**n)  # Discount Factor (D) = {[(1 + i) ^n] - 1} / [i(1 + i)^n]
        self.results['monthly'] = a / d

        return self.results

    @property
    def delta_amount(self):
        return self.amount - (self.results['Available'].sum() - self.results['Available'].iloc[-1])

    @property
    def delta_rate(self):
        return self.delta_amount / self.results['Available'].iloc[-1] * self.results['Rate'].iloc[-1]

    @property
    def rate(self):
        return self.results['Rate'].mean()

    @property
    def total(self):
        return self.results['monthly'].sum() * self.period

    @property
    def month(self):
        return self.results['monthly'].sum()

    def print_output(self):
        """
        Prints loan output to screen
        :return:
        """
        print("Request Amount: £{:.0f}".format(self.amount))
        print("Rate: {:.2f}%".format((self.rate * 100)))
        print("Total Repayment: £{:.2f}".format(self.total))
        print("Monthly Repayment: £{:.2f}".format(self.month))

    def input_validation(self):
        """
        Validates user input is correct and returns error if it is not
        :return:
        """
        if self.amount > self.max_loan:
            raise ValueError(
                'Loan value should be between {} and {}. Increments of £{} only'.format(self.max_loan, self.min_loan,
                                                                                        self.increase))
        if self.amount < self.min_loan:
            raise ValueError(
                'Loan value should be between {} and {}. Increments of £{} only'.format(self.max_loan, self.min_loan,
                                                                                        self.increase))
        if self.amount % self.increase != 0:
            raise ValueError
        else:
            return
