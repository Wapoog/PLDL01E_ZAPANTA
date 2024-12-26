import tkinter as tk
from tkinter import ttk
from meralco_gui import MeralcoGUI

def main():
    window = tk.Tk()
    gui = MeralcoGUI(window)

    # Labels for left column
    gui.create_label1(x=20, y=20, text='JUAN DELA CRUZ')
    gui.create_label1(x=20, y=40, text='123 MALIWANAG STREET, BARANGAY KAUNLARAN')
    gui.create_label1(x=20, y=60, text='STA. LUCIA MANILA')
    gui.create_label1(x=20, y=100, text='CORINTHIAN EXECUTIVE REGENCY')
    gui.create_label1(x=20, y=120, text='Meter No.: 123AB456789')
    gui.create_label1(x=20, y=140, text='Route Seq.: 1234 56 7890\tPrint Seq.: 12345')
    gui.create_label2(x=20, y=180, text='Your electric bill')
    gui.create_label3(x=20, y=218, text='Billing Period')
    gui.create_label4(x=20, y=238, text='07 Sep 2021 to 06 Oct 2021')
    gui.create_label3(x=280, y=218, text='Bill Date')
    gui.create_label4(x=280, y=238, text='06 Oct 2021')
    gui.create_separator1(20, 265)
    gui.create_label3(x=20, y=280, text='Date of Meter Reading')
    gui.create_label4(x=20, y=300, text='06 Oct 2021')
    gui.create_label3(x=20, y=340, text='Date of Next Meter Reading')
    gui.create_label4(x=20, y=360, text='06 Nov 2021')
    gui.create_label3(x=20, y=400, text='Customer Type')
    gui.create_label4(x=20, y=420, text='Residential')
    gui.create_label3(x=20, y=460, text='Your rate this month')
    gui.create_label4(x=20, y=480, text='Php 8.59 kWh')
    gui.create_label3(x=280, y=280, text='Electric Meter Number')
    gui.create_label4(x=280, y=300, text='123AB456789')
    gui.create_square(x=235, y=345)
    gui.create_label3(x=280, y=340, text='Current Reading')
    gui.create_label4(x=280, y=360, text='3,055')
    gui.create_square(x=235, y=405)
    gui.create_label5(x=245, y=406, text='-')
    gui.create_label3(x=280, y=400, text='Previous Reading')
    gui.create_label4(x=280, y=420, text='2,855')
    gui.create_square(x=235, y=470)
    gui.create_label5(x=243, y=474, text='=')
    gui.create_label3(x=280, y=460, text='Actual Consumption')
    gui.create_label4(x=280, y=480, text='200 kWh')

    # labels and frame for right column
    gui.create_label1(x=460, y=20, text='ESPANA-TUTUBAN BUSINESS CENTER')
    gui.create_label1(x=460, y=40, text='LUBIRAN STREET BACOOD, STA. MESA')
    gui.create_label1(x=460, y=60, text='MANILA, 1016 METRO MANILA')
    gui.create_label1(x=460, y=80, text='TIN 000-101-528-000-VAT')
    gui.create_label1(x=460, y=120, text='Invoice No.: 1234567890123')
    gui.create_frame1(x=460, y=200)
    gui.create_label6(x=470, y=210, text='Customer Account Number (CAN)')
    gui.create_label7(x=470, y=230, text='1234567890')
    gui.create_label6(x=750, y=210, text='Due Date')
    gui.create_label7(x=750, y=230, text='17 Oct 2021')
    gui.create_frame2(x=472, y=275)
    gui.create_label6(x=480, y=280, text='Please Pay')
    gui.create_label8(x=480, y=320, text='Php 3,364.00')

    # meralco logo
    gui.create_image(image_path='Meralco_Logo.png', x=705, y=20, width=160, height=140)

    window.mainloop()


if __name__ == '__main__':
    main()