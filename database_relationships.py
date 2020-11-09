import sqlite3
# -------------------Context Manager-------------------
class DatabaseContextManager(object):
    """This class exists for us to use less lines of code than necessary for queries.
        __init__: used to set database file name.
        __enter__: opens connection and creates cursor.
        __exit__: commits the changes to database file and closes connection."""

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


# with DatabaseContextManager("relationships") as db:
#     db.execute(query, parameters)

# "Foreign key table"
# Table = "Customers"
# Fields = [customer_id,first_name, last_name, age, Foreign Key (compnay_id) References Companies(company_id)]

# Table = "Companies"
# Fields = [company_id,company_name, employee_count]

# JOIN OUTPUT: 1,John,johnathan, 30, 2 , 2 , Google, 500


# ------------------------Table Creation------------------------
def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
                 customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 first_name TEXT,
                 last_name TEXT,
                 age INTEGER,
                 company_id INTEGER,
                FOREIGN KEY (company_id) REFERENCES Companies(company_id))"""
    with DatabaseContextManager("relationships") as db:
        db.execute(query)


def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
                 company_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 company_name TEXT,
                 employee_count INTEGER)"""
    with DatabaseContextManager("relationships") as db:
        db.execute(query)


# ------------------------CRUD------------------------

# Create
def create_customer(first_name: str, last_name: str, age: int, company_id: int):
    query = """INSERT INTO Customers(first_name, last_name, age, company_id) VALUES(?,?,?,?)"""
    parameters = [first_name, last_name, age, company_id]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


def create_company(company_name: str, employee_count: int):
    query = """INSERT INTO Companies(company_name, employee_count) VALUES(?,?)"""
    parameters = [company_name, employee_count]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


# Read
def get_customers(last_name):
    query = """SELECT * FROM Customers
               WHERE last_name = ?"""
    parameters = [last_name]
    with DatabaseContextManager("relationships") as cursor:
        cursor.execute(query, parameters)
        for value in cursor.fetchall():
            print(value)
    print("--------------------------------------------------------")


def get_companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("relationships") as db:
        db.execute(query)
        for value in db.fetchall():
            print(value)
    print("--------------------------------------------------------")


# Update
def update_customer_age(db, old_last_name: str, new_last_name: str):
    query = """UPDATE Customers
                SET last_name = ?, 
                WHERE last_name = ?"""
    parameters = [db, new_last_name, old_last_name]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


def update_company_employees(old_employee_count: str, new_employee_count: str):
    query = """UPDATE Companies
                SET employee_count = ? 
                WHERE employee_count = ?"""
    parameters = [new_employee_count, old_employee_count]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


# Delete
def delete_customer(last_name: str):
    query = """DELETE FROM Customers
                WHERE last_name = ?"""
    parameters = [last_name]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


def delete_company(employee_name: str):
    query = """DELETE FROM Companies
                WHERE employee_name = ?"""
    parameters = [employee_name]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


# Join
def get_customers_companies():
    query = """SELECT * FROM Customers
                JOIN Companies
                    ON Customers.company_id=Companies.company_id"""
    with DatabaseContextManager("relationships") as db:
        db.execute(query)
        for value in db.fetchall():
            print(value[0])

def drop_table():
    query = """DROP TABLE Company
    with DatabaseContextManager("relationships") as db:
        db.execute(query)

create_table_customers()
create_table_companies()
create_customer("Simas", "Laurys", 24)
create_customer("Tadas", "Kuisius", 43)
create_customer("Lina", "Aitienė", 20)
create_customer("Siga", "Girytė", 33)
create_customer("Rita", "Stasytė", 50)
create_company("UAB_1", 50)
create_company("UAB_2", 89)
create_company("UAB_3", 10)
get_customers()
get_companies()
update_customer_last_name()
update_company_employees()
delete_customer()
delete_company()"""