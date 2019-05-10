import random

from fpdf import FPDF

class AnswerSheetGenerator(FPDF):
    box_width = 6
    box_h_space = 10
    box_v_space = 10

    def __init__(self):
        FPDF.__init__(self, unit = 'mm', format='A4')
        self.add_page()
        self.set_font('Arial', 'B', 16)
    def get_x(self, width):
        return (210 - self.box_h_space*(width + 2))/2

    def add_row(self, width):
        black = random.randrange(0, width)
        for i in range(width):
            self.set_x(self.get_x(width) + self.box_h_space*(i + 1.5) - self.box_width/2)
            if i == black:
                self.cell(self.box_width, self.box_width, '', fill=True, border = 1)
            else:
                self.cell(self.box_width, self.box_width, '', border = 1)

    def generate_table(self, width, height):
        for i in range(width):
            self.set_x(self.get_x(width) + self.box_h_space*(i + 1.5) - self.box_width/2)
            self.cell(self.box_width, self.box_width, chr(i + ord('A')), border = 0)
        for i in range(height):
            self.set_y(i*10 + 30)
            self.set_x(self.get_x(width))
            self.cell(self.box_width, self.box_width, str(i + 1))
            self.add_row(width)

def generate_table(name, width, height):
    pdf = AnswerSheetGenerator() 
    pdf.generate_table(width, height)
    pdf.output(name)

generate_table('table.pdf', 4, 25)
