import pytest

import app


class TestLoan:

    def test_run_app(self):
        loan = app.main('market.csv', 1000)
        assert loan.rate == 0.07
        assert round(loan.total, 2) == 1111.64
        assert round(loan.month, 2) == 30.88
        assert round(loan.amount, 0) == 1000


if __name__ == '__main__':
    pytest.main()
