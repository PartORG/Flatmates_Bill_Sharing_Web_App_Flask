class Bill:
    """
    Object that contains data about a bill,
    such as total amount and a period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a Flatmate person who lives in the flat
    and pays a share of the Bill.
    """

    def __init__(self, name, days_in_flat):
        self.name = name
        self.days_in_flat = days_in_flat

    def pays(self, bill, flatmate2):
        weight = self.days_in_flat / (self.days_in_flat + flatmate2.days_in_flat)
        return round(bill.amount * weight, 3)
