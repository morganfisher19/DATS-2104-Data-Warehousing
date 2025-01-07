import mysql.connector
from faker import Faker
import random
from pymongo import MongoClient
# Initialize Faker
fake = Faker()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="healthcare"  # Ensure this database is created in MySQL
)
cursor = conn.cursor()

# Function for batch insertion
def batch_insert(data, query, batch_size=1000):
    for i in range(0, len(data), batch_size):
        cursor.executemany(query, data[i:i+batch_size])
        conn.commit()  # Commit after every batch

# Populate Patients Table
print("Generating patients data...")
patients = []
for _ in range(10001):  # Generate 99,900 patients
    patients.append((
        fake.name(),
        fake.random_int(min=1, max=100),  # Age
        fake.phone_number()[:15],  # Truncate to 15 characters to avoid errors
        fake.email()
    ))

print("Inserting patients data in batches...")
batch_insert(
    patients,
    '''
    INSERT INTO patients (name, age, contact_number, email)
    VALUES (%s, %s, %s, %s);
    '''
)

# Retrieve all patient IDs
cursor.execute("SELECT patient_id FROM patients;")
patient_ids = [row[0] for row in cursor.fetchall()]

# Populate Appointments Table
print("Generating appointments data...")
appointments = []
for _ in range(90001):  # Generate 90,000 appointments
    appointments.append((
        random.choice(patient_ids),  # Valid patient_id
        fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        fake.boolean(),
        fake.word(),
        fake.word(),
        fake.word(),
        f"{random.randint(1, 500)}mg",
        random.choice(["Once a day", "Twice a day", "Thrice a day"]),
        random.randint(0, 3),  # dose_day_1
        random.randint(0, 3),  # dose_day_2
        random.randint(0, 3),  # dose_day_3
        random.randint(0, 3),  # dose_day_4
        random.randint(0, 3),  # dose_day_5
        random.randint(0, 3),  # dose_day_6
        random.randint(0, 3)   # dose_day_7
    ))

print("Inserting appointments data in batches...")
batch_insert(
    appointments,
    '''
    INSERT INTO appointments (
        patient_id, date, is_follow_up, symptom1, symptom2, medication_name,
        dosage, frequency, dose_day_1, dose_day_2, dose_day_3, dose_day_4, dose_day_5, dose_day_6, dose_day_7
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''
)

# Commit and close
conn.commit()
conn.close()

print("SQL tables populated successfully!")

# Initialize Faker
fake = Faker()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare"]

# Access collections
patients_collection = db["patients"]
appointments_collection = db["appointments"]

# Populate Patients Collection
print("Populating patients collection...")
patients = []
for i in range(1, 10001):  # Generate 100 patients
    patients.append({
        "_id": i,
        "name": fake.name(),
        "age": fake.random_int(min=1, max=100),
        "contact_number": fake.phone_number(),
        "email": fake.email()
    })

patients_collection.insert_many(patients)

# Populate Appointments Collection
print("Populating appointments collection...")
appointments = []
for i in range(1, 90001):  # Generate 200 appointments
    appointments.append({
        "_id": i,
        "patient_id": random.randint(1, 100001),  # Valid patient_id
        "date": fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "is_follow_up": fake.boolean(),
        "symptoms": [fake.word(), fake.word()],
        "treatment_details": {
            "medication_name": fake.word(),
            "dosage": f"{random.randint(1, 500)}mg",
            "frequency": random.choice(["Once a day", "Twice a day", "Thrice a day"]),
            "dose_schedule": [random.randint(0, 3) for _ in range(7)]
        }
    })

appointments_collection.insert_many(appointments)

print("MongoDB collections populated successfully!")
