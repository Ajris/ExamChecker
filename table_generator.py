import pdf, random

#  def generate_table(height, width):
    #  table = """<table border="1" cellpadding="5px">"""

    #  for i in range(height):
        #  table += generate_row(width)
    #  table += "</table>"
    #  return table
    
#  def generate_row(width):
    #  row = "<tr>"
    #  for i in range(width):
        #  row += "<td width=100> <table> <tr> <td width=30> </td> </tr> </table> </td>"
    #  row += "</tr>"
    #  return row
#  table = generate_table(1, 1)
#  print(table)
#  pdf.simple_table_html(generate_table(1, 1))

from fpdf import FPDF
def add_row(pdf, width):
    x = (210 - 20*width - 10)/2
    black = random.randrange(0, width)
    for i in range(width):
        pdf.set_x(x + 20*i + 10)
        if i == black:
            pdf.cell(10, 10, '', fill=True, border = 1)
        else:
            pdf.cell(10, 10, '', border = 1)


def generate_table(pdf, width, height):
    for i in range(height):
        pdf.set_y(i*20 + 30)
        add_row(pdf, width)
pdf = FPDF(unit = 'mm', format='A4') 
pdf.set_font('Arial', 'B', 16)
pdf.add_page()
#  add_row(pdf, 4)
generate_table(pdf, 4, 7)
#  pdf.cell(10, 10, 'a', border = 1)
pdf.output('table.pdf')
