import os
import pandas as pd
import mysql.connector

# CSV location
csv_file = "Customer-Churn_Telco_Clean.csv"

# Read CSV
df = pd.read_csv(csv_file)

# Remove the extra index column
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

print("CSV loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Column names:")
print(df.columns.tolist())

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="customer_churn"
)

cursor = connection.cursor()

# Make sure we start with an empty table
cursor.execute("TRUNCATE TABLE customers")

# SQL insert
sql = """
INSERT INTO customers (
    customerID, gender, SeniorCitizen, Partner, Dependents,
    tenure, PhoneService, MultipleLines, InternetService,
    OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
    StreamingTV, StreamingMovies, Contract, PaperlessBilling,
    PaymentMethod, MonthlyCharges, TotalCharges, Churn
)
VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s
)
"""

# Convert rows into tuples
data = [tuple(row) for row in df.itertuples(index=False, name=None)]

# Insert data
cursor.executemany(sql, data)

connection.commit()

print("Data imported successfully!")
print("Rows inserted:", cursor.rowcount)

cursor.close()
connection.close()