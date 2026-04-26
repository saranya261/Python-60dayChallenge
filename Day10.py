import random
import copy
import math
import numpy as np
import pandas as pd

def generate_data(n):
    data = []
    for i in range(n):
        student = {
            "id": i + 1,
            "marks": float(random.randint(40, 100)),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        data.append(student)
    return data

def mutate_data(data, roll):
    key = roll % 3
    for i in range(len(data)):
        if i % 3 == key:
            m = data[i]["marks"]
            data[i]["marks"] = m + math.sqrt(m)
            data[i]["attendance"] += 2
            data[i]["scores"][0] += 1

def manual_mean(data):
    total = 0
    for d in data:
        total += d["marks"]
    return total / len(data)

def detect_drift(a, b):
    return abs(a - b)

def classify(drift, copy_failed):
    if copy_failed:
        return "Copy Failure Detected"
    elif drift < 2:
        return "Stable Data"
    elif drift < 5:
        return "Minor Drift"
    else:
        return "Critical Drift"

roll = int(input("Enter your roll number: "))

n = random.randint(10, 12)
original = generate_data(n)
original_safe = copy.deepcopy(original)

shallow = original.copy()
deep = copy.deepcopy(original)

mutate_data(shallow, roll)
mutate_data(deep, roll)

df_original = pd.DataFrame(original_safe)
df_shallow = pd.DataFrame(shallow)
df_deep = pd.DataFrame(deep)

orig_mean = manual_mean(original_safe)
deep_mean = np.mean(df_deep["marks"])
std_dev = np.std(df_deep["marks"])
median = np.median(df_deep["marks"])

drift = detect_drift(orig_mean, deep_mean)

normalized = (df_deep["marks"] - np.min(df_deep["marks"])) / (np.max(df_deep["marks"]) - np.min(df_deep["marks"]))

copy_failed = original != original_safe

unique_attendance = set(df_deep["attendance"])

result = classify(drift, copy_failed)

print("\nNumber of students generated:", n)

print("\nOriginal Data:")
print(df_original)

print("\nShallow Copy Data:")
print(df_shallow)

print("\nDeep Copy Data:")
print(df_deep)

print("\nUnique Attendance Values:", unique_attendance)

print("\nDrift Value:", drift)
print("Median:", median)

print("Tuple (mean, drift, std_dev):", (deep_mean, drift, std_dev))

print("Normalized Marks:", list(normalized))

print("\nFinal Classification:", result)
