import customtkinter as ctk

def submit_entry():
    # Retrieve and process the user's input
    car_name = car_name_entry.get()
    expense_type = expense_type_entry.get()
    expense_amount = expense_amount_entry.get()
    
    # Perform further processing or saving of the entered data
    
    # Clear the input fields
    car_name_entry.delete(0, ctk.END)
    expense_type_entry.delete(0, ctk.END)
    expense_amount_entry.delete(0, ctk.END)

# Create the main application window
window = ctk.CTk()

# Add a title to the window
window.title("CarFactsTracker")

# Create and add labels to the window
ctk.CTkLabel(window, text="Car Name:").grid(row=0, column=0)
ctk.CTkLabel(window, text="Expense Type:").grid(row=1, column=0)
ctk.CTkLabel(window, text="Expense Amount:").grid(row=2, column=0)

# Create and add entry fields to the window
car_name_entry = ctk.CTkEntry(window)
car_name_entry.grid(row=0, column=1)

expense_type_entry = ctk.CTkEntry(window)
expense_type_entry.grid(row=1, column=1)

expense_amount_entry = ctk.CTkEntry(window)
expense_amount_entry.grid(row=2, column=1)

# Create and add a submit button to the window
submit_button = ctk.CTkButton(window, text="Submit", command=submit_entry)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
window.mainloop()