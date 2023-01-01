import openpyxl

path="C:\python-selenium\Data Driven\Excel Data\Writing_Data1.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active





for r in range(1, 6):
    for c in range(1, 6):
        sheet.cell(row=r, column=c).value = "welcome"

workbook.save(path)
