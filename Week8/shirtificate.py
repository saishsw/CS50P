from fpdf import FPDF


def main():
    shirtificate(input("Name: "))

def shirtificate(name):
    pdf = FPDF( orientation = "portrait", format = "A4")
    pdf.add_page()

    pdf.set_font("Helvetica", size = 30)
    pdf.set_y(10)
    pdf.cell(w = 0, h = 20, text = "CS50 Shirtificate", align = "C")

    pdf.image("shirtificate.png", x = 15, y = 70, w = 180)

    pdf.set_y(140)
    pdf.set_font("Helvetica", size = 15)
    pdf.set_text_color(255, 255, 255)

    pdf.cell(w = 0, h = 5, text = f"{name} took CS50", align = "C")

    pdf.output("shirtificate.pdf")

main()