from decimal import Decimal


class CommissionEmployee:
    def __init__(self, first_name, last_name, gender, nin, sales, rate):
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._nin = nin
        self._sales = sales
        self._rate = rate

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def gender(self):
        return self._gender

    @property
    def nin(self):
        return self._nin

    @property
    def sale(self):
        return self._sales

    @sale.setter
    def sales(self, value):
        if value < Decimal(0.0):
            raise ValueError("Invalid sales")

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        if Decimal(0.0) < rate < Decimal(1.0):
            raise ValueError("Invalid rate amount")
        self._rate = rate

    def earning(self):
        return self.sales * (self.rate / 100)

    def __repr__(self):
        return f"FirstName: {self._first_name}\n LastName: {self._last_name}\n" \
               f"Nin: {self._nin}\n Earning: {self.earning()}"


eto = CommissionEmployee("timi", "obantu", "'male", 123, 200, 20)

print(eto)
