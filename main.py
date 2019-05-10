import table_generator as tge
import pdf_to_jpg
import detect_square
from PIL import Image

# print("TEST GENERATED")
# WIDTH = 4
# HEIGHT = 25
# GENERATED_PDF = 'data/pdf/Generated-Document.pdf'
# GENERATED_JPG = 'data/jpg/Generated-Created-Document.jpg'
# GENERATED_OUTPUT = 'data/out/Output-Generated.jpg'
#
# tge.generate_table(GENERATED_PDF, WIDTH, HEIGHT)
# pdf_to_jpg.convert(GENERATED_PDF, GENERATED_JPG)
# detect_square.find_squares(GENERATED_JPG, GENERATED_OUTPUT)
#
# # Image.open(GENERATED_OUTPUT).show()
#
# print("TEST SCANNED")
# SCANNED_PDF = 'data/pdf/Scanned-Document.pdf'
# SCANNED_JPG = 'data/jpg/Converted-Scanned-Document.jpg'
# SCANNED_OUTPUT = 'data/out/Output-Scanned.jpg'
#
# pdf_to_jpg.convert(SCANNED_PDF, SCANNED_JPG)
# detect_square.find_squares(SCANNED_JPG, SCANNED_OUTPUT)

# Image.open(SCANNED_OUTPUT).show()

print("TEST RANDOM")
RANDOM_PDF = 'data/pdf/Random-Document.pdf'
RANDOM_JPG = 'data/jpg/Converted-Random-Document.jpg'
RANDOM_OUTPUT = 'data/out/Output-Random.jpg'

pdf_to_jpg.convert(RANDOM_PDF, RANDOM_JPG)
detect_square.find_squares(RANDOM_JPG, RANDOM_OUTPUT)

Image.open(RANDOM_OUTPUT).show()
