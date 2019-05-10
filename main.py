import pdf_to_jpg
import detect_square

PDF_NAME = 'data/table.pdf'
CONVERTED_PDF = 'data/convertedPDF.jpg'
OUTPUT = 'data/out.jpg'

# pdf_to_jpg.convert(PDF_NAME, CONVERTED_PDF)
detect_square.find_squares(CONVERTED_PDF, OUTPUT)
