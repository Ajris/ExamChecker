# simple_table_html.py
 
from fpdf import FPDF, HTMLMixin

import HTML
table_data = [
        ['Last name',   'First name',   'Age'],
        ['Smith',       'John',         30],
        ['Carpenter',   'Jack',         47],
        ['Johnson',     'Paul',         62],
    ]
htmlcode = HTML.table(table_data)

class HTML2PDF(FPDF, HTMLMixin):
    pass
 
def simple_table_html():
    pdf = HTML2PDF()
 
    table = htmlcode 
 
    pdf.add_page()
    pdf.write_html(table)
    pdf.output('simple_table_html.pdf')
 
if __name__ == '__main__':
    simple_table_html()
