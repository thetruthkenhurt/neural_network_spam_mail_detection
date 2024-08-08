# config.py
# Configuration for database connectivity 

import os 

# Database Path Configuration:
# Please update the DB_PATH with the absolute path to your 'calls.db' database file on your local system.
# This path is used by the Python scripts to connect to the SQLite database.
# Ensure that the path uses double backslashes (\\) or raw string notation (r'path') to avoid escape character issues.

# For Windows, use a raw string to avoid issues with backslashes:
# DB_PATH = r'C:\path\to\calls.db'
# For Unix/Linux or macOS, use a regular string:
# DB_PATH = '/path/to/calls.db'
#please place the path of your calls.db file on your local machine here
DB_PATH = r'yourpath'

#if using public data(spambase.data from UCSI)
PUBLIC_DATA_PATH = os.path.join(os.path.dirname(__file__), '../spambase/spambase.data')