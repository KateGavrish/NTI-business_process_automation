import openpyxl


def import_drons():
    wb = openpyxl.load_workbook(filename = 'СписокДронов.xlsx')
    sheet = wb['Лист1']

    vals = []
    n = 0
    while True:
        n += 1
        val = [sheet[f'A{n}'].value, sheet[f'B{n}'].value, sheet[f'C{n}'].value]
        vals.append(val)
        if val[0] == None and val[1] == None and val[2] == None:
            break
    vals = vals[1:]
    print(*vals)

def import_komplecktuyshye():
    wb = openpyxl.load_workbook(filename='Комплектующие.xlsx')
    sheet = wb['Лист1']

    vals = []
    n = 0
    while True:
        n += 1
        val = [sheet[f'A{n}'].value, sheet[f'B{n}'].value, sheet[f'C{n}'].value]
        vals.append(val)
        if val[0] == None and val[1] == None and val[2] == None:
            break
    vals = vals[1:]
    print(*vals)


def import_technial_map():
    wb = openpyxl.load_workbook(filename='ТехнологическиеКарты.xlsx')
    sheet = wb['Лист1']

    vals = []
    n = 0
    while True:
        n += 1
        val = [sheet[f'A{n}'].value, sheet[f'B{n}'].value, sheet[f'C{n}'].value]
        vals.append(val)
        if val[0] == None and val[1] == None and val[2] == None:
            break
    vals = vals[1:]
    print(*vals)