from tkinter import *
from tkinter import messagebox
from interface import create_interface


def button_patients_func():
    messagebox.showinfo("Hospital Manager", "Patient section coming soon!")

def open_appointments():
    messagebox.showinfo("Hospital Manager", "Appointments section coming soon!")

def open_staff():
    messagebox.showinfo("Hospital Manager", "Staff section coming soon!")

interface = create_interface()
button_patients = Button(interface, text="Patients", command=button_patients_func)
appointment_button = Button(interface, text="Appointment", command=open_appointments)
staff_button = Button(interface, text="Staff", command=open_staff)
staff_button.pack()
appointment_button.pack()
button_patients.pack()

interface.mainloop()
