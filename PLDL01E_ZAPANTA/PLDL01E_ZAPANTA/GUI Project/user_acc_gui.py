import tkinter as tk
from tkinter import ttk # Import ttk module for Combobox
from PIL import Image, ImageTk # Import Image and ImageTk modules from PIL

class UserAccountGUI:
    def __init__(self, root):
        # Initialize the window
        self.root = root
        self.root.title("User Account")
        self.root.geometry("1500x600") # Set the window size
        self.root.configure(bg='#f2f0e3') # Set the window background color

        # Configure styles for ttk widgets
        self.configure_styles()
        # Create header label
        self.create_header()
        # Create main frame for the form
        self.create_frame()
        # Create form with labels and entries
        self.create_form()
        # Create buttons for actions
        self.create_buttons()
        # Create profile icon
        self.create_profile_icon()

    def configure_styles(self):
        # Configure styles for ttk widgets
        style = ttk.Style()
        style.configure('TFrame', bg='#f0f0f0')
        style.configure('TLabel', bg='#f8f3f3', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))

    def create_header(self):
        # Create header label
        self.header = tk.Label(self.root, text="User Account Information", bg='#f2f0e3', font=('Arial', 24))
        self.header.pack(pady=80)

    def create_frame(self):
        # Create main frame for the form
        self.frame = tk.Frame(self.root, width=1300, height=350, bg='#f8f3f3', relief='raised', borderwidth=10)
        self.frame.place(x=100, y=180)

    def create_form(self):
        # Define labels, positions, and entry widths
        labels = ["First Name", "Middle Name", "Last Name", "Suffix", "Department",
                  "Description", "Username", "Password", "Confirm Password", "User Type",
                  "User Status", "Employee Number"]
        positions = [(220, 20), (420, 20), (620, 20), (820, 20), (1020, 20),
                     (220, 100), (530, 100), (860, 100), (50, 200), (350, 200),
                     (650, 200), (950, 200)]
        entry_widths = [25, 25, 25, 25, 25, 40, 40, 40, 35, 35, 35, 35]
        entry_positions = [(220, 50), (420, 50), (620, 50), (820, 50), (1020, 50),
                           (220, 130), (530, 130), (860, 130), (50, 230), (350, 230),
                           (650, 230), (950, 230)]

        self.entries = {}
        # Create labels and entries for the form
        for label, pos, width, entry_pos in zip(labels, positions, entry_widths, entry_positions):
            self.create_label(self.frame, label, pos)
            self.entries[label] = self.create_entry(self.frame, width, entry_pos)

    def create_label(self, parent, text, position):
        # Create a label
        label = ttk.Label(parent, text=text, background='#f8f3f3')
        label.place(x=position[0], y=position[1])

    def create_entry(self, parent, width, position):
        # Create an entry
        entry = ttk.Entry(parent, width=width)
        entry.place(x=position[0], y=position[1])
        return entry

    def create_buttons(self):
        # Define buttons with their properties
        buttons = [("Update", 900, 285, '#007bff', 'white'),
                   ("Delete", 1025, 285, '#ffc107', 'black'),
                   ("Cancel", 1150, 285, None, 'black')]
        # Create buttons
        for text, x, y, bg, fg in buttons:
            self.create_button(self.frame, text, x, y, bg, fg)

    def create_button(self, parent, text, x, y, bg, fg):
        # Create a button
        button = tk.Button(parent, width=10, text=text, bg=bg, fg=fg, font=('Arial', 12))
        button.place(x=x, y=y)

    def create_profile_icon(self):
        # Load and resize profile image
        photo = Image.open("profile_circle.png")
        photo = photo.resize((150, 150))
        icon = ImageTk.PhotoImage(photo)
        # Create label for profile image
        user_icon = tk.Label(self.root, image=icon, bg='#f8f3f3')
        user_icon.image = icon
        user_icon.place(x=135, y=195)