import PyPDF2


def pdf_reader() :
    pn = input("Please enter the full name of the pdf with extension:")
    book = open(pn,'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(f"Total numbers of pages in this book {pages}")
    print("Please enter the page number I have to read")
    pg = int(input ("Please enter the page number: ") )
    page = pdfReader.getPage(pg)
    text = page.extractText()
    print(text)

pdf_reader()