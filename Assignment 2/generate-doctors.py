from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Generate 100 patient records
doctors = []
for _ in range(50000):
    doctor = {
        "doctor_id": fake.uuid4(),
        "name": fake.name(),
        "specialty": random.choice([
            "Allergy and Immunology",
            "Anesthesiology",
            "Cardiology",
            "Dermatology",
            "Emergency Medicine",
            "Endocrinology",
            "Family Medicine",
            "Gastroenterology",
            "General Surgery",
            "Geriatrics",
            "Hematology",
            "Infectious Disease",
            "Internal Medicine",
            "Nephrology",
            "Neurology",
            "Obstetrics and Gynecology (OB-GYN)",
            "Oncology",
            "Ophthalmology",
            "Orthopedics",
            "Otolaryngology (ENT)",
            "Pathology",
            "Pediatrics",
            "Plastic Surgery",
            "Psychiatry",
            "Pulmonology",
            "Radiology",
            "Rheumatology",
            "Sports Medicine",
            "Vascular Surgery",
            "Urology"
        ]),
        "experience_years": random.randint(1, 40)
    }
    doctors.append(doctor)

# Save to CSV
df_doctors = pd.DataFrame(doctors)
df_doctors.to_csv("doctors.csv", index=False)

'''
Expected CSV File: 
doctors.csv

Columns:
doctor_id: Unique identifier for each doctor (UUID format).
name: Doctor's name.
specialty: Doctor's medical specialty.
experience_years: Years of experience (1-40).
'''