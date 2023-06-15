# This is the place where new queries should be implemented. Define a unique
# identifier variable, then copy/paste the function to the configuration
# file.

# POPULATE TABLES
# This query belongs to a table with an "AUTO_INCREMENT" inndex value; remember
# to left 'NULL' the '_id' field.
pop_dummy = """
INSERT INTO dummy_table VALUES
(NULL, 'Atolon Inc.', 'Address street, 42', 'Rollos de pelicula', 'metrajes a encargo', '666666666', '0'),
(NULL, 'Telas asfalticas NG.', 'Address boulevard, 21', 'Obra publica', 'hoyos/hundimientos', '666000000', '1');
"""

# DELETE DATA
# When an entire row is deleted from a table, the other index will not be
# affected; but the table will remain with a no-contiguous list of numbered
# indexes.
delete_entry = """
    DELETE FROM dummy_table
    WHERE dummy_id = 1;
"""

# to delete multiple rows, write a line for each one.
# This is not valid '1, 2, 37, 38, 39, 40, 41, 42, 43, 44'

# As a general rule; to overwrite identifiers(whatever_id), is a bad idea.
# Because you are rewriting history! Once a row is deleted, forget the entry.
# SQL has 'methods' enough to not bother with that. Some people enter a
# dummy_row, with a note reffering the deleted entry. Pff, innecessary!;
# but in the worst situation, the dummy_row case it's acceptable.
# Another aproach, is to dump the entire table, 'format' the new data,
# and push the datum again. All information in a table it's precious, and
# should be preserved; like a jump in a counter. Some DataBase administrators
# goes crazy when some unexperienced user, decides to change the counter.
# Counter strikes!
# Do you know that all information in a DataBase it's accounted! it has
# a similar concept as the repo(repository).
delete_multiple = """
    DELETE FROM dummy_table WHERE dummy_id = 1;
    DELETE FROM dummy_table WHERE dummy_id = 2;
    DELETE FROM dummy_table WHERE dummy_id = 3;
"""
