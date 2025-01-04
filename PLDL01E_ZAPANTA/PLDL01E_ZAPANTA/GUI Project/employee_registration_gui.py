import tkinter as tk
from tkinter import ttk # Import the ttk module from the tkinter library
from PIL import Image, ImageTk  # Import the Image and ImageTk modules from the PIL library

class EmployeeRegistrationGUI:
    def __init__(self, window):
        self.window = window
        self.window.title('Employee Registration')
        self.window.geometry("900x800")
        self.window.configure(bg='#f2f0e3')

        # Heading
        self.heading = tk.Label(self.window,
                                text="Se-Ri's Employee's Personal Information",
                                fg='black',
                                bg='#f2f0e3',
                                font=('Times New Roman', 22, 'bold'))
        self.heading.pack(pady=20)

        # Frames
        self.create_frames()

        # Image
        self.load_image()

        # Labels and Textboxes in Frame 1
        self.create_frame1_widgets()

        # Labels and Textboxes in Frame 2
        self.create_frame2_widgets()

        # Labels and Textboxes in Frame 3
        self.create_frame3_widgets()

        # Labels and Textboxes in Frame 4
        self.create_frame4_widgets()

        # Buttons
        self.create_buttons()

        # Combo boxes
        self.create_comboboxes()

    def create_frames(self):
        """Create and place frames in the window."""
        self.frame1 = self.create_frame(50, 80, 800, 130)
        self.frame2 = self.create_frame(50, 220, 800, 130)
        self.frame3 = self.create_frame(50, 380, 800, 110)
        self.frame4 = self.create_frame(50, 520, 800, 220)

    def create_frame(self, x, y, width, height):
        """Helper function to create a frame."""
        frame = tk.Frame(self.window, width=width, height=height, bg='#f8f3f3', relief='raised', borderwidth=5)
        frame.place(x=x, y=y)
        return frame

    def load_image(self):
        """Load and display the profile image."""
        self.image = Image.open("no_profile.jpg")
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((120, 120)))
        self.profile_icon = tk.Label(self.window, image=self.bck_pic, borderwidth=2, relief='solid')
        self.profile_icon.place(x=60, y=25)

    def create_frame1_widgets(self):
        """Create and place widgets in frame 1."""
        self.create_label(self.window, "No File Chosen", 75, 182)
        self.create_label(self.window, "First Name", 200, 90)
        self.create_label(self.window, "Middle Name", 390, 90)
        self.create_label(self.window, "Last Name", 520, 90)
        self.create_label(self.window, "Suffix", 710, 90)
        self.create_label(self.window, "Date of Birth", 200, 140)
        self.create_label(self.window, "Gender", 420, 140)
        self.create_label(self.window, "Nationality", 550, 140)
        self.create_label(self.window, "Civil Status", 680, 140)

        self.create_entry(self.window, 30, 200, 110)
        self.create_entry(self.window, 20, 390, 110)
        self.create_entry(self.window, 30, 520, 110)
        self.create_entry(self.window, 20, 710, 110)
        self.create_entry(self.window, 20, 420, 160)
        self.create_entry(self.window, 20, 550, 160)
        self.create_entry(self.window, 25, 680, 160)

    def create_frame2_widgets(self):
        """Create and place widgets in frame 2."""
        self.create_label(self.window, "Department", 75, 230)
        self.create_label(self.window, "Designation", 387, 230)
        self.create_label(self.window, "Qualified Dep. Status", 610, 230)
        self.create_label(self.window, "Employee Status", 75, 280)
        self.create_label(self.window, "Pay Date", 448, 280)
        self.create_label(self.window, "Employee Number", 610, 280)

        self.create_entry(self.window, 50, 75, 250)
        self.create_entry(self.window, 35, 387, 250)
        self.create_entry(self.window, 37, 610, 250)
        self.create_entry(self.window, 60, 75, 300)
        self.create_entry(self.window, 25, 448, 300)
        self.create_entry(self.window, 37, 610, 300)

    def create_frame3_widgets(self):
        """Create and place widgets in frame 3."""
        self.create_label(self.window, "Contact Info:", 50, 355, font=('Times New Roman', 12, 'bold'))
        self.create_label(self.window, "Contact No.", 75, 390)
        self.create_label(self.window, "Email", 390, 390)
        self.create_label(self.window, "Other(Social Media)", 75, 435)
        self.create_label(self.window, "Social Media Account ID/No.", 390, 435)

        self.create_entry(self.window, 50, 75, 410)
        self.create_entry(self.window, 73, 390, 410)
        self.create_entry(self.window, 50, 75, 455)
        self.create_entry(self.window, 73, 390, 455)

    def create_frame4_widgets(self):
        """Create and place widgets in frame 4."""
        self.create_label(self.window, "Address:", 50, 495, font=('Times New Roman', 12, 'bold'))
        self.create_label(self.window, "Address Line 1", 75, 525)
        self.create_label(self.window, "Address Line 2", 75, 565)
        self.create_label(self.window, "City/Municipality", 75, 605)
        self.create_label(self.window, "State/Province", 458, 605)
        self.create_label(self.window, "Country", 75, 643)
        self.create_label(self.window, "Zip Code", 458, 643)
        self.create_label(self.window, "Picture Path", 75, 680)

        self.create_entry(self.window, 126, 75, 545)
        self.create_entry(self.window, 126, 75, 585)
        self.create_entry(self.window, 62, 75, 625)
        self.create_entry(self.window, 62, 458, 625)
        self.create_entry(self.window, 62, 75, 663)
        self.create_entry(self.window, 62, 458, 663)
        self.create_entry(self.window, 126, 75, 700)

    def create_buttons(self):
        """Create and place buttons in the window."""
        self.create_button(self.window, 'Choose File', 63, 150)
        self.create_button(self.window, 'Save', 50, 750, bg='#007bff', fg='white')
        self.create_button(self.window, 'Cancel', 160, 750)

    def create_comboboxes(self):
        """Create and place combo boxes in the window."""
        self.create_combobox(self.window, [str(i) for i in range(1, 32)], 5, 200, 160) # Days
        self.create_combobox(self.window, ['January', 'February', 'March', 'April', 'May',
                                           'June', 'July', 'August', 'September', 'October',
                                           'November', 'December'], 10, 260, 160) # Months
        self.create_combobox(self.window, [str(i) for i in range(1900, 2026)], 7, 350, 160) # Years

        self.create_combobox(self.window, ['Male', 'Female'], 17, 422, 160) # Gender
        self.create_combobox(self.window, ['Single', 'Married', 'Widow',
                                           'Divorced', 'Annulled'], 22, 680, 160) # Civil Status

        self.create_combobox(self.window, ['American', 'Argentinian', 'Australian', 'Bangladeshi',
                                           'Brazilian', 'British', 'Canadian', 'Chilean', 'Chinese', 'Colombian',
                                           'Dutch', 'Egyptian', 'Filipino', 'French', 'German', 'Greek', 'Indian',
                                           'Indonesian', 'Iraqi', 'Italian', 'Japanese', 'Kenyan', 'Korean',
                                           'Malaysian', 'Mexican', 'Nigerian', 'Pakistani', 'Peruvian', 'Polish',
                                           'Portuguese', 'Russian', 'Singaporean', 'South African', 'Spanish',
                                           'Sri Lankan', 'Swedish', 'Thai', 'Turkish', 'Ukrainian',
                                           'Venezuelan', 'Vietnamese'], 17, 550, 160) # Nationalities

        self.create_combobox(self.window, ['Facebook', 'Instagram', 'Twitter', 'Youtube',
                                           'Tiktok', 'Snapchat', 'Pinterest', 'Messenger',
                                           'Telegram', 'Twitch'], 47, 75, 455) # Social Media
        self.create_combobox(self.window, ['Brazil', 'Cambodia', 'China', 'Indonesia', 'Japan',
                                           'Russia', 'Philippines', 'Poland', 'Portugal', 'South Korea',
                                           'Thailand', 'United States', 'Vietnam'], 59, 75, 663) # Countries

    def create_label(self, parent, text, x, y, font=('Arial', 10)):
        """Helper function to create a label."""
        label = tk.Label(parent, text=text, bg='#f8f3f3', font=font)
        label.place(x=x, y=y)

    def create_entry(self, parent, width, x, y, font=('Arial', 8)):
        """Helper function to create an entry."""
        entry = ttk.Entry(parent, width=width, font=font)
        entry.place(x=x, y=y)

    def create_button(self, parent, text, x, y, bg='white', fg='black'):
        """Helper function to create a button."""
        button = tk.Button(parent, text=text, width=10, padx=10, bg=bg, fg=fg, cursor='hand2', border=5)
        button.place(x=x, y=y)

    def create_combobox(self, parent, values, width, x, y):
        """Helper function to create a combobox."""
        combobox = ttk.Combobox(parent, width=width)
        combobox['values'] = values
        combobox.place(x=x, y=y)
        combobox.current()