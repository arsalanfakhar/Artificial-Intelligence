import xlrd

loc=("C:\\Users\\Arsalan\\Desktop\\cars.xlsx")

wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)


print(sheet.cell_value(0,0))

print(sheet.cell_value(1,0))
