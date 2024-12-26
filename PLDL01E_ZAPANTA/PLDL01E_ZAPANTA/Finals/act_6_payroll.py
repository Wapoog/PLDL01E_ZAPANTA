import tkinter as tk
from tkinter import ttk
from payroll_gui import PayrollGUI

def main():
    window = tk.Tk()
    gui = PayrollGUI(window)

    # Heading
    gui.create_label(x=260, y=20, text="SE-RI'S CHOICE PAYROLL", font=('Times New Roman', 30, 'bold'))

    # Employee Basic Info Labels
    gui.create_label(x=40, y=290, text='Employee Number')
    gui.create_label(x=40, y=330, text='Search Employee')
    gui.create_label(x=40, y=360, text='Department')
    gui.create_label(x=450, y=120, text='First Name')
    gui.create_label(x=450, y=150, text='Middle Name')
    gui.create_label(x=450, y=180, text='Surname')
    gui.create_label(x=450, y=210, text='Civil Status')
    gui.create_label(x=450, y=240, text='Qualified Dependents Status')
    gui.create_label(x=450, y=270, text='Pay Date')
    gui.create_label(x=450, y=300, text='Employee Status')
    gui.create_label(x=450, y=330, text='Designation')

    # Employee Basic Info Textboxes
    gui.create_textbox(x=180, y=290)
    gui.create_textbox(x=180, y=360)
    gui.create_textbox(x=640, y=120)
    gui.create_textbox(x=640, y=150)
    gui.create_textbox(x=640, y=180)
    gui.create_textbox(x=640, y=210)
    gui.create_textbox(x=640, y=240)
    gui.create_textbox(x=640, y=270)
    gui.create_textbox(x=640, y=300)
    gui.create_textbox(x=640, y=330)

    # Basic Income Labels
    gui.create_label(x=40, y=440, text='Rate / Hour')
    gui.create_label(x=40, y=470, text='No. of Hours / Cut Off')
    gui.create_label(x=40, y=500, text='Income / Cut Off')

    # Basic Income Textboxes
    gui.create_textbox(x=180, y=440)
    gui.create_textbox(x=180, y=470)
    gui.create_textbox(x=180, y=500)

    # Honorarium Income Labels
    gui.create_label(x=40, y=580, text='Rate / Hour')
    gui.create_label(x=40, y=610, text='No. of Hours / Cut Off')
    gui.create_label(x=40, y=640, text='Income / Cut Off')

    # Honorarium Income Textboxes
    gui.create_textbox(x=180, y=580)
    gui.create_textbox(x=180, y=610)
    gui.create_textbox(x=180, y=640)

    # Other Income Labels
    gui.create_label(x=40, y=720, text='Rate / Hour')
    gui.create_label(x=40, y=750, text='No. of Hours / Cut Off')
    gui.create_label(x=40, y=780, text='Income / Cut Off')

    # Other Income Textboxes
    gui.create_textbox(x=180, y=710)
    gui.create_textbox(x=180, y=740)
    gui.create_textbox(x=180, y=770)

    # Summary Income Labels
    gui.create_label(x=40, y=860, text='GROSS INCOME')
    gui.create_label(x=40, y=890, text='NET INCOME')

    # Summary Income Textboxes
    gui.create_textbox(x=180, y=860)
    gui.create_textbox(x=180, y=890)

    # Regular Deductions Labels
    gui.create_label(x=450, y=410, text='SSS Contribution')
    gui.create_label(x=450, y=440, text='PhilHealth Contribution')
    gui.create_label(x=450, y=470, text='Pagibig Contribution')
    gui.create_label(x=450, y=500, text='Income Tax Contribution')

    # Regular Deductions Textboxes
    gui.create_textbox(x=640, y=410)
    gui.create_textbox(x=640, y=440)
    gui.create_textbox(x=640, y=470)
    gui.create_textbox(x=640, y=500)

    # Other Deductions Labels
    gui.create_label(x=450, y=580, text='SSS Loan')
    gui.create_label(x=450, y=610, text='Pagibig Loan')
    gui.create_label(x=450, y=640, text='Faculty Savings Deposit')
    gui.create_label(x=450, y=670, text='Faculty Savings Loan')
    gui.create_label(x=450, y=700, text='Salary Loan')
    gui.create_label(x=450, y=730, text='Other Loan')

    # Other Deductions Textboxes
    gui.create_textbox(x=640, y=580)
    gui.create_textbox(x=640, y=610)
    gui.create_textbox(x=640, y=640)
    gui.create_textbox(x=640, y=670)
    gui.create_textbox(x=640, y=700)
    gui.create_textbox(x=640, y=730)

    # Deduction Summary Label
    gui.create_label(x=450, y=810, text='Total Deduction')

    # Deduction Summary Textbox
    gui.create_textbox(x=640, y=810, bg='light gray')

    # Section Labels
    gui.create_label(x=30, y=100, text='EMPLOYEE BASIC INFO:', font=('Arial', 12, 'bold'))
    gui.create_label(x=30, y=400, text='BASIC INCOME:', font=('Arial', 12, 'bold'))
    gui.create_label(x=30, y=540, text='HONORARIUM INCOME:', font=('Arial', 12, 'bold'))
    gui.create_label(x=30, y=680, text='OTHER INCOME:', font=('Arial', 12, 'bold'))
    gui.create_label(x=30, y=820, text='SUMMARY INCOME:', font=('Arial', 12, 'bold'))
    gui.create_label(x=430, y=370, text='REGULAR DEDUCTIONS:', font=('Arial', 12, 'bold'))
    gui.create_label(x=430, y=540, text='OTHER DEDUCTIONS:', font=('Arial', 12, 'bold'))
    gui.create_label(x=430, y=770, text='DEDUCTION SUMMARY:', font=('Arial', 12, 'bold'))

    # Buttons
    gui.create_button1(x=180, y=320, text='SEARCH')
    gui.create_button(x=430, y=870, text='GROSS INCOME', bg='#007bff')
    gui.create_button(x=525, y=870, text='NET INCOME', bg='#007bff')
    gui.create_button(x=620, y=870, text='SAVE', bg='#17a2b8', fg='black')
    gui.create_button(x=695, y=870, text='UPDATE', bg='#17a2b8', fg='black')
    gui.create_button(x=775, y=870, text='NEW', bg='#ffc107', fg='black')

    # Combo Box for Civil Status
    civil_status = tk.StringVar()
    civil_status_combo = ttk.Combobox(window, width=34, textvariable=civil_status)
    civil_status_combo['values'] = (' Single', ' Married', ' Widow', ' Divorced', ' Annulled')
    civil_status_combo.place(x=640, y=210)
    civil_status_combo.current()

    # Profile Image
    gui.create_image(image_path='no_profile.jpg', x=40, y=130, width=150, height=145)

    window.mainloop()

if __name__ == '__main__':
    main()