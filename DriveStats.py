import customtkinter as ctk

class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

        self.geometry("800x700")
        self.title("DriveStats")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text="DriveStats Dashboard", font=("Segoe UI", 36, "bold"))
        self.title_label.pack(pady=(20,0))
        self.created_by = ctk.CTkLabel(self, text="created by Matteo Dagostino", font= ("Segoe UI", 20))
        self.created_by.pack(pady=(0,40))


        self.mileage_economy_frame = ctk.CTkFrame(self, corner_radius=20, border_width=5)
        self.mileage_economy_frame.pack(pady=(0, 30), padx=80, fill="x")

        self.mileage_frame = ctk.CTkFrame(self.mileage_economy_frame, corner_radius=20, border_width=1)
        self.mileage_frame.grid(row=0,column=0,padx=20, pady= 20)
        self.mileage_label = ctk.CTkLabel(self.mileage_frame, text="Current Mileage:", font=("Segoe UI", 18, "bold"))
        self.mileage_label.pack(side="top", padx=(20, 20), pady=(10, 0))
        self.mileage_value_label = ctk.CTkLabel(self.mileage_frame, text="87000 km", font=("Segoe UI", 24))
        self.mileage_value_label.pack(side="top", pady=(0,10))

        self.economy_frame = ctk.CTkFrame(self.mileage_economy_frame, corner_radius=20, border_width=1)
        self.economy_frame.grid(row=0,column=1,padx=20, pady= 20)
        self.economy_label = ctk.CTkLabel(self.economy_frame, text="Avg. L/100km:", font=("Segoe UI", 18, "bold"))
        self.economy_label.pack(side="top", padx=(20, 20), pady=(10, 0))
        self.economy_value_label = ctk.CTkLabel(self.economy_frame, text="12.5", font=("Segoe UI", 24))
        self.economy_value_label.pack(side="top", pady=(0,10))

        self.last_fill_frame = ctk.CTkFrame(self.mileage_economy_frame, corner_radius=20, border_width=1)
        self.last_fill_frame.grid(row=0,column=2,padx=20, pady= 20)
        self.last_fill_label = ctk.CTkLabel(self.last_fill_frame, text="Last Updated:", font=("Segoe UI", 18, "bold"))
        self.last_fill_label.pack(side="top", padx=(20, 20), pady=(10, 0))
        self.last_fill_value_label = ctk.CTkLabel(self.last_fill_frame, text="2023-07-06", font=("Segoe UI", 24))
        self.last_fill_value_label.pack(side="top", pady=(0,10))

        self.recent_act_frame = ctk.CTkFrame(self, corner_radius=20, border_width=5)
        self.recent_act_frame.pack(pady=(0, 30), padx=80, fill="x")
        self.recent_activity_label = ctk.CTkLabel(self.recent_act_frame, text="Recent Activity:", font=("Segoe UI", 18, "bold"))
        self.recent_activity_label.pack(pady=(20, 10))
        self.recent_activity_text = ctk.CTkTextbox(self.recent_act_frame, width=250, height=10, fg_color="grey", font=("Segoe UI", 12))
        self.recent_activity_text.configure(state='disabled')
        self.recent_activity_text.pack(pady=(0, 20))
        self.recent_activity_show_more = ctk.CTkButton(self.recent_act_frame, text="View All Activity", command=print("All activity requested"), font=("Segoe UI Semibold", 15), cursor="hand2")
        self.recent_activity_show_more.pack(pady = (0,20))

        self.linkedin_frame = ctk.CTkFrame(self, corner_radius=20, border_width=5)
        self.linkedin_frame.pack(pady=(0, 30), padx=80, fill="x")
        self.linkedin_label = ctk.CTkLabel(self.linkedin_frame, text="Connect with me on LinkedIn:", font=("Segoe UI", 18, "bold"))
        self.linkedin_label.pack(pady=(20, 0))
        self.linkedin_link_label = ctk.CTkLabel(self.linkedin_frame, text="www.linkedin.com/in/matteo-dagostino09", text_color="#1AA7EC", font=("Segoe UI", 18))
        self.linkedin_link_label.pack(pady=(0,20))

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=(15, 0))
        self.add_record_button = ctk.CTkButton(self.button_frame, text="+ Add Record", command=self.add_record, font=("Segoe UI Semibold", 20), width=200, height=50)
        self.add_record_button.pack(side="left", padx=(0, 20))
        self.view_report_button = ctk.CTkButton(self.button_frame, text="View Report", command=self.view_report, font=("Segoe UI Semibold", 20), width=200, height=50)
        self.view_report_button.pack(side="left")

    def add_record(self):

        # Create a new Toplevel window for record entry
        record_window = ctk.CTk()
        record_window.title("Add Record")
        record_window.geometry("400x200")

        record_type= ctk.CTkLabel(record_window, text="Record Type:")
        record_type.pack(pady = (10,0))

        button_frame = ctk.CTkFrame(record_window)
        button_frame.pack(pady= 20)

        expense = ctk.CTkButton(button_frame, text= "Expense", command=lambda: print("expense"))
        expense.grid(row=0, column= 0, padx= 10)

        fuelup = ctk.CTkButton(button_frame, text= "Fuel Up", command=lambda: print("fuelup"))
        fuelup.grid(row=0, column= 1, padx= 10)

        record_window.mainloop()

    def view_report(self):
        # Add functionality to view the report
        print("View Report button clicked")


dashboard = Dashboard()
dashboard.mainloop()
