import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

        self.geometry("1200x800")
        self.title("DriveStats")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title = ctk.CTkLabel(self, text="DriveStats", text_color="white", font= ("Segoe UI", 70))
        self.title.pack()

        self.created_by = ctk.CTkLabel(self, text="created by Matteo Dagostino", text_color="white", font= ("Segoe UI", 20))
        self.created_by.pack()

        self.car_name_label = ctk.CTkLabel(self, text="Car Name:", text_color="white", font=("Segoe UI", 20))
        self.car_name_label.pack(pady=(50,0))
        self.car_name_entry = ctk.CTkEntry(self)
        self.car_name_entry.pack()

        self.expense_type_label = ctk.CTkLabel(self, text="Expense Type:", text_color="white", font=("Segoe UI", 20))
        self.expense_type_label.pack()
        self.expense_type_entry = ctk.CTkEntry(self)
        self.expense_type_entry.pack()

        self.expense_amount_label = ctk.CTkLabel(self, text="Expense Amount:", text_color="white", font=("Segoe UI", 20))
        self.expense_amount_label.pack()
        self.expense_amount_entry = ctk.CTkEntry(self)
        self.expense_amount_entry.pack()

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.button_event)
        self.submit_button.pack()

    def button_event(self):
        car_name = self.car_name_entry.get()
        expense_type = self.expense_type_entry.get()
        expense_amount = self.expense_amount_entry.get()

        # Process the entered data or perform further actions

        # Clear the entry fields
        self.car_name_entry.delete(0, ctk.END)
        self.expense_type_entry.delete(0, ctk.END)
        self.expense_amount_entry.delete(0, ctk.END)

        print("Car Name:", car_name)
        print("Expense Type:", expense_type)
        print("Expense Amount:", expense_amount)



app = App()
app.mainloop()