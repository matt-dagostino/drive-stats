import sqlite3 as sl
connect = sl.connect('record_info.db')
#connect.execute("DELETE FROM record_info")
with connect:
    connect.execute("""
        CREATE TABLE record_info (
            id INTEGER PRIMARY KEY,
            current_mileage INT,
            fuel_price DOUBLE,
            fuel_amount DOUBLE,
            total_amount DOUBLE,
            date DATE
        );
    """)

connect.close()
