default_backup = """
BACKUP DATABASE name
TO DISK = 'filepath';
"""

# backups only the change
differential = """
BACKUP DATABASE name
TO DISK = 'D:\buckups\testDB.bak'
WITH DIFFERENTIAL;
"""
