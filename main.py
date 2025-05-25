# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
from dateutil.relativedelta import relativedelta
import register
import extra

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.minsize(800, 600)
        self.maxsize(800, 600)
        self.title("Person register in Python")

        frame = ttk.Frame(self)
        frame.pack()

        # Set the initial theme
        self.tk.call("source", "azure.tcl")
        self.tk.call("set_theme", "light")

        lb_title = ttk.Label(master=self, text="Person register in Python", font=("TkDefaultFont", 20))
        lb_title.pack(pady=20)

        btn_list = ttk.Button(master=self, command=self.list_people, text="List registered people")
        btn_list.pack(pady=30)

        btn_register = ttk.Button(master=self, command=self.register_person, text="Register person")
        btn_register.pack(pady=30)

        btn_delete = ttk.Button(master=self, command=self.delete_person, text="Delete person")
        btn_delete.pack(pady=30)

    def list_people(self):
        people = register.load_file()

        list_win = tk.Toplevel()
        list_win.geometry("640x480")
        list_win.minsize(640, 480)
        list_win.maxsize(640, 480)
        list_win.title("List of registered people")

        list_frame = ttk.Frame(list_win)
        list_frame.pack(expand=True, fill=tk.BOTH)

        treeview_list = ttk.Treeview(
            list_frame,
            columns=("Id", "Name", "Gender", "Birth Date", "Age"),
            show="headings"
        )

        treeview_list.heading("Id", text="Id")
        treeview_list.heading("Name", text="Name")
        treeview_list.heading("Gender", text="Gender")
        treeview_list.heading("Birth Date", text="Birth Date")
        treeview_list.heading("Age", text="Age")

        treeview_list.column("Id", width=50, anchor="center")
        treeview_list.column("Name", width=150, anchor="w")
        treeview_list.column("Gender", width=100, anchor="center")
        treeview_list.column("Birth Date", width=120, anchor="center")
        treeview_list.column("Age", width=50, anchor="center")

        for i in sorted(people, key=lambda x: x['name'].lower()):
            treeview_list.insert('', index=tk.END, values=(str(i['id']), i['name'], i['gender'], str(i['birth_date']), str(extra.calculate_age(i['birth_date']))))

        treeview_list.pack(expand=True, fill=tk.BOTH)

    def register_person(self):
        def validate():
            button_register.config(state="disabled")

            if not name.get().strip():
                messagebox.showinfo("Error", "Name cannot be empty!")
                button_register.config(state="normal")
                return
            if not birth_date.get().strip():
                messagebox.showinfo("Error", "Birth date cannot be empty!")
                button_register.config(state="normal")
                return
            if not selected_gender.get().strip():
                messagebox.showinfo("Error", "Gender must be selected!")
                button_register.config(state="normal")
                return

            name_validated = name.get().title()

            try:
                birth_date_formated = datetime.datetime.strptime(birth_date.get(), "%Y-%m-%d").date()
            except ValueError:
                messagebox.showinfo("Error", "Invalid date or this day does not exist. Use YYYY-MM-DD format.")
                button_register.config(state="normal")
                return

            today = datetime.date.today()
            min_date = today - relativedelta(years=120)

            if birth_date_formated < min_date:
                messagebox.showinfo("Error", "Age must be less than 120 years!")
                button_register.config(state="normal")
                return
            if birth_date_formated > today:
                messagebox.showinfo("Error", "The date entered is in the future!")
                button_register.config(state="normal")
                return

            register.register_person(name_validated, selected_gender.get(), birth_date_formated)
            messagebox.showinfo("Success", "Person registered successfully!")

            name.set("")
            birth_date.set("")
            selected_gender.set("")
            name_entry.focus()

            button_register.config(state="normal")

        register_win = tk.Toplevel()
        register_win.geometry("380x480")
        register_win.minsize(380, 480)
        register_win.maxsize(380, 480)
        register_win.title("Register person")
        
        register_frame = ttk.Frame(register_win)
        register_frame.pack(expand=True, fill=tk.BOTH)

        register_title = ttk.Label(register_frame, font=("TkDefaultFont", 16), text="Register person")
        register_title.pack(pady=20)

        name_lb = ttk.Label(register_frame, font=("TkDefaultFont", 10), text="Person's name")
        name_lb.pack(pady=2)

        name = tk.StringVar()

        name_entry = ttk.Entry(register_frame, textvariable=name)
        name_entry.pack(pady=5)
        name_entry.focus()  # Foco só aqui
        
        birthdate_lb = ttk.Label(register_frame, font=("TkDefaultFont", 10), text="Person's birth date (YYYY-MM-DD)")
        birthdate_lb.pack(pady=2)

        birth_date = tk.StringVar()

        birthdate_entry = ttk.Entry(register_frame, textvariable=birth_date)
        birthdate_entry.pack(pady=5)

        gender_lb = ttk.Label(register_frame, font=("TkDefaultFont", 10), text="Person's gender")
        gender_lb.pack(pady=2)
        selected_gender = tk.StringVar()
        gender_opt = ("Male", "Female", "Other/Non Binary")
        
        for gender in gender_opt:
            radiogender = ttk.Radiobutton(register_frame, text=gender, value=gender, variable=selected_gender)
            radiogender.pack(fill="x", padx=5, pady=5)

        button_register = ttk.Button(register_frame, text="Register person", command=validate)
        button_register.pack(pady=20)


    def delete_person(self):
        def validate_id():
            person_id = id.get().strip()
            if not person_id:
                messagebox.INFO("Error", "Id cannot be empty!")
                return
            if not person_id.isdigit():
                messagebox.showinfo("Error", "Id must be a number!")
                return
            
            person_id = int(person_id)
            people = register.load_file()

            if not any(p["id"] == person_id for p in people):
                messagebox.showinfo("Error", f"No person found with ID {person_id}!")
                return
            
            register.delete_person(person_id)
            messagebox.showinfo("Success", f"Person with ID {person_id} found.")


        delete_win = tk.Toplevel()
        delete_win.geometry("240x320")
        delete_win.minsize(240, 320)
        delete_win.maxsize(240, 320)
        delete_win.title("Delete person")

        delete_frame = ttk.Frame(delete_win)
        delete_frame.pack(expand=True, fill=tk.BOTH)
        
        delete_title = ttk.Label(delete_frame, font=("TkDefaultFont", 16), text="Delete person")
        delete_title.pack(pady=20)

        delete_lb = ttk.Label(delete_frame, font=("TkDefaultFont", 10), text="Person's id")
        delete_lb.pack(pady=2)

        id = tk.StringVar()

        id_entry = ttk.Entry(delete_frame, textvariable=id)
        id_entry.pack(pady=5)
        id_entry.focus()

        button_delete = ttk.Button(delete_frame, text="Register person", command=validate_id)
        button_delete.pack(pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()