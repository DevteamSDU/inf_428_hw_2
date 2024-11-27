import pandas as pd
import numpy as np
import random


def generate_random_data(num_departments=5):
    departments = ["Engineering", "Marketing", "Finance", "HR", "Science"]
    data = []

    for department in departments:
        num_users = random.randint(10, 200)
        mean = random.randint(20, 70)
        variance = random.randint(5, 20)
        scores = np.random.randint(max(0, mean - variance), min(90, mean + variance + 1), num_users)

        for score in scores:
            data.append({"department": department, "threat_score": score})

    return pd.DataFrame(data)
