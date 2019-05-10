import table_generator as tge
import pdf_to_jpg
import detect_square

WIDTH = 4
HEIGHT = 25
PDF_NAME = 'data/table.pdf'
CONVERTED_PDF = 'data/convertedPDF.jpg'
OUTPUT = 'data/out.jpg'

tge.generate_table(PDF_NAME, WIDTH, HEIGHT)
pdf_to_jpg.convert(PDF_NAME, CONVERTED_PDF)
detect_square.find_squares(CONVERTED_PDF, OUTPUT)
