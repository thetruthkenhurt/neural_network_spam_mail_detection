# config.py
# Configuration for database connectivity 

# Database Path Configuration:
# Please update the DB_PATH with the absolute path to your 'calls.db' database file on your local system.
# This path is used by the Python scripts to connect to the SQLite database.
# Ensure that the path uses double backslashes (\\) or raw string notation (r'path') to avoid escape character issues.

# For Windows, use a raw string to avoid issues with backslashes:
# DB_PATH = r'C:\path\to\calls.db'
# For Unix/Linux or macOS, use a regular string:
# DB_PATH = '/path/to/calls.db'
#please place the path of your calls.db file on your local machine here
DB_PATH = r'C:\Users\Ken\Documents\AISG Assessment\AIAP 17 Assessment\calls.db'

#if using public data(spambase.data from UCSI)
PUBLIC_DATA_PATH = r'C:\Users\Ken\Documents\Code Projects\Spam Mail Classification\spambase\spambase.data'