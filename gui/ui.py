from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import sys
sys.path.insert(0, '/home/charon/Documents/ExamChecker/table/generator')
sys.path.insert(0, '/home/charon/Documents/ExamChecker/table')
from table_generator import generate_table

import pdf_to_jpg
from checker import detect_square
from PIL import Image

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
    add_radiobuttons(questions_number.get(), answers_number.get())

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
        v = IntVar()
        question_values.append(v)
        lb = Label(window, text=str(i))
        lb.grid(column=0, row=i + 3)
        question_nums.append(lb)
        for j in range(answers):
            rad = Radiobutton(window, text=chr(j + ord('A')), value=j, variable=v)
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
    generate_table("./.data/pdf/output.pdf", answers_number.get(), questions_number.get())


def check_answers():
    global answered
    RANDOM_PDF = pdf_file
    RANDOM_JPG = '.data/jpg/Document1.jpg'
    RANDOM_OUTPUT = '.data/out/Output-Random.jpg'
    x, y = generate_table(".data/pdf/output.pdf", answers_number.get(), questions_number.get())
    pdf_to_jpg.convert(RANDOM_PDF, RANDOM_JPG)
    answers = detect_square.find_squares(RANDOM_JPG, RANDOM_OUTPUT, x, y, answer_file)

    f = open(answer_file, 'r')
    contents = f.readlines()
    for line in contents:
        for i in range(len(line)-1):
            if line[i] == str(answers[i]):
                answered = answered + 1


    Label(window, text="CORRECT: " + str(answered) + "/25").grid(column=1, row=4)

    Image.open(RANDOM_OUTPUT).show()


pdf_file = ''
answer_file = ''

window = Tk()
window.title("Exam Checker")
window.geometry('700x900')

questions_number = IntVar()
questions_number.set(25)

answers_number = IntVar()
answers_number.set(4)

root_menu = Menu(window)
window.config(menu=root_menu)

generate_menu = Menu(root_menu)
root_menu.add_cascade(label="Generate", menu=generate_menu)
generate_menu.add_command(label="Generate PDF", command=generate_function)

check_menu = Menu(root_menu)
root_menu.add_cascade(label="Check", menu=check_menu)
check_menu.add_command(label="Check PDF", command=check_function)

window.mainloop()
