import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Employee Registration")
window.geometry('1520x900')

class design_gui_inteface():
    def __int__(self, frame1):
        frame = ''
    def frames(self, x, y):
        self.frame1 = Frame(window, width=1100, height=160, border=0,
           bg='light gray')
        self. frame1.place (x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text (width=25, height= 1, fg='black', bg='white',
           font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=31, height=1, fg='black', bg='white',
            font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self. lbl = Label(text=text_value, bg='light gray',font)
