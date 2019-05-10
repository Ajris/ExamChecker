# simple_table_html.py
 
from fpdf import FPDF, HTMLMixin
 
class HTML2PDF(FPDF, HTMLMixin):
    pass

def simple_table_html(tab):
    pdf = HTML2PDF()
 
    pdf.add_page()

    pdf.write_html(tab)
    pdf.output('simple_table_html.pdf')
 
if __name__ == '__main__':
    tab = """<table border="1" cellpadding="5px">
        <tr>
        <td widht=100> 
        x
        </td>
        </table>"""
    simple_table_html(tab)
