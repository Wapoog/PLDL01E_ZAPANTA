import tkinter as tk
from login_gui import LoginGUI  # Import the LoginGUI class from the login_gui module


def main():
    # Create the main application window
    root = tk.Tk()

    # Initialize the LoginGUI class with the root window
    _app = LoginGUI(root)

    # Start the Tkinter event loop
    root.mainloop()


# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()