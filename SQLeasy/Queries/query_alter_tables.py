# There are no defaults, security, stability... reasons.
dummy_alters = """
  ALTER TABLE dummy_table
  ADD FOREIGN KEY(clients)
  REFERENCES clients(client_id)
  ON DELETE SET NULL;
"""
alt_size_type = """
ALTER TABLE dummy_db.dummy_table
CHANGE COLUMN dummy_industry dummy_industry VARCHAR(30) NULL DEFAULT NULL;
"""

# The initial value for AUTO_INCREMENT variable.
# WARNING, Drop the table data before doing this action, otherwise
# 'the re-indexing action' will start the counter bihind the last
# greater value. If the last entry shows 42(index), it will start
# from there==43.
counter = """
ALTER TABLE dummy_table
AUTO_INCREMENT = 1;
"""

# Key column 'clients' doesn't exist in table'
# This is because the table bills hasn't the column name 'clients'
# Conclusion: to make a relationship between tables, you should had
# been planned before, what the table is used for. This is a fun-ky problem.
# Now you need to add an extra field, for each table you want to relate
# with a main table.
# Solution: add first and move later.
# Add a new column
add_column = """
  ALTER TABLE orders
  ADD COLUMN client INT NULL AFTER order_id;
"""

# Move an existing column.
# Move the column col_name to a new column and preserve the column name -that
# is the name repetition, and place it AFTER other_col_name. The INT argument
# states the data type. The following NULL points to the default expresion,
# in this case nothing. The remaining two vars 'DEFAULT NULL' i'm not sure
# default could means 'default charset' and 'NULL' stands for collation; in
# case to not be defined, results in NULL.
move_column = """
ALTER TABLE budgets
  CHANGE COLUMN col_name col_name INT NULL DEFAULT NULL AFTER last_column;
"""

# Change the column name.
rename_column = """
  ALTER TABLE bills
  CHANGE COLUMN old_col new_col INT NULL DEFAULT NULL ;
"""

bills_alters = """
  ALTER TABLE bills
  ADD FOREIGN KEY(client)
  REFERENCES clients(client_id)
  ON DELETE SET NULL;
"""
budgets_alters = """
  ALTER TABLE budgets
  ADD FOREIGN KEY(client)
  REFERENCES clients(client_id)
  ON DELETE SET NULL;
"""
delivery_notes_alters = """
  ALTER TABLE delivery_notes
  ADD FOREIGN KEY(client)
  REFERENCES clients(client_id)
  ON DELETE SET NULL;
"""
offers_alters = """
  ALTER TABLE offers
  ADD FOREIGN KEY(client)
  REFERENCES clients(client_id)
  ON DELETE SET NULL;
"""
orders_alters = """
  ALTER TABLE orders
  ADD FOREIGN KEY(client)
  REFERENCES clients(client_id)
  ON DELETE SET NULL;
"""
