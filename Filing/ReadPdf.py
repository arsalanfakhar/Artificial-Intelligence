
#
# pdffileobj=open("C:\\Users\\Arsalan\\Desktop\\CA.pdf",'rb')
# pdfReader=PyPDF2.PdfFileReader(pdffileobj)
#
# print(pdfReader.documentInfo)

import PyPDF2
pdf_file = open("C:\\Users\\Arsalan\\Desktop\\CA.pdf", 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
count = read_pdf.numPages

for i in range(count):
    page = read_pdf.getPage(i)
    print(page.extractText())


# number_of_pages = read_pdf.getNumPages()
# page = read_pdf.getPage(0)
# page_content = page.extractText()
# print (page_content)