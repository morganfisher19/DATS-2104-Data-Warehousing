from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Load the IDs from the patients and doctors CSV files
patients_df = pd.read_csv("patients.csv")
doctors_df = pd.read_csv("doctors.csv")

# Get lists of patient_id and doctor_id
patient_ids = patients_df["patient_id"].tolist()
doctor_ids = doctors_df["doctor_id"].tolist()


# Generate 100 patient records
appointments = []
for _ in range(50000):
    appointment = {
        "appointment_id": fake.uuid4(),
        "patient_id": random.choice(patient_ids),
        "doctor_id": random.choice(doctor_ids),
        "status": random.choice(["Scheduled", "Completed", "Cancelled"])
        }
    appointments.append(appointment)

# Save to CSV
df_appointments = pd.DataFrame(appointments)
df_appointments.to_csv("appointments.csv", index=False)

'''
Expected CSV File: 
appointments.csv

Columns:
appointment_id: Unique identifier for each appointment (UUID format).
patient_id: Reference to the patient's ID (from patients).
doctor_id: Reference to the doctor's ID (from doctors).
status: Status of the appointment (Scheduled/Completed/Cancelled).
'''