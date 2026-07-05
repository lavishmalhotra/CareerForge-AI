from fpdf import FPDF


def create_pdf(title, content, filename):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_auto_page_break(True, 15)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, title, ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "", 11)

    for line in content.split("\n"):

        try:
            pdf.multi_cell(
                0,
                8,
                line.encode("latin-1", "replace").decode("latin-1")
            )
        except:
            pass

    pdf.output(filename)

    return filename