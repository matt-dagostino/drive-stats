
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

#from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import sqlite3 as sl

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/admin/Desktop/PythonApp/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#3A7FF6")
window.title("Car Fax - DEMO")


canvas = Canvas(
    window,
    bg = "#3A7FF6",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    430.9999999999999,
    0.0,
    861.9999999999999,
    519.0,
    fill="#FCFCFC",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command = lambda: SubmitINFO(),
    relief="flat"
)
button_1.place(
    x=556.9999999999999,
    y=417.0,
    width=180.0,
    height=55.0
)

canvas.create_text(
    39.999999999999886,
    127.0,
    anchor="nw",
    text="Welcome to Car Fax",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    481.9999999999999,
    61.00000000000001,
    anchor="nw",
    text="Enter the details below.",
    fill="#505485",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    481.9999999999999,
    120.0,
    anchor="nw",
    text="Name",
    fill="#505485",
    font=("Roboto Bold", 12 * -1)
)

canvas.create_text(
    481.9999999999999,
    215.0,
    anchor="nw",
    text="Email",
    fill="#505485",
    font=("Roboto Bold", 12 * -1)
)

canvas.create_text(
    481.9999999999999,
    310.0,
    anchor="nw",
    text="Phone number",
    fill="#505485",
    font=("Roboto Bold", 12 * -1)
)

canvas.create_rectangle(
    39.999999999999886,
    160.0,
    99.99999999999989,
    165.0,
    fill="#FCFCFC",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    650.4999999999999,
    167.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=489.9999999999999,
    y=137.0,
    width=321.0,
    height=59.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    650.4999999999999,
    262.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=489.9999999999999,
    y=232.0,
    width=321.0,
    height=59.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    650.4999999999999,
    357.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=489.9999999999999,
    y=327.0,
    width=321.0,
    height=59.0
)

canvas.create_text(
    34.999999999999886,
    215.0,
    anchor="nw",
    text="Simply input your information and watch as the appliation does the magic!",
    fill="#FFFFFF",
    font=("RobotoRoman Light", 24 * -1),
    width = 350
)


connect = sl.connect('user_info.db')
connect.execute("DELETE FROM USER")

def SubmitINFO():
    sql = 'INSERT INTO USER (name, email, phone_number) values (?, ?, ?)' 
    data = [
        (entry_1.get(), entry_2.get(), entry_3.get())
    ]
    with connect:
        connect.executemany(sql, data)
    with connect:
        testing = connect.execute("SELECT * FROM USER")
        for row in testing:
            print(row)
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
    messagebox.showinfo('Info', "Success! Thank you for your submission!")

# with connect:
#     connect.execute("""
#         CREATE TABLE USER (
#             name TEXT,
#             email TEXT,
#             phone_number INTEGER
#         );
#     """)

window.resizable(False, False)
window.mainloop()