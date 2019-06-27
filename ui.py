import os
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

from fpdf import FPDF

import pdf_to_jpg
from table.checker import detect_square
from table.generator.table_generator import generate_table

questions = []
question_values = []
question_nums = []
answered = 0


def clear_without_menu():
    for child in window.winfo_children():
        if child.winfo_class() != 'Menu':
            child.destroy()


def generate_function():
    clear_without_menu()
    lbl = Label(window, text="Number of questions: ")
    lbl.grid(column=0, row=0)

    spin = Spinbox(window, from_=0, to=25, width=5, textvariable=questions_number, command=update_questions)
    spin.grid(column=1, row=0)

    lbl = Label(window, text="Number of answers: ")
    lbl.grid(column=0, row=1)

    spin = Spinbox(window, from_=2, to=6, width=5, textvariable=answers_number, command=update_questions)
    spin.grid(column=1, row=1)

    lbl = Label(window, text="exam file name: ")
    lbl.grid(column=2, row=0)
    e = Entry(window, textvariable=filname)
    e.grid(column=3, row=0)

    lbl = Label(window, text="answers file name: ")
    lbl.grid(column=2, row=1)
    add_radiobuttons(questions_number.get(), answers_number.get())
    e2 = Entry(window, textvariable=ans_filname)
    e2.grid(column=3, row=1)

    btn = Button(window, text="Generate pdf", command=generate_pdf)
    btn.grid(column=4, row=100)


def check_function():
    global pdf_file
    global answer_file
    clear_without_menu()
    pdf_file = filedialog.askopenfilename(initialdir="./.data/pdf", title="Select file",
                                          filetypes=(("pdf file", "*.pdf"), ("all files", "*.*")))
    answer_file = filedialog.askopenfilename(initialdir="./.data/ans", title="Select file",
                                             filetypes=(("txt file", "*.txt"), ("all files", "*.*")))
    Label(window, text="PREPARED PDF: " + pdf_file).grid(column=1, row=1)

    Label(window, text="PREPARED ANSWER FILE: " + answer_file).grid(column=1, row=2)

    btn = Button(window, text="Check answers", command=check_answers)
    btn.grid(column=1, row=3)


def add_radiobuttons(question, answers):
    global questions
    global question_nums
    global question_values
    questions = []
    question_values = []
    question_nums = []
    for i in range(question):
        questions.append([])
        lb = Label(window, text=str(i))
        lb.grid(column=0, row=i + 3)
        question_nums.append(lb)
        for j in range(answers):
            v = IntVar()
            question_values.append(v)
            rad = Checkbutton(window, text=chr(j + ord('A')), variable=v)
            rad.grid(column=j + 1, row=i + 3)
            questions[i].append(rad)


def update_questions():
    global questions
    global question_nums
    for i in question_nums:
        i.grid_forget()
    for i in questions:
        for j in i:
            j.grid_forget()
    add_radiobuttons(questions_number.get(), answers_number.get())


def generate_pdf():
    generate_table("./.data/pdf/" + filname.get(), answers_number.get(), questions_number.get())
    f = open('.data/ans/' + ans_filname.get(), 'w+')
    f.write(str(answers_number.get()) + "\n")
    f.write(str(questions_number.get()) + "\n")
    string = ""
    for i in range(0,len(question_values) - answers_number.get()+1, answers_number.get()):
        for j in range(answers_number.get()):
            if question_values[i+j].get() == 1:
                string += str(j)
                string += " "
        string += "\n"
    f.write(string)


def check_answers():
    global answered
    head, tail = os.path.split(pdf_file)
    RANDOM_PDF = pdf_file
    if not os.path.exists(head[:-4] + '/jpg/' + tail[:-4]):
        os.mkdir(head[:-4] + '/jpg/' + tail[:-4])
    if not os.path.exists(head[:-4] + '/jpg/' + tail[:-4] + 'RES/'):
        os.mkdir(head[:-4] + '/jpg/' + tail[:-4] + 'RES/')

    RANDOM_JPG = head[:-4] + '/jpg/' + tail[:-4] + '.jpg'
    RANDOM_OUTPUT = head[:-4] + '/jpg/' + tail[:-4] + 'RES/'
    pdf_to_jpg.convert(RANDOM_PDF, RANDOM_JPG)
    f = open(answer_file, 'r')
    contents = f.readline()
    width = int(contents)
    contents = f.readline()
    height = int(contents)
    x = int(contents)
    x, y = generate_table(".data/pdf/output.pdf", width, height)

    pdf = FPDF(unit='mm', format='A4')

    for r, d, fa in os.walk(head[:-4] + '/jpg/' + tail[:-4]):
        for file in fa:
            curr = RANDOM_OUTPUT + str(file)
            print(curr)
            detect_square.find_squares(head[:-4] + '/jpg/' + tail[:-4] + '/' + str(file), curr, x, y, answer_file, pdf)

    pdf.output("res.pdf")


pdf_file = ''
answer_file = ''

window = Tk()
window.title("Exam Checker")
window.geometry('700x900')

questions_number = IntVar()
questions_number.set(5)

answers_number = IntVar()
answers_number.set(4)

filname = StringVar()
filname.set("exam.pdf")

ans_filname = StringVar()
ans_filname.set("TMP.txt")

root_menu = Menu(window)
window.config(menu=root_menu)

generate_menu = Menu(root_menu)
root_menu.add_cascade(label="Generate", menu=generate_menu)
generate_menu.add_command(label="Generate PDF", command=generate_function)

check_menu = Menu(root_menu)
root_menu.add_cascade(label="Check", menu=check_menu)
check_menu.add_command(label="Check PDF", command=check_function)

window.mainloop()
