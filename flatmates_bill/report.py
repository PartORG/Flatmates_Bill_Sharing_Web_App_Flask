import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a PDF file that contains data about flatmates,
    such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(flatmate1.pays(bill, flatmate2))
        flatmate2_pay = str(flatmate2.pays(bill, flatmate1))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add icon
        pdf.image('files/house.png', w=60, h=60)

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, align='C', ln=1)

        pdf.set_font(family='Times', size=14, style='I')
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, align='C', ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, align='C', ln=1)

        pdf.output(f"files/{self.file_name}")
        webbrowser.open(f"files/{self.file_name}")
