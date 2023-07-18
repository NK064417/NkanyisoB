import psycopg2
import json
from psycopg2.extras import RealDictCursor

# Override the cursor factory to return RealDictCursor
class JSONCursorFactory(psycopg2.extensions.cursor):
    def __init__(self, *args, **kwargs):
        kwargs['cursor_factory'] = RealDictCursor
        super().__init__(*args, **kwargs)

# Connect to the database
conn = psycopg2.connect(
    host='your_host',
    database='your_database',
    user='your_username',
    password='your_password'
)

# Set the cursor_factory to use the JSONCursorFactory
conn.cursor_factory = JSONCursorFactory

# Create a cursor
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM public.user_table")

# Fetch all rows
rows = cur.fetchall()

# Convert the rows to JSON string format
json_result = json.dumps(rows)

# Print the JSON string result
print(json_result)

# Close the cursor and connection
cur.close()
conn.close()
