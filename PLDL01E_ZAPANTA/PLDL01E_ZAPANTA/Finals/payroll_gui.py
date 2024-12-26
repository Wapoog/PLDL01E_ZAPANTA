from tkinter import Label, Text, Button, ttk
from PIL import Image, ImageTk

class PayrollGUI:
    def __init__(self, window):
        self.window = window
        self.window.title('Payroll Check GUI')
        self.window.geometry("900x1520")

    def create_label(self, x, y, text, font=('Arial', 10)):
        label = Label(self.window, text=text, font=font)
        label.place(x=x, y=y)
        return label

    def create_textbox(self, x, y, width=25, height=1, fg='black', bg='white', font=('Arial', 12)):
        textbox = Text(self.window, width=width, height=height, fg=fg, bg=bg, font=font)
        textbox.place(x=x, y=y)
        return textbox

    def create_button(self, x, y, text, width=10, bg='red', fg='white'):
        button = Button(self.window, width=width, text=text, bg=bg, fg=fg, cursor='hand2', border=5)
        button.place(x=x, y=y)
        return button

    def create_button1(self, x, y, text, width=10, bg='red', fg='white', relief='raised'):
        button = Button(self.window, width=width, text=text, bg=bg, fg=fg, cursor='hand2', border=2, relief='solid')
        button.place(x=x, y=y)
        return button

    def create_image(self, image_path, x, y, width, height):
        image = Image.open(image_path)
        resized_image = ImageTk.PhotoImage(image.resize((width, height)))
        label = Label(self.window, image=resized_image)
        label.image = resized_image  # Keep a reference to avoid garbage collection
        label.place(x=x, y=y)
        return label