import tkinter as tk
from tkinter import ttk # Import ttk module
from PIL import Image, ImageTk # Import Image and ImageTk modules from PIL

class LoginGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("390x550") # Set the window size
        self.root.configure(bg='#f2f0e3')

        self.load_image() # Load the image
        self.configure_styles() # Configure styles for ttk widgets
        self.create_image_label() # Create a Label widget to display the image
        self.create_login_form() # Create a frame for the login form with additional padding at the top

    def load_image(self):
        # Load the image
        self.photo = Image.open("profile_circle.png")
        self.photo = self.photo.resize((150, 150))
        self.icon = ImageTk.PhotoImage(self.photo)

    def configure_styles(self):
        # Style configuration
        style = ttk.Style()
        style.configure('TFrame', background='#f8f3f3', relief='raised', borderwidth=10)
        style.configure('TLabel', background='#f8f3f3', foreground='black', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TButton', background='#3498db', foreground='black', font=('Arial', 12, 'bold'))

    def create_image_label(self):
        # Create a Label widget to display the image
        self.image_label = tk.Label(self.root, image=self.icon, bg='#f2f0e3', borderwidth=2, relief='solid')
        self.image_label.grid(row=0, column=0, columnspan=2, pady=(50, 20))

    def create_login_form(self):
        # Create a frame for the login form with additional padding at the top
        self.frame = ttk.Frame(self.root, padding="20 20 20 20")
        self.frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky=tk.NSEW)

        # Username label and entry
        self.username_label = ttk.Label(self.frame, text="Username:")
        self.username_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.username_entry = ttk.Entry(self.frame, width=35)
        self.username_entry.grid(row=0, column=1, pady=5)

        # Password label and entry
        self.password_label = ttk.Label(self.frame, text="Password:")
        self.password_label.grid(row=1, column=0, sticky=tk.W, pady=5)

        # Frame for password entry and eye icon
        self.password_frame = ttk.Frame(self.frame)
        self.password_frame.grid(row=1, column=1, sticky=tk.W)

        # Password entry
        self.password_entry = ttk.Entry(self.password_frame, width=30, show="*")
        self.password_entry.grid(row=0, column=0)

        # Load eye icon
        self.eye_icon = Image.open("eye_icon.png")
        self.eye_icon = self.eye_icon.resize((15, 15))
        self.eye_icon = ImageTk.PhotoImage(self.eye_icon)

        # Eye button to toggle password visibility
        self.show_password_button = ttk.Button(self.password_frame, image=self.eye_icon, command=self.toggle_password)
        self.show_password_button.grid(row=0, column=1, padx=5)

        # Login button
        self.login_button = ttk.Button(self.frame, text="Login")
        self.login_button.grid(row=2, column=1, sticky=tk.E, pady=5)

    def toggle_password(self):
        # Toggle the visibility of the password
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')