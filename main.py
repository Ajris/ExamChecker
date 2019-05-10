import table_generator as tge
import pdf_to_jpg
import detect_square


print("TEST GENERATED IN COMPUTER")
WIDTH = 4
HEIGHT = 25
PDF_NAME = 'data/pdf/Generated-Document.pdf'
CONVERTED_PDF = 'data/jpg/Generated-Created-Document.jpg'
OUTPUT = 'data/out/Output-Generated.jpg'

tge.generate_table(PDF_NAME, WIDTH, HEIGHT)
pdf_to_jpg.convert(PDF_NAME, CONVERTED_PDF)
detect_square.find_squares(CONVERTED_PDF, OUTPUT)

print("TEST OWN GENERATED")
PDF_NAME = 'data/pdf/Scanned-Document.pdf'
CONVERTED_PDF = 'data/jpg/Converted-Scanned-Document.jpg'
OUTPUT = 'data/out/Output-Scanned.jpg'

pdf_to_jpg.convert(PDF_NAME, CONVERTED_PDF)
detect_square.find_squares(CONVERTED_PDF, OUTPUT)
