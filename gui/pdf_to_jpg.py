from pdf2image import convert_from_path


def convert(pdf_file, jpg_file):
    pages = convert_from_path(pdf_file, 100)
    for page in pages:
        page.save(jpg_file, 'JPEG')
