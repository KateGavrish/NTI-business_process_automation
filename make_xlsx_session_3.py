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
    book.save(f"{filename}.xlsx")


# вот например: make_xlsx_table("lol", [[1, 2, 3], [4, 5, 6]])
