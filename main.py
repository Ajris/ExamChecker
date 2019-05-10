import pdf
import pdf_to_jpg
import detect_square

pdf.simple_table_html()
pdf_to_jpg.convert('simple_table_html.pdf')
detect_square.find_squares()
