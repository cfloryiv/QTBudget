from unittest import TestCase
from busrules import Period


class TestPeriod(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_next(self):
        period = Period('21-05')
        period.next()
        pstring = period.period
        self.assertTrue(pstring == '21-06')

    def test_month(self):
        period = Period('21-01')
        month = period.month()
        self.assertTrue(month == 1)

    def test_year(self):
        period = Period('22-12')
        year = period.year()
        self.assertTrue(year == 22)

    def test_period(self):
        period = Period('19-10')
        pstring = period.period
        self.assertTrue(pstring == '19-10')
