from flat import Bill, Flatmate
from report import PdfReport


def main():
    bill_amount = int(input("Hey user, enter the bill amount: "))
    bill_period = input("What is the bill period? E.g. December 2020: ")

    flatmate1_name = input("What is your name? ")
    flatmate1_days = int(input(f"How many days did {flatmate1_name} stay in the house during the bill period? "))

    flatmate2_name = input("What is the name of the other flatmate? ")
    flatmate2_days = int(input(f"How many days did {flatmate1_name} stay in the house during the bill period? "))

    the_bill = Bill(bill_amount, bill_period)
    flat1 = Flatmate(name=flatmate1_name, days_in_flat=flatmate1_days)
    flat2 = Flatmate(name=flatmate2_name, days_in_flat=flatmate2_days)

    print(f"{flat1.name} pays: ", flat1.pays(bill=the_bill, flatmate2=flat2))
    print(f"{flat2.name} pays: ", flat2.pays(bill=the_bill, flatmate2=flat1))

    pdf_report = PdfReport(file_name="report_1.pdf")
    pdf_report.generate(flatmate1=flat1, flatmate2=flat2, bill=the_bill)


if __name__ == '__main__':
    main()
