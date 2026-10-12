from tkinter import * 


def create_interface():
    interface = Tk()
    interface.title("Hospital Manager")
    interface.geometry("600x600")
    title = Label(interface, text="Hospital Manager", font=("Arial", 24, "bold"))
    title.pack()
    return interface

