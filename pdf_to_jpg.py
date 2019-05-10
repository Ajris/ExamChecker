from pdf2image import convert_from_path


def convert(filename):
    pages = convert_from_path(filename, 300)
    for page in pages:
        page.save('out.jpg', 'JPEG')
