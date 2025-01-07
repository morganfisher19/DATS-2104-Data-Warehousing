import mysql.connector
import time
import pprint
# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="healthcare"  # Replace with your database name
)
cursor = conn.cursor()

# Define the SQL query, I just deleted and paster in new queries here each time
sql_query = """

"""

# Measure execution time
start_time = time.time()
cursor.execute(sql_query)
results = cursor.fetchall()
end_time = time.time()

# Output execution time
print(f"Execution Time: {end_time - start_time:.6f} seconds(SQL)")

# Close connection
cursor.close()
conn.close()




