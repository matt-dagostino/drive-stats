import customtkinter as ctk
from tkinter import ttk 
import tkinter as tk
from datetime import date
import sqlite3 as sl

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
        self.recent_activity_show_more = ctk.CTkButton(self.recent_act_frame, text="View All Activity", command=self.view_all_activity, font=("Segoe UI Semibold", 15), cursor="hand2")
        self.recent_activity_show_more.pack(pady = (0,20))

        self.linkedin_frame = ctk.CTkFrame(self, corner_radius=20, border_width=5)
        self.linkedin_frame.pack(pady=(0, 30), padx=80, fill="x")
        self.linkedin_label = ctk.CTkLabel(self.linkedin_frame, text="Connect with me on LinkedIn:", font=("Segoe UI", 18, "bold"))
        self.linkedin_label.pack(pady=(20, 0))
        self.linkedin_link_label = ctk.CTkLabel(self.linkedin_frame, text="www.linkedin.com/in/matteo-dagostino09", text_color="#1AA7EC", font=("Segoe UI", 18))
        self.linkedin_link_label.pack(pady=(0,20))

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=(15, 0))
        self.add_record_button = ctk.CTkButton(self.button_frame, text="+ Add Record", command=self.add_record, font=("Segoe UI Semibold", 20), width=200, height=50, corner_radius=10)
        self.add_record_button.pack(side="left", padx=(0, 20))
        self.view_report_button = ctk.CTkButton(self.button_frame, text="View Report", command=print("View Report"), font=("Segoe UI Semibold", 20), width=200, height=50, corner_radius=10)
        self.view_report_button.pack(side="left")

    def add_record(self):
        # Create a new Toplevel window for record entry
        self.record_window = ctk.CTk()
        self.record_window.title("Add Record")
        self.record_window.geometry("500x300")

        self.record_type= ctk.CTkLabel(self.record_window, text="Record Type:", font=("Segoe UI", 30, "bold"))
        self.record_type.pack(pady = (20,5))

        self.button_frame = ctk.CTkFrame(self.record_window)
        self.button_frame.pack(pady= (20,5))

        self.expense = ctk.CTkButton(self.button_frame, text= "Expense", command=self.add_expense, font=("Segoe UI Semibold", 20), width = 200, height=100)
        self.expense.grid(row=0, column= 0, padx= (20,10), pady= 20)

        self.fuelup = ctk.CTkButton(self.button_frame, text= "Fuel Up", command=self.add_fuelup, font=("Segoe UI Semibold", 20), width = 200, height=100)
        self.fuelup.grid(row=0, column= 1, padx= (10,20), pady= 20)

        self.cancel_button = ctk.CTkButton(self.record_window, text="Cancel", command=self.record_window.destroy, font=("Segoe UI Semibold", 15), fg_color="#FF5555", hover_color= "#ff0021")
        self.cancel_button.pack(side="top", padx=10, pady=20)

        self.record_window.mainloop()

    def add_fuelup(self):
        self.fuelup_window = ctk.CTk()
        self.fuelup_window.title("Add Fuel Up")
        self.fuelup_window.geometry("500x500")

        self.title = ctk.CTkLabel(self.fuelup_window, text="Add Fuel Up", font=("Segoe UI", 25, "bold"))
        self.title.pack(pady=10)

        self.current_mileage_label = ctk.CTkLabel(self.fuelup_window, text="Current Mileage", font=("Segoe UI Semibold", 14))
        self.current_mileage_label.pack(pady=(10,0))
        self.current_mileage_entry = ctk.CTkEntry(self.fuelup_window, placeholder_text="test")
        self.current_mileage_entry.pack()

        self.fuel_price_label = ctk.CTkLabel(self.fuelup_window, text="Fuel Price", font=("Segoe UI Semibold", 14))
        self.fuel_price_label.pack(pady=(10,0))
        self.fuel_price_entry = ctk.CTkEntry(self.fuelup_window, placeholder_text="0.00 $ per L")
        self.fuel_price_entry.pack()

        self.fuel_amount_label = ctk.CTkLabel(self.fuelup_window, text="Fuel Amount", font=("Segoe UI Semibold", 14))
        self.fuel_amount_label.pack(pady=(10,0))
        self.fuel_amount_entry = ctk.CTkEntry(self.fuelup_window, placeholder_text="0.00 L")
        self.fuel_amount_entry.pack()

        self.total_amount_label = ctk.CTkLabel(self.fuelup_window, text="Total Amount", font=("Segoe UI Semibold", 14))
        self.total_amount_label.pack(pady=(10,0))
        self.total_amount_entry = ctk.CTkEntry(self.fuelup_window,  placeholder_text="0.00 $")
        self.total_amount_entry.pack()

        self.date_label = ctk.CTkLabel(self.fuelup_window, text="Date", font=("Segoe UI Semibold", 14))
        self.date_label.pack(pady=(10,0))
        self.date_entry = ctk.CTkEntry(self.fuelup_window, placeholder_text=date.today())
        self.date_entry.pack()

        self.button_frame2 = ctk.CTkFrame(self.fuelup_window, fg_color="transparent")
        self.button_frame2.pack(pady=(15, 0))
        self.cancel_button = ctk.CTkButton(self.button_frame2, text="Cancel", command=self.fuelup_window.destroy, font=("Segoe UI Semibold", 12), fg_color="#FF5555", hover_color= "#ff0021")
        self.cancel_button.pack(side="left", padx=10, pady=20)
        self.save_button = ctk.CTkButton(self.button_frame2, text="Save", command=lambda: save_record(self), font=("Segoe UI Semibold", 12))
        self.save_button.pack(side="left", padx=10, pady=20)

        def save_record(self):
            connect = sl.connect('record_info.db')

            sql = 'INSERT INTO record_info (current_mileage, fuel_price, fuel_amount, total_amount, date) values (?, ?, ?, ? , ?)' 
            data = [(self.current_mileage_entry.get(), self.fuel_price_entry.get(), self.fuel_amount_entry.get(), self.total_amount_entry.get(), self.date_entry.get())]
            with connect:
                connect.executemany(sql, data)
            with connect:
                testing = connect.execute("SELECT * FROM record_info")
                print("Start")
                for row in testing:
                    print(row)
            self.current_mileage_entry.delete(0, 'end')
            self.fuel_price_entry.delete(0, 'end')
            self.fuel_amount_entry.delete(0, 'end')
            self.total_amount_entry.delete(0, 'end')
            self.date_entry.delete(0, 'end')

            connect.close()

        self.fuelup_window.mainloop()


    def add_expense(self):
        # Add functionality to view the report
        print("View Report button clicked")

    def view_all_activity(self):
        
        self.all_activity_frame = ctk.CTk()
        self.all_activity_frame.title("View Data")
        self.all_activity_frame.geometry("1000x450")

        self.title = ctk.CTkLabel(self.all_activity_frame, text="Showing all records...", font=("Segoe UI", 25, "bold"))
        self.title.pack(pady=10)

        self.entry_frame = ctk.CTkScrollableFrame(self.all_activity_frame, width= 850, height=300)
        self.entry_frame.pack(pady=(15, 0), padx=20)

        record_number_lbl = ctk.CTkLabel(self.entry_frame, font=("Segoe UI Semibold", 14), text= "ID")
        record_number_lbl.grid(row=0, column=0, pady=(5,5))

        current_mileage_lbl = ctk.CTkLabel(self.entry_frame, font=("Segoe UI Semibold", 14), text= "Mileage")
        current_mileage_lbl.grid(row=0, column=1, pady=(5,5))

        fuel_price_lbl = ctk.CTkLabel(self.entry_frame, font=("Segoe UI Semibold", 14), text= "Fuel Price")
        fuel_price_lbl.grid(row=0, column=2, pady=(5,5))

        fuel_amount_lbl = ctk.CTkLabel(self.entry_frame, font=("Segoe UI Semibold", 14), text= "Fuel Amount")
        fuel_amount_lbl.grid(row=0, column=3, pady=(5,5))

        total_amount_lbl = ctk.CTkLabel(self.entry_frame, font=("Segoe UI Semibold", 14), text= "Total Amount")
        total_amount_lbl.grid(row=0, column=4, pady=(5,5))

        date_lbl = ctk.CTkLabel(self.entry_frame, font=("Segoe UI Semibold", 14), text= "Date")
        date_lbl.grid(row=0, column=5, pady=(5,5))


        connect = sl.connect('record_info.db') 
        r_set=connect.execute('''SELECT * from record_info''');

        i=1 # row value inside the loop 
        for record in r_set:
            # b = ctk.CTkButton(self.entry_frame, text=i, width = 30, font=("Segoe UI",12, "bold"), fg_color="#FF5555",hover_color= "#ff0021", text_color="black", command=lambda: print(b._text))
            # b.grid(row=i, column= 0, pady=5, padx=10) 
            for j in range(len(record)):
                if (j == 0):
                    b = ctk.CTkButton(self.entry_frame, text=record[j], width = 30, font=("Segoe UI",12, "bold"), fg_color="#FF5555",hover_color= "#ff0021", text_color="black", command=lambda: print(b._text))
                    b.grid(row=i, column= 0, pady=5, padx=10) 
                e = ctk.CTkEntry(self.entry_frame) 
                e.grid(row=i, column=j+1, pady=5, padx=10) 
                e.insert(1,record[j])
                e.configure(state='disabled')

            i=i+1

        def delete_record():
            self.delete_record_window = ctk.CTk()
            self.delete_record_window.title("Delete record")
            self.delete_record_window.geometry("300x150")

            
            test = "2023-07-14"
            connect = sl.connect('record_info.db') 
            with connect:
                connect.execute("DELETE FROM record_info where date is ?", (test,))
            #self.all_activity_frame.destroy()

            self.delete_record_window.mainloop()
            

        #connect.close()
        
        self.button_frame3 = ctk.CTkFrame(self.all_activity_frame, fg_color="transparent")
        self.button_frame3.pack(pady=20)
        self.cancel_button = ctk.CTkButton(self.button_frame3, text="Go Back", command=self.all_activity_frame.destroy, font=("Segoe UI", 14, "bold"), fg_color="#1084cb", hover_color="#094971")
        self.cancel_button.grid(row=0, column=0,padx=10)
        self.delete_certain_record = ctk.CTkButton(self.button_frame3, text="Delete Record", command= delete_record, font=("Segoe UI", 14, "bold"), fg_color="#FF5555", hover_color= "#ff0021")
        self.delete_certain_record.grid(row=0, column=1, padx=10)

        self.all_activity_frame.mainloop()


dashboard = Dashboard()
dashboard.mainloop()
