from tkinter import Label, Text, Button, ttk # Import Label, Text, Button, and ttk modules
from PIL import Image, ImageTk # Import Image and ImageTk modules

class PayrollGUI:
    def __init__(self, window):
        # Initialize the window
        self.window = window
        self.window.title('Payroll Check GUI')
        self.window.geometry("900x1520") # Set the window size
        self.window.configure(bg='#f2f0e3') # Set the window background color

    def create_label(self, x, y, text, font=('Arial', 10), bg='#f2f0e3'):
        # Create a label
        label = Label(self.window, text=text, font=font, bg=bg)
        label.place(x=x, y=y)
        return label

    def create_textbox(self, x, y, width=25, height=1, fg='black', bg='white', font=('Arial', 12)):
        # Create a textbox
        textbox = Text(self.window, width=width, height=height, fg=fg, bg=bg, font=font)
        textbox.place(x=x, y=y)
        return textbox

    def create_button(self, x, y, text, width=10, bg='red', fg='white'):
        # Create the 'SEARCH' button
        button = Button(self.window, width=width, text=text, bg=bg, fg=fg, cursor='hand2', border=5)
        button.place(x=x, y=y)
        return button

    def create_button1(self, x, y, text, width=10, bg='red', fg='white', relief='raised'):
        # Create the remaining buttons at the bottom of the payroll page
        button = Button(self.window, width=width, text=text, bg=bg, fg=fg, cursor='hand2', border=2, relief='solid')
        button.place(x=x, y=y)
        return button

    def create_image(self, image_path, x, y, width, height):
        # Function to display the 'no_profile.jpg' image
        image = Image.open(image_path)
        resized_image = ImageTk.PhotoImage(image.resize((width, height)))
        label = Label(self.window, image=resized_image, bg='#f2f0e3', borderwidth=2, relief='solid')
        label.image = resized_image  # Keep a reference to avoid garbage collection
        label.place(x=x, y=y)
        return label