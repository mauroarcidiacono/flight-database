import sqlite3
import csv
import os
import pandas as pd
from src import airline_classes


class DBOperations:
    """This class will perform all the database operations"""

    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')

    # Database name
    database_name = os.path.join(base_dir, "db", "DBAirline.db")

    # SQL create table statements
    sql_create_table_flights = """
CREATE TABLE IF NOT EXISTS flights (
    flight_id INTEGER PRIMARY KEY,
    aircraft_id INTEGER,
    pilot_id INTEGER,
    origin TEXT,
    destination TEXT,
    flight_status TEXT,
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(aircraft_id),
    FOREIGN KEY (pilot_id) REFERENCES pilot(pilot_id)
)
"""

    sql_create_table_aircrafts = """
CREATE TABLE IF NOT EXISTS aircrafts (
    aircraft_id INTEGER PRIMARY KEY,
    aircraft_name TEXT,
    aircraft_type TEXT,
    capacity INTEGER,
    aircraft_status TEXT
)
"""

    sql_create_table_pilots = """
CREATE TABLE IF NOT EXISTS pilots (
    pilot_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    date_of_birth DATE,
    pilot_license TEXT,
    contact_number TEXT
)
"""
    # Database tables
    tables = ["aircrafts", "pilots", "flights"]

    sql_create_table = [sql_create_table_aircrafts,
                        sql_create_table_pilots,
                        sql_create_table_flights]

    # Table column names
    columns_names = {
        'aircrafts': ['aircraft_id', 'aircraft_name', 'aircraft_type', 'capacity', 'aircraft_status'],
        'pilots': ['pilot_id', 'first_name', 'last_name', 'date_of_birth', 'pilot_license', 'contact_number'],
        'flights': ['flight_id', 'aircraft_id', 'pilot_id', 'origin', 'destination', 'flight_status']
    }

    # Insert statements
    insert_statements = {
        'aircrafts': "INSERT INTO aircrafts (aircraft_id, aircraft_name, aircraft_type, capacity, aircraft_status) VALUES (?, ?, ?, ?, ?)",
        'pilots': "INSERT INTO pilots (pilot_id, first_name, last_name, date_of_birth, pilot_license, contact_number) VALUES (?, ?, ?, ?, ?, ?)",
        'flights': "INSERT INTO flights (flight_id, aircraft_id, pilot_id, origin, destination, flight_status) VALUES (?, ?, ?, ?, ?, ?)"
    }

    # SQL select and search statements
    sql_select_all = "SELECT * FROM TableName"
    sql_search = "SELECT * FROM TableName WHERE attribute = ?"

    # SQL update and delete statements
    sql_update_data = "UPDATE TableName SET ColName = ? WHERE row = ?"
    sql_delete_data = "DELETE FROM TableName WHERE ColName = ?"

    def __init__(self):
        try:
            self.conn = sqlite3.connect(self.database_name)
            self.conn.execute("PRAGMA foreign_keys = ON")
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def get_connection(self):
        """This method will get the connection to the database"""

        self.conn = sqlite3.connect(self.database_name)
        self.cur = self.conn.cursor()

    def create_table(self):
        """This method will create a table in the database"""

        print(" 1.1 Select the table you want to create")
        self.options_print()
        try:
            table_choice = int(input("Enter your choice: "))
            self.get_connection()
            self.cur.execute(self.sql_create_table[table_choice - 1])
            self.conn.commit()
            print("Table created successfully")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def insert_data_from_csv(self, table_choice, c, insert_statements):
        '''This method will insert data from csv files into a table'''
        
        files = [i + ".csv" for i in self.tables]
        filename = os.path.join(self.data_dir, files[table_choice - 1])
        table_name = os.path.splitext(os.path.basename(filename))[0]
        sql_insert = insert_statements[table_name]

        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                c.execute(sql_insert, tuple(row))

    def insert_data(self):
        """This method will insert a row into a table.
        The user will be asked to select a table and then
        he/she will be asked to enter the values for the row"""

        try:
            print(" 2.2 Select from the following options")
            print(" (1) Insert a row in a table")
            print(" (2) Insert data from csv files into a table")
            insert_option = int(input("Enter your choice: "))
            self.get_connection()

            print("Select the table you want to insert data into")
            allowed_options = self.options_print()
            table_choice = int(input("Enter your choice: "))

            if insert_option == 1:
                if table_choice == 1:
                    aircraft = airline_classes.Aircraft()
                    aircraft.set_aircraft_id(int(input("Enter aircraft_id: ")))
                    aircraft.set_aircraft_name(input("Enter aircraft_name: "))
                    aircraft.set_aircraft_type(input("Enter aircraft_type: "))
                    aircraft.set_aircraft_capacity(
                        int(input("Enter aircraft_capacity: ")))
                    aircraft.set_aircraft_status(
                        input("Enter aircraft_status: "))
                    self.cur.execute(self.insert_statements['aircrafts'], tuple(
                        str(aircraft).split("\n")))
                    print("Inserted data successfully")
                elif table_choice == 2:
                    pilot = airline_classes.Pilot()
                    pilot.set_pilot_id(int(input("Enter pilot_id: ")))
                    pilot.set_first_name(input("Enter first_name: "))
                    pilot.set_last_name(input("Enter last_name: "))
                    pilot.set_date_of_birth(input("Enter date_of_birth: "))
                    pilot.set_pilot_license(input("Enter pilot_license: "))
                    pilot.set_contact_number(input("Enter contact_number: "))
                    self.cur.execute(self.insert_statements['pilots'], tuple(
                        str(pilot).split("\n")))
                    print("Inserted data successfully")
                elif table_choice == 3:
                    flight = airline_classes.Flight()
                    flight.set_flight_id(int(input("Enter flight_id: ")))
                    flight.set_aircraft_id(int(input("Enter aircraft_id: ")))
                    flight.set_pilot_id(int(input("Enter pilot_id: ")))
                    flight.set_flight_origin(input("Enter flight_origin: "))
                    flight.set_flight_destination(
                        input("Enter flight_destination: "))
                    flight.set_flight_status(input("Enter flight_status: "))
                    self.cur.execute(self.insert_statements['flights'], tuple(
                        str(flight).split("\n")))
                    print("Inserted data successfully")
                else:
                    print("Invalid Choice")

            elif insert_option == 2:
                if table_choice in allowed_options:
                    self.insert_data_from_csv(
                        table_choice, self.cur, self.insert_statements)
                    print("Inserted data successfully")
            else:
                print("Invalid Choice")

            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def options_print(self):
        """This method will print the options for the user to select from"""

        options = []
        for i, table in enumerate(self.tables):
            print(f"({i + 1}) {table}")
            options.append(i + 1)
        return options

    def select_all(self):
        """This method will select all the data from a table and display it"""

        try:
            self.get_connection()
            print("Select the table you want to visualize")
            allowed_options = self.options_print()
            table_choice = int(input("Enter your choice: "))

            if table_choice in allowed_options:
                string_table_choice = self.tables[table_choice - 1]
                sql_select_all_mod = self.sql_select_all.replace(
                    "TableName", string_table_choice)
                self.cur.execute(sql_select_all_mod)
                result = self.cur.fetchall()
                df = pd.DataFrame(
                    result, columns=self.columns_names[string_table_choice])
                print(df)
            else:
                print("Invalid Choice")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def search_data_id(self):
        """This method will search for a row in a table based on the ID"""

        try:
            self.get_connection()
            print("Select a table to perform the search operation")
            self.options_print()
            table_choice = int(input("Enter your choice: "))
            if table_choice == 1:
                sql_search_mod = self.sql_search.replace(
                    "TableName", "aircrafts").replace(
                    "attribute", "aircraft_id")
                aircraft_id = int(input("Enter Aircraft ID: "))
                self.cur.execute(sql_search_mod, (aircraft_id,))
                result = self.cur.fetchone()
                if type(result) == type(tuple()):
                    for index, detail in enumerate(result):
                        if index == 0:
                            print("Aircraft ID: " + str(detail))
                        elif index == 1:
                            print("Aircraft Name: " + detail)
                        elif index == 2:
                            print("Aircraft Type: " + detail)
                        elif index == 3:
                            print("Capacity: " + str(detail))
                        else:
                            print("Status: " + detail)
                else:
                    print("No Record")
            elif table_choice == 2:
                sql_search_mod = self.sql_search.replace(
                    "TableName", "pilots").replace(
                    "attribute", "pilot_id")
                pilot_id = int(input("Enter Pilot ID: "))
                self.cur.execute(sql_search_mod, (pilot_id,))
                result = self.cur.fetchone()
                if type(result) == type(tuple()):
                    for index, detail in enumerate(result):
                        if index == 0:
                            print("Pilot ID: " + str(detail))
                        elif index == 1:
                            print("First Name: " + detail)
                        elif index == 2:
                            print("Last Name: " + detail)
                        elif index == 3:
                            print("Date of Birth: " + detail)
                        elif index == 4:
                            print("Pilot License: " + detail)
                        else:
                            print("Contact Number: " + str(detail))
            elif table_choice == 3:
                sql_search_mod = self.sql_search.replace(
                    "TableName", "flights").replace(
                    "attribute", "flight_id")
                flight_id = int(input("Enter Flight ID: "))
                self.cur.execute(sql_search_mod, (flight_id,))
                result = self.cur.fetchone()
                if type(result) == type(tuple()):
                    for index, detail in enumerate(result):
                        if index == 0:
                            print("Flight ID: " + str(detail))
                        elif index == 1:
                            print("Aircraft ID: " + str(detail))
                        elif index == 2:
                            print("Pilot ID: " + str(detail))
                        elif index == 3:
                            print("Flight Origin: " + detail)
                        elif index == 4:
                            print("Flight Destination: " + detail)
                        else:
                            print("Status: " + str(detail))
            else:
                print("Invalid Choice")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def search_data(self):
        """This method will search for a row or rows in a table based on the attribute value"""

        try:
            self.get_connection()

            print("Select a table to perform the search operation")
            allowed_options = self.options_print()
            table_choice = int(input("Enter your choice: "))
            print("Select the attribute to perform the search operation")
            print(
                f"The available attributes are {self.columns_names[self.tables[table_choice - 1]]}")
            attribute_search = input("Enter your choice: ")
            print("Select the attribute value to perform the search operation")
            attribute_value = input("Enter your choice: ")

            if table_choice in allowed_options and attribute_search in self.columns_names[self.tables[table_choice - 1]]:
                string_table_choice = self.tables[table_choice - 1]
                sql_search_mod = self.sql_search.replace(
                    "TableName", string_table_choice).replace(
                    "attribute", attribute_search)
                self.cur.execute(sql_search_mod, (attribute_value,))
                result = self.cur.fetchall()
                df = pd.DataFrame(
                    result, columns=self.columns_names[string_table_choice])
                print(df)
            else:
                print("Invalid Choice")
                return
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def update_data(self):
        """This method will update a table based on a search condition"""

        try:
            # Select a table to update
            self.get_connection()
            print("Select a table to update:")
            allowed_options = self.options_print()
            table_choice = int(input("Enter your choice: "))
            if table_choice not in allowed_options:
                print("Invalid Choice")
                return

            table_name = self.tables[table_choice - 1]

            # Select attribute for the search condition
            print("Which attribute do you want to use as a condition?")
            for i, col in enumerate(self.columns_names[table_name], 1):
                print(f"({i}) {col}")
            condition_col_choice = int(input("Enter your choice: "))
            if condition_col_choice < 1 or condition_col_choice > len(self.columns_names[table_name]):
                print("Invalid Choice")
                return

            # Define the value for the search condition
            condition_col_name = self.columns_names[table_name][condition_col_choice - 1]
            condition_value = input(
                f"Enter the value for {condition_col_name} to use as a condition: ")

            # Display the records that match the condition
            sql_search = self.sql_search.replace(
                "TableName", table_name).replace("attribute", condition_col_name)
            self.cur.execute(sql_search, (condition_value,))
            result = self.cur.fetchall()
            if not result:
                print("No records match the given condition.")
                return
            else:
                # Show the results in a dataframe
                df = pd.DataFrame(
                    result, columns=self.columns_names[table_name])
                print("Records that match the condition:")
                print(df)

            # Define the attribute to update and the new value
            print("Which attribute do you want to update?")
            for i, col in enumerate(self.columns_names[table_name], 1):
                print(f"({i}) {col}")
            update_col_choice = int(input("Enter your choice: "))
            if update_col_choice < 1 or update_col_choice > len(self.columns_names[table_name]):
                print("Invalid Choice")
                return

            update_col_name = self.columns_names[table_name][update_col_choice - 1]
            new_value = input(f"Enter the new value for {update_col_name}: ")

            # Perform the update operation
            sql_update = self.sql_update_data.replace(
                "TableName", table_name).replace(
                "ColName", update_col_name).replace(
                "row", condition_col_name)
            self.cur.execute(sql_update, (new_value, condition_value))
            affected_rows = self.cur.rowcount
            self.conn.commit()

            if affected_rows != 0:
                print(f"{affected_rows} Row(s) affected.")
            else:
                print("No records were updated.")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def delete_data(self):
        """This method will delete a row or rows from a table based on a search condition"""

        try:
            # Select a table to delete from
            self.get_connection()
            print("Select a table to delete from:")
            allowed_options = self.options_print()
            table_choice = int(input("Enter your choice: "))
            if table_choice not in allowed_options:
                print("Invalid Choice")
                return

            table_name = self.tables[table_choice - 1]

            # Select attribute for the search condition
            print("Which attribute do you want to use as a condition for deletion?")
            for i, col in enumerate(self.columns_names[table_name], 1):
                print(f"({i}) {col}")
            condition_col_choice = int(input("Enter your choice: "))
            if condition_col_choice < 1 or condition_col_choice > len(self.columns_names[table_name]):
                print("Invalid Choice")
                return

            condition_col_name = self.columns_names[table_name][condition_col_choice - 1]
            condition_value = input(
                f"Enter the value for {condition_col_name} to use as a condition: ")

            # Display the records that match the condition
            sql_search = self.sql_search.replace(
                "TableName", table_name).replace("attribute", condition_col_name)
            self.cur.execute(sql_search, (condition_value,))
            result = self.cur.fetchall()
            if not result:
                print("No records match the given condition.")
                return
            else:
                df = pd.DataFrame(
                    result, columns=self.columns_names[table_name])
                print("Records that match the condition:")
                print(df)

            # Perform the delete operation only if the user confirms it
            confirm = input(
                "Are you sure that you want to delete these records? (yes/no): ")
            if confirm.lower() == 'yes':
                sql_delete = self.sql_delete_data.replace(
                    "TableName", table_name).replace(
                    "ColName", condition_col_name)
                self.cur.execute(sql_delete, (condition_value,))
                affected_rows = self.cur.rowcount
                self.conn.commit()

                if affected_rows != 0:
                    print(f"{affected_rows} Row(s) deleted.")
                else:
                    print("No records were deleted.")
            else:
                print("Deletion cancelled.")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def summarize(self):
        """This method will summarize the data in the database"""

        try:
            # Menu for summarization
            self.get_connection()
            print("Select an option to summarize:")
            print("(1) Most popular destination")
            print("(2) Most used aircraft")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                # Popular destination
                sql_destination = """
                SELECT destination, COUNT(destination) as count
                FROM flights
                GROUP BY destination
                ORDER BY count DESC
                LIMIT 1
                """
                self.cur.execute(sql_destination)
                result = self.cur.fetchone()
                if result:
                    print(
                        f"The most popular destination is {result[0]} with {result[1]} flights.")
                else:
                    print("No data available.")

            elif choice == 2:
                # Most used aircraft
                sql_aircraft = """
                SELECT aircraft_id, COUNT(aircraft_id) as count
                FROM flights
                GROUP BY aircraft_id
                ORDER BY count DESC
                LIMIT 1
                """
                self.cur.execute(sql_aircraft)
                result = self.cur.fetchone()
                if result:
                    self.cur.execute(
                        "SELECT aircraft_name FROM aircrafts WHERE aircraft_id = ?", (result[0],))
                    aircraft_name = self.cur.fetchone()[0]
                    print(
                        f"The most used aircraft is {aircraft_name} (ID: {result[0]}) with {result[1]} flights.")
                else:
                    print("No data available.")

            else:
                print("Invalid Choice")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()
