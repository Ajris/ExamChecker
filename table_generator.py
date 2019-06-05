import random

from fpdf import FPDF


class AnswerSheetGenerator(FPDF):
    box_width = 6
    box_h_space = 10
    box_v_space = 10
    answers_y_pos = []
    answers_x_pos = []
    width = None
    height = None

    def __init__(self, width, height, random_answer=False):
        FPDF.__init__(self, unit='mm', format='A4')
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.width = width
        self.height = height
        self.generate_table(width, height, random_answer)
        self.generate_reference_rectangles()

    def get_x(self, width):
        return (210 - self.box_h_space * (width + 2)) / 2

    def add_row(self, width, random_answer=False):
        black = random.randrange(0, width)
        for i in range(width):
            self.set_x(self.get_x(width) + self.box_h_space * (i + 1.5) - self.box_width / 2)
            if random_answer and i == black:
                self.cell(self.box_width, self.box_width, '', fill=True, border=1)
            else:
                self.cell(self.box_width, self.box_width, '', border=1)

    def generate_table(self, width, height, random_answer=False):
        self.set_y(20)
        for i in range(width):
            x_pos = self.get_x(width) + self.box_h_space * (i + 1.5) - self.box_width / 2
            self.set_x(x_pos)
            self.cell(self.box_width, self.box_width, chr(i + ord('A')), border=0)
            #  self.answers_x_pos.append(x_pos - 22.5 + self.box_width/2)
            self.answers_x_pos.append(x_pos - 22.5)
        for i in range(height):
            y_pos = i * self.box_v_space + 30
            self.set_y(y_pos)
            self.set_x(self.get_x(width))
            self.cell(self.box_width, self.box_width, str(i + 1))
            self.add_row(width, random_answer)
            self.answers_y_pos.append(y_pos - 22.5)
            #  self.answers_y_pos.append(y_pos - 22.5 + self.box_width/2)

    def generate_reference_rectangles(self):
        self.rect(15, 15, 15, 15)
        self.rect(210 - 30, 15, 15, 15)
        self.rect(210 - 30, 297 - 30, 15, 15)
        self.rect(15, 297 - 30, 15, 15)

    #  def get_answer(self, question, answer):
    #  return self.answers.get(question)


def generate_table(name, width, height):
    pdf = AnswerSheetGenerator(width, height)
    pdf.output(name)


def random_answer_table(name, width, height):
    pdf = AnswerSheetGenerator(width, height, True)
    pdf.output(name)
    # print(pdf.answers_x_pos)
    # print(pdf.answers_y_pos)
    return pdf.answers_x_pos, pdf.answers_y_pos


if __name__ == '__main__':
#  def random_answer_table(name, width, height):
#  pdf = AnswerSheetGenerator(width, height, True)
#  pdf.output(name)

    generate_table('table.pdf', 4, 25)
