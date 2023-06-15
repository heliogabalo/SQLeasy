import mysql.connector
from mysql.connector import Error
# import pandas as pd

##############################################
####### FreeCodeCamp - tutorial FreeCC.py #######
##############################################

####### connect to the serer and create database #######
def create_server_connection(host_name, user_name, user_pwd):
  """
  An implemented function prototype, teaching the MySQL ``connect()`` method
  how_to guide. Application <SQLeasy module> use it to check the database server
  connection.

  :paran host_name: host runing the SQL server.
  :paran user_name: user name.
  :paran user_pwd: idem as definition name.
  """
  connection = None
  try:
    connection = mysql.connector.connect(
    host=host_name,
    user=user_name,
    passwd=user_pwd
    )
    print("MySQL Database connection successful")
  except Error as err:
    print(f"Error: '{err}'")

  return connection

####### SECTION create new database #######
def create_database(connection, query):
  '''
  It stablish an initial connection. It should not be used, beyond the initial
  set up of the database connection server. So any new database initial
  configuration(any other database) it will make use of it.

  The actual SQL(Structured Query Language) query, it's saved in a simple
  variable idealy. So you can write SQL commands, as you typed over a
  natural SQL interface.

  :param connection: defined connection. See create_server_connection().
  :param query: python simple string. Save any MySQL valid query to
                modify the defaul value.
  '''
  cursor = connection.cursor()
  try:
      cursor.execute(query)
      print("Database created successfully")
  except Error as err:
      print(f"Error: '{err}'")

####### SECTION modify server connectionfunction #######
def create_db_connection(host_name, user_name, user_pwd, dbName):
  '''
  A function library to reuse the code. It defines a MySQL server connection
  Actualy the only value that not have defults is ``host_name``; not yet
  implemented.

  :param host_name: or machine name.
  :param user_name: a wise choose, to reflect a system agnostic approach(root).
  :param user_pwd: user password.
  :param dbName: user DataBase.
  '''
  connection = None
  try:
      connection = mysql.connector.connect(
          host=host_name,
          user=user_name,
          passwd=user_pwd,
          database=dbName
      )
      print("MySQL Database connection successful")
  except Error as err:
      print(f"Error: '{err}'")

  return connection

####### SECTION define query execution function #######
def execute_query(connection, query):
  '''
  Function library; method cursor(). As usual, it is passed the connection
  method to the cursor() function libraryin python style, where everything
  is an object; as our connection.
  We wrap the function contents, inside a try ... except sentence, to catch up
  the server answer. Note the commit() method here, because not doing this,
  the actual query will be flushed away, without any effect.

  :param connection: reusable code, as seen before.
  :param query: This argument is a placeholder of the actual SQL function.

  Note that any query that write data(add, delete, modify) to the database, will
  use this execute_query() function. Read(or fetch) data is another way
  to do things, and requires another function by their own.
  '''
  cursor = connection.cursor()
  try:
      cursor.execute(query)
      connection.commit()
      print("Query successful")
  except Error as err:
      print(f"Error: '{err}'")

## READING DATA
def read_query(connection, query):
  '''
  Read only function, to interface the database. It differs slightly from
  execute_query() function, with the fetchall() method.

  :param connection: our connection, as usual.
  :param query: those qN* SQL functions, writed as a simple string. I.e:
                "SELECT * FROM clients"
  '''
  cursor = connection.cursor()
  result = None
  try:
    cursor.execute(query)
    result = cursor.fetchall()
    return result
  except Error as err:
    print(f"Error: '{err}'")

def execute_list_query(connection, sql, val):
  """
  MySQL function to push 'packaged' data to the DB. It takes a Python data
  structures -such as a list, and insert directly into the database.
  Useful to store user activity logs or inputs from users into a wiki or
  social media app, we have built.

  If the database is open to other users, it helps to prevent aginsst
  SQL-injection attacks. To acomplish this task it has been used the method
  ``executemany()``.

  It is coincidence the use of the Python placeholder ``%s``. It refers
  to the SQL one, and it does not distiguish betweeen ``str`` or ``int``.
  Using this method it is encouraged to name the ``val`` parameter as
  a specifically named variable, if you think in save the query for automated
  queries; more easy to find inside the config file.

  :parm connection: MySQL connection.
  :parm sql: the SQL command you are trying to run.
  :parm val: a list of Python tuples.
  """
  cursor = connection.cursor()
  try:
    cursor.executemany(sql, val)
    connection.commit()
    print("Query successful")
  except Error as err:
    print(f"Error: '{err}'")
