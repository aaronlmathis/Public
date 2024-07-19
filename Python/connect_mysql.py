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


def main():
    # Database connection parameters
    db_params = {
        "host": "localhost",
        "user": "root",
        "password": "ThisIsADevSecret1!",
        "database": "mysql",
        "port": 3307
    }

    # Create database connection
    conn = create_connection(**db_params)

    # Create a cursor object
    cursor = conn.cursor()

    # Fetch and display employees
    employees = fetch_employees(cursor)
    display_employees(employees)

    # Close the cursor and connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
