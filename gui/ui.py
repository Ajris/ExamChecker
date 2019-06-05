from tkinter import *
from tkinter.ttk import *
from table.generator.table_generator import generate_table
from gui import pdf_to_jpg
from table.checker import detect_square
from PIL import Image

questions = []
question_values = []
question_nums = []


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
    clear_without_menu()
    Label(window, text="Username").grid(row=10)  # this is placed in 0 0
    Entry(window).grid(row=0, column=1)

    btn = Button(window, text="Check answers", command=check_answers)
    btn.grid(column=2, row=1)


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
    generate_table(".data/pdf/output.pdf", answers_number.get(), questions_number.get())


def check_answers():
    RANDOM_PDF = '.data/pdf/test1.pdf'
    RANDOM_JPG = '.data/jpg/Document1.jpg'
    RANDOM_OUTPUT = '.data/out/Output-Random.jpg'
    x, y = generate_table(".data/pdf/output.pdf", answers_number.get(), questions_number.get())
    answers = detect_square.find_squares(RANDOM_JPG, RANDOM_OUTPUT, x, y)
    pdf_to_jpg.convert(RANDOM_PDF, RANDOM_JPG)
    print(len(question_values))
    if len(answers) == len(question_values):
        correct = 0
        for i in range(len(answers)):
            print(str(answers[i]) + " " + str(question_values[i].get()))
            if answers[i] == question_values[i].get():
                correct += 1
        print(correct)
    else:
        print("Wrong number of questions")

    Image.open(RANDOM_OUTPUT).show()


window = Tk()
window.title("Exam Checker")
window.geometry('500x900')

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
