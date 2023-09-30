import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

database_name = "flight_prices"

def create_database(database_name):
    try:
        # Connect to the SQLite database (this will create the database if it doesn't exist)
        conn = sqlite3.connect(database_name)
        
        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()

        # Create tables and define the schema as needed
        # Example: Creating a simple "users" table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS flight_prices (
                departure_airport TEXT,       
                destinatation_airport TEXT,
                departure_date TEXT,
                return_date TEXT,
                price_pp TEXT,
                url TEXT)
        ''')

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        print(f"Database '{database_name}' created successfully.")

    except sqlite3.Error as e:
        print("Error creating the database:", str(e))

def add_to_db(departure_aiport, destination_airport, departure_date, return_date, price_pp, url):
    try:
        # Connect to the SQLite database (this will create the database if it doesn't exist)
        conn = sqlite3.connect(database_name)
        
        sql = ('''
            INSERT INTO albums (departure_airport, destination_airport, departure_date, return_date, price_pp, url)
                       VALUES(?,?,?,?,?,?)      
        ''')  
        values =  departure_aiport, destination_airport, departure_date, return_date, price_pp, url
        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()
        cursor.execute(sql, values)
       
        # Commit the changes to the database
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

    except sqlite3.Error as e:
        print("Error creating the database:", str(e))