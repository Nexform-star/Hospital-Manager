from tkinter import * 
from tkinter import messagebox
import sqlite3
from tkinter import ttk



def open_patient_list():
    patients_list_window = Toplevel()
    patients_list_window.title("Patient List")
    patients_list_window.geometry("700x450")
    patients_list_window.configure(bg="#F3F6FA")

    title = Label(
        patients_list_window,
        text="Registered Patients",
        font=("Arial", 20, "bold"),
        fg="#163B65",
        bg="#F3F6FA"
    )
    title.pack(pady=20)

    columns = ("id", "first_name", "last_name", "age")

    patients_table = ttk.Treeview(
        patients_list_window,
        columns=columns,
        show="headings"
    )

    patients_table.heading("id", text="ID")
    patients_table.heading("first_name", text="First Name")
    patients_table.heading("last_name", text="Last Name")
    patients_table.heading("age", text="Age")

    patients_table.pack(fill="both", expand=True, padx=20, pady=10)

    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, first_name, last_name, age FROM patients"
    )
    patients = cursor.fetchall()
    conn.close()

    for patient in patients:
        patients_table.insert("", END, values=patient)


def button_patients_func():
    patients_window = Toplevel()
    patients_window.title("Patients")
    patients_window.geometry("600x400")
    patients_window.configure(bg="#F3F6FA")

    patients_title = Label(
        patients_window,
        text="Patient Management",
        font=("Arial", 20, "bold"),
        fg="#163B65",
        bg="#F3F6FA"
    )
    patients_title.pack(pady=20)

    first_name_label = Label(
        patients_window,
        text="First name",
        font=("Arial", 11),
        bg="#F3F6FA"
    )
    first_name_label.pack(anchor="w", padx=40)

    first_name_entry = Entry(patients_window, font=("Arial", 12))
    first_name_entry.pack(fill="x", padx=40, pady=(5, 15))

    last_name_label = Label(
        patients_window,
        text="Last name",
        font=("Arial", 11),
        bg="#F3F6FA"
    )
    last_name_label.pack(anchor="w", padx=40)

    last_name_entry = Entry(patients_window, font=("Arial", 12))
    last_name_entry.pack(fill="x", padx=40, pady=(5, 15))

    age_label = Label(
        patients_window,
        text="Age",
        font=("Arial", 11),
        bg="#F3F6FA"
    )
    age_label.pack(anchor="w", padx=40)

    age_entry = Entry(patients_window, font=("Arial", 12))
    age_entry.pack(fill="x", padx=40, pady=(5, 15))
    
    def add_patient():
        first_name = first_name_entry.get().strip()
        last_name = last_name_entry.get().strip()
        age = age_entry.get().strip()

        if not first_name or not last_name or not age:
            messagebox.showwarning(
                "Missing information",
                "Please fill in all fields."
            )
            return

        if not age.isdigit():
            messagebox.showerror(
                "Invalid age",
                "Age must be a number."
            )
            return

        if int(age) > 130:
            messagebox.showerror(
                "Invalid age",
                "Please enter a valid age."
            )
            return


        conn = sqlite3.connect("hospital.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO patients (first_name, last_name, age) VALUES (?, ?, ?)",
            (first_name, last_name, int(age))
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Patient added",
            f"{first_name} {last_name} has been saved!"
        )

        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        age_entry.delete(0, END)


    add_button = Button(
        patients_window,
        text="Add Patient",
        command=add_patient,
        bg="#2563EB",
        fg="white",
        font=("Arial", 12, "bold"),
        relief="flat",
        cursor="hand2"
    )
    add_button.pack(pady=10, ipadx=20, ipady=5)
    
    view_patients_button = Button(
        patients_window,
        text="View Patients",
        command=open_patient_list,
        bg="#163B65",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    )
    view_patients_button.pack(pady=5, ipadx=15, ipady=5)



