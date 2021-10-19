import PyPDF2
path = r"C:\Users\Matthew Prata\Downloads\CostcoReceipt.pdf"
pdf_file = open(path,'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print(page_content)