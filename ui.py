from tkinter import *
 
from tkinter.ttk import *
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('500x600')

questions_number = IntVar()
questions_number.set(10)
 
answers_number = IntVar()
answers_number.set(4)

questions = []
def add_radiobuttons(question, answers):
    global questions
    questions = []
    for i in range(question):
        questions.append([])
        for j in range(answers):
            rad = Radiobutton(window, text=chr(j + ord('A')), value=j, variable=i)
            rad.grid(column = j, row = i + 3)
            questions[i].append(rad)

def update_questions():
    global questions
    for i in questions:
        for j in i:
            j.grid_forget()
    add_radiobuttons(questions_number.get(), answers_number.get())

spin = Spinbox(window, from_=0, to=100, width=5)


lbl = Label(window, text="Number of questions: ")
lbl.grid(column=0, row=0)

spin = Spinbox(window, from_=0, to=25, width=5, textvariable=questions_number, command=update_questions)
spin.grid(column=1, row=0)

lbl = Label(window, text="Number of answers: ")
lbl.grid(column=0, row=1)

spin = Spinbox(window, from_=2, to=6, width=5, textvariable=answers_number, command = update_questions)
spin.grid(column=1, row=1)

def clicked():
   print(answers_number.get())
   print(questions_number.get())

add_radiobuttons(questions_number.get(), answers_number.get())

btn = Button(window, text="Generate pdf", command=clicked)
btn.grid(column = 2, row = 0)

window.mainloop()
