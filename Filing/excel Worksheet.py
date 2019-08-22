import xlsxwriter

workbook=xlsxwriter.Workbook('C:\\Users\\Arsalan\\Desktop\\example_2.xlsx')
worksheet=workbook.add_worksheet()


worksheet1=workbook.add_worksheet()
worksheet2=workbook.add_worksheet('Data')
worksheet3=workbook.add_worksheet()

expenses=(['rent',23],['gas',234],['food',324])

row=0
col=0

for item , cost in (expenses):
    worksheet1.write(row,col,item)
    worksheet1.write(row, col+1, cost)
    row += 1


workbook.close()