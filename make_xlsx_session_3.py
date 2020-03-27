import xlwt


def make_xlsx_table(filename, spisok):
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("Sheet1")
    row = sheet1.row(0)
    for i in range(3):
        row.write(i, ["№", "Комплектующее", "Остаток"][i])
    for num in range(1, len(spisok) + 1):
          row = sheet1.row(num)
          for index in range(3):
              value = spisok[num - 1][index]
              row.write(index, value)
    book.save(filename)


# вот например: make_xlsx_table("lol", [[1, 2, 3], [4, 5, 6]])


from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
pdf.output("simple_demo.pdf")


def simple_table(spisok, spacing=1):
    data = spisok
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    pdf.add_page()
    data = [['N', 'экмммэ', 'fewf']] + spisok
    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height * spacing,
                     txt=item, border=1)
        pdf.ln(row_height * spacing)

    pdf.output('result_table.pdf')


if __name__ == '__main__':
    simple_table([["fdfd", "dfdf", "dfdf"], ["fddf", "fddf", "dfdffd"]])