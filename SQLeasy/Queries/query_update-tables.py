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

# TO UPDATE DATA
# This is BAD PRACTICE.
update = """
    UPDATE dummy_table
    SET dummy_id = 1
    WHERE dummy_id = 2;
"""

# ok with that.
update2 = """
    UPDATE dummy_table
    SET address = 'the new value for address field, 42'
    WHERE dummy_id = 101;
"""
