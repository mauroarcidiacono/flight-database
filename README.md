# Database Management System

## Project Description

This project implements a menu-driven program for managing an airline database system using SQLite. The system allows users to perform operations such as creating tables, inserting data, searching, updating, and summarizing data from tables representing aircrafts, pilots, and flights. This program supports importing data from CSV files, querying based on user-defined criteria, and displaying results in a structured format.

## Features

### Menu Options
1. **Create Table**: Dynamically create tables in the SQLite database for aircrafts, pilots, and flights.
2. **Insert Data**: Insert rows into a table manually or from pre-defined CSV files.
3. **Select All Data**: Retrieve and display all records from a selected table.
4. **Search by ID**: Search for a specific record by its unique ID (e.g., Flight ID, Aircraft ID, Pilot ID).
5. **Search by Attribute**: Query records based on an attribute value.
6. **Update Data**: Modify existing records in the database.
7. **Delete Data**: Remove records from a table based on specific criteria.
8. **Summarization**: Generate insights such as the most popular flight destination or most-used aircraft.
9. **Exit**: Exit the program gracefully.

### File Structure
- **src/**: Contains the main program logic and supporting classes.
- **data/**: Holds CSV files for importing initial data.
- **db/**: Contains the SQLite database file (`DBAirline.db`).

### Key Functionalities
- SQLite integration with foreign key support.
- Import data from CSV files.
- Dynamic table creation and data insertion.
- Robust error handling for invalid inputs.

## Requirements

### Software
- Python 3.8 or higher
- SQLite

### Python Libraries
- `os`
- `sqlite3`
- `csv`
- `pandas`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install pandas
   ```

## Usage

1. Run the program:
   ```bash
   python -m src.main
   ```

2. Follow the interactive menu to perform database operations.

## Sample Data Files

The `data/` directory contains sample CSV files:
- `aircrafts.csv`: Data for aircrafts.
- `pilots.csv`: Data for pilots.
- `flights.csv`: Data for flights.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

