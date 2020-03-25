import openpyxl


def import_drons(file_name):
    wb = openpyxl.load_workbook(filename = file_name)
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
    return vals

def import_komplecktuyshye(file_name):
    wb = openpyxl.load_workbook(filename=file_name)
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
    return vals


def import_technial_map(file_name):
    wb = openpyxl.load_workbook(filename=file_name)
    sheet = wb['Лист1']

    vals = []
    n = 0
    while True:
        n += 1
        val = [sheet[f'A{n}'].value, sheet[f'B{n}'].value, sheet[f'C{n}'].value, sheet[f'D{n}'].value]
        vals.append(val)
        if val[0] == None and val[1] == None and val[2] == None and val[3] == None:
            break
    vals = vals[1:]
    return vals