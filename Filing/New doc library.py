import docx as d

d.Document('cv.doc')


d.add_pictures('demo.jpg')

records=((3,'101','Spam'),(3,'101','Spad'),(2,'101','Spam'))

hdr_cells=table.row[0].cells

for qty,id,desc  in records:
    row_cells=table.add.row().cells
    row_cells[0].text=str(qty)
    row_cells[1].text=id
    row_cells[2].text =desc
#Add page break
d.add_page_break()


d.image('dddd')

