from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Generate 100 patient records
patients = []
for _ in range(50000):
    patient = {
        "patient_id": fake.uuid4(),
        "name": fake.name(),
        "age": random.randint(1, 90),
        "gender": random.choice(["Male", "Female"]),
        "phone_number": fake.phone_number() if random.random() > 0.2 else None,  # 20% chance for no phone number
        "medical_history": fake.sentence() if random.random() > 0.3 else None  # 30% chance for no medical history
    }
    patients.append(patient)

# Save to CSV
df_patients = pd.DataFrame(patients)
df_patients.to_csv("patients.csv", index=False)
