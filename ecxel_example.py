import openpyxl
wb = openpyxl.load_workbook(filename = 'Комплектующие.xlsx')
sheet = wb['Лист1']

#считываем значение определенной ячейки
val = sheet['A1'].value
#считываем заданный диапазон
vals = []
n = 0
while True:
    n += 1
    val = [sheet[f'A{n}'].value, sheet[f'B{n}'].value, sheet[f'C{n}'].value]
    vals.append(val)
    if val[0] == None:
        break
vals = vals[1:]
print(*vals)