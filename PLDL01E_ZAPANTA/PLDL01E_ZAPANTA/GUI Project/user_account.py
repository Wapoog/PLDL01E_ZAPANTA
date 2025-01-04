import tkinter as tk
from user_acc_gui import UserAccountGUI # Import UserAccountGUI class from user_acc_gui.py

def main():
    # Create the main window
    root = tk.Tk()
    # Initialize the UserAccountGUI with the main window
    _app = UserAccountGUI(root)
    # Run the main loop to keep the window open
    root.mainloop()

if __name__ == "__main__":
    # Entry point of the program
    main()