# Import necessary libraries
# sqlalchemy is used to interact with the database
import sqlalchemy
# re is imported but not used in this code; it's typically used for regular expression operations

# Create a database engine using SQLAlchemy
# This establishes a connection to the MariaDB database using the pymysql driver
# "root" is the username, no password is provided, "localhost" is the server location,
# 3307 is the port number, and "northwindsdb" is the name of the database
# echo=True means SQLAlchemy will log all SQL statements executed, useful for debugging
db = sqlalchemy.create_engine(
    "mariadb+pymysql://root:@localhost:3307/northwindsdb", echo=True
)

# Define a function to fetch all customers from the customers table
def get_customers():
    # Connect to the database
    with db.connect() as conn:
        # Execute a SQL query to select all records from the customers table
        result = conn.execute(sqlalchemy.text("SELECT * FROM customers"))
        # Print all the results fetched by the query
        print(result.all())

# Define a function to fetch total price of orders grouped by shipper
def get_shipper_total_price_of_orders():
    # Connect to the database
    with db.connect() as conn:
        # Execute a SQL query to join shippers and orders tables, calculate total freight cost,
        # and group results by shipper company name
        result = conn.execute(
            sqlalchemy.text(
                "SELECT shippers.companyname, orders.shipvia, SUM(orders.freight) AS total_freight, "
                "orders.shipcountry, shippers.phone FROM shippers "
                "RIGHT JOIN orders ON orders.shipvia = shippers.shipperid "
                "GROUP BY shippers.companyname"
            )
        )
        # Return the fetched results
        return result.all()

# Define a function to fetch all employee first and last names
def get_all_employees():
    # Initialize an empty string to store employee names
    returnString = ""

    # Connect to the database
    with db.connect() as conn:
        # Execute a SQL query to select first and last names from the employees table
        result = conn.execute(
            sqlalchemy.text("SELECT firstname, lastname FROM employees"),
        )
        # Iterate through each record in the result set
        for employee in result:
            # Store the first name of each employee into returnString, but this loop will
            # only keep the last employee's first name due to reassignment
            returnString = f"{employee.firstname}"

        # Return the first name of the last employee in the result set
        return returnString

# Define the main function that calls other functions when the script is executed
def main():
    # Uncomment the desired function to execute it
    # get_customers() # Calls the function to print all customers
    # get_shipper_total_price_of_orders() # Calls the function to get total freight cost per shipper
    get_all_employees() # Calls the function to get all employee names

    # You can print additional information from functions, for example:
    # print("List of employee first names:", get_all_employees())

# Checks if the script is run directly (not imported as a module) and then calls the main function
if __name__ == "__main__":
    main()
