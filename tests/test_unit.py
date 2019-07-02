import pytest
import pandas as pd
from pandas.util.testing import assert_frame_equal
import numpy as np

import app


test_lender = pd.DataFrame(
        [['Jane', 0.069, 480, 14.79],
        ['Fred', 0.071, 520, 16.08]],
        columns=['Lender', 'Rate', 'Available', 'monthly'])


class TestLoan:

    def setup_method(self):
        self.amount = 1000
        self.loan = app.Loan(test_lender, self.amount)

    def test_calc_offer(self):
        loan_offer = self.loan.calc_offer()
        pd.testing.assert_frame_equal(loan_offer, test_lender)

    def test_rate(self):
        assert self.loan.rate == 0.07

    def test_delta_amount(self):
        assert self.loan.delta_amount == 520

    def test_delta_rate(self):
        assert self.loan.delta_rate == 0.071

    def test_total(self):
        assert round(self.loan.total, 2) == 1111.64

    def test_month(self):
        assert round(self.loan.month, 2) == 30.88

    def test_input_validation_u1000(self):
        self.loan.amount = 900
        with pytest.raises(ValueError):
            self.loan.input_validation()

    def test_input_validation_increase(self):
        self.loan.amount = 1050
        with pytest.raises(ValueError):
            self.loan.input_validation()


if __name__ == '__main__':
    pytest.main()

