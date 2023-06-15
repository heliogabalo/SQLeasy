# This File is a map of known queries. To add new ones, just define a new variable
# and place there your query as a simple string. At the same time, could be
# used as a configuration file.

################################################
################### DEFAULTS ###################
################################################
# DEFAULT DATA BASE
defaultdB = 'customers_db'

# DEFAULT FILE
file = 'mySqlPsw.txt'

# VAULT
# Idealy, this path should be an URL path, to the 'vault-tec' server we
# expect to host in an undeterminated future. TerritorioLinux.
vault = 'C:/Users/Raul Vilchez Ruiz/OneDrive/Documentos/Private'

# PANDAS COLUMNS
# It should be consulted the table before; run a simple query to
# get the column's name.
p_columnus = ['client_id', 'client_name', 'client_address', 'client_industry', 'client_notes', 'client_telephone', 'client_status']

################################################
################### QUERIES ###################
################################################

# DEFAULT QUERY
default_query = """
    SELECT *
    FROM clients
"""

# DATA BASES' NAMES
dbNames = ['customers_db', 'dummy_db', 'information_schema',
           'mysql', 'performance_schema', 'sakila', 'sys', 'world']

# CREATE DATABASE
create_dummyDB = """
    CREATE DATABASE dummy_db
"""
# DELETE DATABASE
delete_dummyDB = """
    DROP DATABASE dummy_db
"""

# CREATE TABLE
create_dummy_table = """
    CREATE TABLE dummy_table(
      dummy_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      dummy_name VARCHAR(40) NOT NULL,
      dummy_address VARCHAR(60) NOT NULL,
      dummy_industry VARCHAR(20),
      dummy_notes VARCHAR(60),
      dummy_telephone INT,
      dummy_status BOOLEAN
    );
"""

# DELETE TABLE
delete_dummy_table = """
    DROP TABLE dummy_table
"""
delete_multiple_tables = """
    DROP TABLE bills, budgets, clients, delivery_notes, offers, orders, products, services;
"""

# ALTER TABLES
dummy_alters = """
  ALTER TABLE dummy_table
  ADD FOREIGN KEY(clients)
  REFERENCES clients(client_id)
  ON DELETE SET NULL;
"""

# Populate tables
pop_dummy = """
INSERT INTO dummy_table VALUES
(NULL, 'Atolon Inc.', 'Address street, 42', 'Rollos de pelicula', 'metrajes a encargo', '666666666', '0'),
(NULL, 'Telas asfalticas NG.', 'Address boulevard, 21', 'Obra publica', 'hoyos/hundimientos', '666000000', '1');
"""

q1 = """
    SELECT *
    FROM clients
"""

# To update data
update = """
    UPDATE dummy_table
    SET address = 'the new value for address field, 42'
    WHERE dummy_id = 101;
"""
# Delete data
delete_entry = """
    DELETE FROM dummy_table
    WHERE dummy_id = 1;
"""

# To push Python data structures(lists of tuples) into a database.
# This construction, isolates the values from the usual query:
# The Query:
sql = """
  INSERT INTO dummy_table (dummy_id, dummy_name, dummy_address, dummy_industry, dummy_notes, dummy_telephone, dummy_status)
  VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
# Do Note, that the placeholder has nothing to do with Python's strings
# data type '%s'. Sql will use this syntax to work with all types
# sql placeholder '%s' --> (str, int, dates...).
# The data structures:
val = [
    (7, 'Hunk', 'Dodson', 'ENG', None, '1991-12-23', 11111, '+09812734098'),
    (8, 'Funk', 'Bolson', 'EKR', 'ENG', '1491-15-16', 22222, '+09219014098')
]
################################################
############### APPLICATION MESAGES ############
################################################
message = """
You can do the following actions:\n \
      1. Test connection\t 5. ConnectionDB \t 9. Insert into Table\n \
      2. Start a new query\t 6. List Databases\t 10. Erase from Table\n \
      3. Create DataBase\t 7. Create Table\t 11. Python structures\n \
      4. Delete DataBase\t 8. Delete Table\t 12. Dump Html\n \
      \t\tq. Exit\t\t\t 0. List saved queries
 """

chosedB = """\n  Type the Data Base to update the SQL command \
\n  or chose one in the list:\n{}"""

test_message = """
    This is a test message with formated text, ready to get displayed \
    by the namespace.
"""

atention = """
ATENTION! This action can NOT be UNDONE. \
Do you want to proceed?
"""

cancel_action = """
The process "delete_db" was canceled.
"""

selectDb = """
\tChose one of the available Databases\n
\tby typing one, from the following list.\n
\t- If the Database does not exist, create one before this action.

"""

wrongDb = """
\tError; The database you typed it does not exist.\n \
\tCreate one or choose another !
"""

typeName = """
\tWrite the DataBase name:
"""
