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

        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.name = ctk.CTkEntry(self.info_frame, placeholder_text="Name", corner_radius=10)
        #self.name.grid(row=0,column=0, padx=10,pady=10,sticky="w")

        self.button = ctk.CTkButton(self.info_frame, text="Submit Info", command=self.button_event)
        #self.button.grid(row=0,column=0, padx=10,pady=10,sticky="w")

    def button_event(): 
        print("button pressed")



app = App()
app.mainloop()