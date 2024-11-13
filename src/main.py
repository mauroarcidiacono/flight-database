from src import dboperations

# The main function will parse arguments.
# These argument will be defined by the users on the console.
# The user will select a choice from the menu to interact with the database.

while True:
    print("\n Menu:")
    print("**********")
    print(" 1. Create table")
    print(" 2. Insert data into table")
    print(" 3. Select all data from table")
    print(" 4. Search a flight, aircraft or pilot by ID")
    print(" 5. Search based on a attribute value")
    print(" 6. Update data in the database")
    print(" 7. Delete data in the database")
    print(" 8. Summarization")
    print(" 9. Exit\n")

    __choose_menu = input("Enter your choice: ")

    # Validate input
    if not __choose_menu.isdigit():
        print("Invalid input! Please enter a number between 1 and 9.")
        continue

    __choose_menu = int(__choose_menu)

    db_ops = dboperations.DBOperations()
    if __choose_menu == 1:
        db_ops.create_table()
    elif __choose_menu == 2:
        db_ops.insert_data()
    elif __choose_menu == 3:
        db_ops.select_all()
    elif __choose_menu == 4:
        db_ops.search_data_id()
    elif __choose_menu == 5:
        db_ops.search_data()
    elif __choose_menu == 6:
        db_ops.update_data()
    elif __choose_menu == 7:
        db_ops.delete_data()
    elif __choose_menu == 8:
        db_ops.summarize()
    elif __choose_menu == 9:
        exit(0)
    else:
        print("Invalid Choice")
