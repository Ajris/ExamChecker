import os

from pdf2image import convert_from_path


def convert(pdf_file, jpg_file):
    pages = convert_from_path(pdf_file, 100)
    i = 0
    if not os.path.exists(jpg_file[:-4]):
        os.mkdir(jpg_file[:-4])
    for page in pages:
        page.save(jpg_file[:-4] + '/' + 'part' + str(i) + '.jpg', 'JPEG')
        i = i + 1
