import time
from pymongo import MongoClient
import pprint
client = MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
db = client["healthcare"]  # Access the 'healthcare' database
appointments_collection = db["appointments"]  # Access the 'appointments' collection
# Define mongodb query,  I just deleted and paster in new queries here each time
query = {

}

# --- Step 3: Execute the Query ---
start_time = time.time()
results = list(appointments_collection.find(query))  # Execute the query using find()
end_time = time.time()

# --- Step 4: Display Execution Time ---
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.6f} seconds (MongoDB)")