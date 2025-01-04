import tkinter as tk
from employee_registration_gui import EmployeeRegistrationGUI  # Import the EmployeeRegistrationGUI class


def main():
    # Create the main application window
    window = tk.Tk()

    # Initialize the EmployeeRegistrationGUI class with the main window
    _app = EmployeeRegistrationGUI(window)

    # Start the Tkinter event loop
    window.mainloop()


# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()
