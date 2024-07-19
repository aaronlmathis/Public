import mysql.connector
from datetime import date, datetime

def create_connection(host, user, password, database, port):
    """Create and return a MySQL database connection."""
    print("Establishing MySQL connection...\n")
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )

def create_employee_table(cursor, conn):
    """Create the employees table if it doesn't exist and populate it with initial data."""
    table_creation_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(100),
        hire_date DATE,
        salary DECIMAL(10, 2)
    )
    """
    cursor.execute(table_creation_query)
    conn.commit()
    
    # Check if table is empty
    cursor.execute("SELECT COUNT(*) FROM employees")
    if cursor.fetchone()[0] == 0:
        # Populate with initial data
        initial_data = [
            (0, 'Aaron', 'Mathis', 'aaron@pcmc.us', '2022-01-15', 50000.00),
            (0, 'Beth', 'Smith', 'beth@pcmc.us', '2023-02-20', 60000.00),
            (0, 'Charlie', 'Johnson', 'charlie@pcmc.us', '2021-03-25', 55000.00)
        ]
        insert_query = """
        INSERT INTO employees (id, first_name, last_name, email, hire_date, salary)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.executemany(insert_query, initial_data)
        conn.commit()
        print("Employees table created and populated with initial data.")

def fetch_employees(cursor):
    """Fetch employee data from the database."""
    query = "SELECT id, first_name, last_name, email, hire_date, salary FROM employees"
    cursor.execute(query)
    return cursor.fetchall()

def format_date(hire_date):
    """Format hire_date to MM-DD-YYYY."""
    if isinstance(hire_date, date):
        return hire_date.strftime("%m-%d-%Y")
    else:
        return datetime.strptime(hire_date, "%Y-%m-%d").strftime("%m-%d-%Y")

def display_employees(employees):
    """Display employee data with formatted hire_date."""
    print("Returning employees...\n\n")
    for row in employees:
        id, first_name, last_name, email, hire_date, salary = row
        formatted_date = format_date(hire_date)
        print(f"Name: {first_name} {last_name}, Email: {email}, Hire Date: {formatted_date}, Salary: {salary}")

def main_menu():
    """Display the main menu and handle user input."""
    conn = None
    cursor = None
    
    while True:
        print("\nMain Menu:")
        print("1. Establish database connection")
        print("2. Create and populate employees table")
        print("3. Fetch and display employees")
        print("4. Run SQL query")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            if conn and conn.is_connected():
                print("Connection is already established.")
            else:
                db_params = get_db_params()
                conn = create_connection(**db_params)
                cursor = conn.cursor()
                print("Database connection established.")
        elif choice == "2":
            if not conn or not conn.is_connected():
                print("Please establish a database connection first.")
            else:
                create_employee_table(cursor, conn)
        elif choice == "3":
            if not conn or not conn.is_connected():
                print("Please establish a database connection first.")
            else:
                employees = fetch_employees(cursor)
                display_employees(employees)
        elif choice == "4":
            if not conn or not conn.is_connected():
                print("Please establish a database connection first.")
            else:
                run_sql_query(cursor, conn)
        elif choice == "5":
            print("Exiting...")
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            break
        else:
            print("Invalid choice. Please try again.")

def get_db_params():
    """Prompt the user for database connection parameters."""
    host = input("Enter host: ")
    user = input("Enter user: ")
    password = input("Enter password: ")
    database = input("Enter database: ")
    port = int(input("Enter port: "))
    return {
        "host": host,
        "user": user,
        "password": password,
        "database": database,
        "port": port
    }

def run_sql_query(cursor, conn):
    """Prompt the user for an SQL query and execute it."""
    query = input("Enter your SQL query: ")
    try:
        cursor.execute(query)
        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()
            for row in result:
                print(row)
        else:
            conn.commit()
            print("Query executed successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main_menu()