def init_database():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def open_appointments():
    messagebox.showinfo("Hospital Manager", "Appointments section coming soon!")

def open_staff():
    messagebox.showinfo("Hospital Manager", "Staff section coming soon!")


def create_interface():
    init_database()
    interface = Tk()
    interface.title("Hospital Manager")
    interface.geometry("1000x650")
    main_frame = Frame(interface, bg="#F3F6FA")
    title = Label(main_frame, text="Hospital Manager", font=("Arial", 24, "bold"), fg="#163B65", bg="#F3F6FA")
    title.pack(anchor="w", padx=20, pady=20)
    sub_title_label = Label(main_frame, text="Hospital overview", font=("Arial", 14, "bold"), fg="#64748B", bg="#F3F6FA")
    sub_title_label.pack(anchor="w", padx=20, pady=(0, 20))
    patients_card = Frame(main_frame, bg="white", height=120, width=220, highlightbackground="#DCE4EE", highlightthickness=1)
    patients_card.pack_propagate(False)
    label_patients_card = Label(patients_card, text="Total Patients", font=("Arial", 12, "bold"), fg="#2563EB", bg="white")
    label_patients_card.pack(pady=10)
    patients_card.pack(side="left", padx=20)
    appointments_card = Frame(main_frame, bg="white", width=220, height=120, highlightbackground="#DCE4EE", highlightthickness=1)
    appointments_card.pack(side="left", padx=20)
    appointments_card.pack_propagate(False)
    label_appointments_card = Label(appointments_card, text="Upcoming Appointments", font=("Arial", 12, "bold"), fg="#2563EB", bg="white")
    label_appointments_card.pack(pady=10)
    patients_count = Label(patients_card, text="128", font=("Arial", 22, "bold"), fg="#2563EB", bg="white")
    patients_count.pack(pady=5)
    appointments_count = Label(appointments_card, text="24", bg="white", fg="#2563EB", font=("Arial", 22, "bold"))
    appointments_count.pack(pady=5)
    staff_card = Frame(main_frame, bg="white", width=220, height=120, highlightbackground="#DCE4EE", highlightthickness=1)
    staff_card.pack(side="left", padx=20)
    staff_card_label = Label(staff_card, bg="white", text="Staff Members", font=("Arial", 12, "bold"), fg="#2563EB")
    staff_card_label.pack(pady=10)
    staff_count = Label(staff_card, text="56", font=("Arial", 22, "bold"), fg="#2563EB", bg="white")
    staff_count.pack(pady=5)
    staff_card.pack_propagate(False)
    frame = Frame(interface, bg="#163B65", width=200)
    frame.pack(side="left", fill="y")
    frame.pack_propagate(False)
    dashboard_button = Button(frame, text="Dashboard", bg="#245584", fg="white", font=("Arial", 12, "bold"), relief="flat", activebackground="#245584", activeforeground="white", cursor="hand2")
    dashboard_button.pack(pady=5, fill="x", ipady=8)
    main_frame.pack(side="left", fill="both", expand=True)
    button_patients = Button(frame, text="Patients", command=button_patients_func, bg="#163B65", fg="white", font=("Arial", 12, "bold"), relief="flat", activebackground="#245584", activeforeground="white", cursor="hand2")
    appointment_button = Button(frame, text="Appointment", command=open_appointments, bg="#163B65", fg="white", font=("Arial", 12, "bold"), relief="flat", activebackground="#245584", activeforeground="white", cursor="hand2")
    staff_button = Button(frame, text="Staff", command=open_staff, bg="#163B65", fg="white", font=("Arial", 12, "bold"), relief="flat", activebackground="#245584", activeforeground="white", cursor="hand2")
    staff_button.pack(fill="x", pady=5, ipady=8)
    appointment_button.pack(fill="x", pady=5, ipady=8)
    button_patients.pack(fill="x", pady=5, ipady=8)
    return interface 

