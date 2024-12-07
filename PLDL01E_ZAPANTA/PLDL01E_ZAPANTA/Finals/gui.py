import tkinter as tk
from tkinter import *
from PIL import image, imageTk

window = tk.tk()
window.title("Payroll System")
image = Image.open()
bck_pic = ImageTk.PhotoImage(image.resize((1540,900)))
lbl = Label(window, image=bck_pic)
lbl.place(x=1, y=1)

frame=Frame(window, width=300, height=300, bg='floral white').place(x=190, y=450)

heading = Label(frame, text='sign in', fg='navy blue', bg="white", font=('Calibre', 21, 'bold'))
heading.place (x=190, y=450)

#user section
username=Entry(frame, width=25, fg='black', border=2, bg="white", font=('Arial', 11, "bold"))
username.place(x=270, y=500)
username.insert(0, 'Username')
Frame(frame, width=210, height=2, bg="black").place(x=268, y=530)

#password section
password=Entry(frame, width=25, fg='black', border=2, bg='white', font=('Arial', 11, 'bold'))
password.place(x=270, y=570)
password.insert(0, 'Password')

Frame(frame, width=210, height=2, bg='black').place(x=268, y=600)

#button section
Button(frame, width=25, pady=7, text='Sign in', bg='#57a1f8', fg='white', cursor='hand2', border=0).place(x=275, y=630)
label= Label(frame, text='Dont have an account?', fg='black', bg='white', cursor='hand2', font=('Calibre', 9))
label.place(x=250, y=710)

sign_up = Button(frame, width=6, text='sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8').place(x=410, y=710)


window.geometry('1540x900')
window.mainloop()