import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

#  window
window = tk.Tk()
window.title("Assessment Form")
window.geometry('1920x1080')
window.configure(bg='white')
image = Image.open('LPU1.jpg')
bck_pic = ImageTk.PhotoImage(image.resize((280, 200)))
lbl = Label(window, image=bck_pic)
lbl.place(x=1, y=1)


class GuiDesign:
    def __init__(self):
        frame1 = ''

    def frames(self, x, y):
        self.frame1 = Frame(window, width=1500, height=160, border=0, bg='#a2262f')
        self.frame1.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 11))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg= 'white', bg='#a2262f', font=('Times New Roman', 12, 'bold'))
        self.lbl.place(x=x, y=y)


my_gui_design = GuiDesign()
#  call
my_gui_design.frames(200, 220)
my_gui_design.frames(200, 400)
my_gui_design.frames(200, 580)

#  text box in the first frame
student_nametxt = my_gui_design.textbox_design1(300, 262)
student_numbertxt = my_gui_design.textbox_design1(650, 262)
student_course = my_gui_design.textbox_design1(950, 262)
academic_yeartxt = my_gui_design.textbox_design1(300, 330)
current_datetxt = my_gui_design.textbox_design1(650, 330)

#  textbox in the second frame
sectiontxt = my_gui_design.textbox_design2(300, 467)
subjecttxt = my_gui_design.textbox_design2(630, 467)
unitstxt = my_gui_design.textbox_design2(950, 467)

#  textbox label in the first frame
student_namelbl = my_gui_design.label_design(300, 235, 'Student Name')
student_numberlbl = my_gui_design.label_design(650, 235, 'Student Number')
student_courselbl = my_gui_design.label_design(950, 235, 'Student Course')
academic_yearlbl = my_gui_design.label_design(300, 305, 'Academic Year')
current_datelbl = my_gui_design.label_design(650, 305, 'Current Date')

#  textbox label in the second frame
sectionlbl = my_gui_design.label_design(300, 440, 'Section')
subjectlbl = my_gui_design.label_design(630, 440, 'Subjects')
unitslbl = my_gui_design.label_design(950, 440, 'Units')

#  text box in the third frame
sectiontxt = my_gui_design.textbox_design2(300, 660)

window.mainloop()