import tkinter as tk
from tkinter import Label, Text, ttk
from PIL import Image, ImageTk

class MeralcoGUI:
    def __init__(self, window):
        self.window = window
        self.window.title('Meralco Bill GUI')
        self.window.geometry("900x900")

    def create_label1(self, x, y, text, font=('Arial', 9)):
        label = Label(self.window, text=text, font=font)
        label.place(x=x, y=y)
        return label

    def create_label2(self, x, y, text, font=('Arial', 16), fg='#575757'):
        label = Label(self.window, text=text, font=font, fg=fg)
        label.place(x=x, y=y)
        return label

    def create_label3(self, x, y, text, font=('Arial', 10), fg='black'):
        label = Label(self.window, text=text, font=font, fg=fg)
        label.place(x=x, y=y)
        return label

    def create_label4(self, x, y, text, font=('Arial', 12, 'bold'), fg='black'):
        label = Label(self.window, text=text, font=font, fg=fg)
        label.place(x=x, y=y)
        return label

    def create_label5(self, x, y, text, font=('Arial', 12, 'bold'), fg='black', bg='#dfdfdf'):
        label = Label(self.window, text=text, font=font, fg=fg, bg=bg)
        label.place(x=x, y=y)
        return label

    def create_label6(self, x, y, text, font=('Arial', 9), fg='black', bg='#ccf0f2'):
        label = Label(self.window, text=text, font=font, fg=fg, bg=bg)
        label.place(x=x, y=y)
        return label

    def create_label7(self, x, y, text, font=('Arial', 10, 'bold'), fg='black', bg='#ccf0f2'):
        label = Label(self.window, text=text, font=font, fg=fg, bg=bg)
        label.place(x=x, y=y)
        return label

    def create_label8(self, x, y, text, font=('Arial', 24, 'bold'), fg='black', bg='#ccf0f2'):
        label = Label(self.window, text=text, font=font, fg=fg, bg=bg)
        label.place(x=x, y=y)
        return label

    def create_image(self, image_path, x, y, width, height):
        image = Image.open(image_path)
        resized_image = ImageTk.PhotoImage(image.resize((width, height)))
        label = Label(self.window, image=resized_image)
        label.image = resized_image  # Keep a reference to avoid garbage collection
        label.place(x=x, y=y)
        return label

    def create_frame1(self, x, y, width=410, height=215, bg='#ccf0f2'):
        frame1 = tk.Frame(self.window, width=width, height=height, bg=bg)
        frame1.place(x=x, y=y)
        return frame1

    def create_frame2(self, x, y, width=385, height=125, bg='#ccf0f2', highlightbackground='#58c8cf'):
        frame1 = tk.Frame(self.window, width=width, height=height, bg=bg, highlightbackground=highlightbackground, highlightthickness=1)
        frame1.place(x=x, y=y)
        return frame1

    def create_square(self, x, y, width=30, height=30, bg='#dfdfdf'):
        square =tk.Frame(self.window, width=width, height=height, bg=bg)
        square.place(x=x, y=y)
        return square

    def create_separator1(self, x, y, width=410, height=2, bg='#c4c4c4'):
        separator1 = ttk.Separator(self.window, orient='horizontal')
        separator1.place(x=x, y=y, width=width, height=height)
        return separator1
