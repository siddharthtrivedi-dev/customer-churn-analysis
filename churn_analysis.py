import pandas as pd

# Load the customer churn dataset
file_path = "Customer-Churn_Telco_Clean.csv"
df = pd.read_csv(file_path)

# Remove the extra index column
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Check dataset size
print("Dataset shape:", df.shape)

# Check column names
print("\nColumn names:")
print(df.columns.tolist())

# Check data types and missing values
print("\nDataset information:")
df.info()

print("\nMissing values in each column:")
print(df.isnull().sum())

# Analyze customer churn
print("\nChurn Distribution:")
print(df["Churn"].value_counts())

print("\nChurn Percentage:")
print((df["Churn"].value_counts(normalize=True) * 100).round(2))

# Customer churn summary
total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
retained_customers = (df["Churn"] == "No").sum()

churn_rate = (churned_customers / total_customers) * 100

print("\n===== CUSTOMER CHURN SUMMARY =====")
print("Total customers:", total_customers)
print("Churned customers:", churned_customers)
print("Retained customers:", retained_customers)
print("Churn rate:", round(churn_rate, 2), "%")

# Churn analysis by contract type
contract_analysis = df.groupby("Contract").agg(
    total_customers=("Churn", "count"),
    churned_customers=("Churn", lambda x: (x == "Yes").sum())
)

contract_analysis["churn_rate"] = (
    contract_analysis["churned_customers"]
    / contract_analysis["total_customers"] * 100
).round(2)

print("\n===== CHURN BY CONTRACT TYPE =====")
print(contract_analysis.sort_values("churn_rate", ascending=False))

# Create customer tenure groups
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, float("inf")],
    labels=["0-12 Months", "13-24 Months", "25-48 Months", "49+ Months"]
)

# Analyze churn by tenure group
tenure_analysis = df.groupby("TenureGroup", observed=False).agg(
    total_customers=("Churn", "count"),
    churned_customers=("Churn", lambda x: (x == "Yes").sum())
)

tenure_analysis["churn_rate"] = (
    tenure_analysis["churned_customers"]
    / tenure_analysis["total_customers"] * 100
).round(2)

print("\n===== CHURN BY TENURE =====")
print(tenure_analysis)

# Analyze churn by internet service
internet_analysis = df.groupby("InternetService").agg(
    total_customers=("Churn", "count"),
    churned_customers=("Churn", lambda x: (x == "Yes").sum())
)

internet_analysis["churn_rate"] = (
    internet_analysis["churned_customers"]
    / internet_analysis["total_customers"] * 100
).round(2)

print("\n===== CHURN BY INTERNET SERVICE =====")
print(internet_analysis.sort_values("churn_rate", ascending=False))

# Analyze churn by payment method
payment_analysis = df.groupby("PaymentMethod").agg(
    total_customers=("Churn", "count"),
    churned_customers=("Churn", lambda x: (x == "Yes").sum())
)

payment_analysis["churn_rate"] = (
    payment_analysis["churned_customers"]
    / payment_analysis["total_customers"] * 100
).round(2)

print("\n===== CHURN BY PAYMENT METHOD =====")
print(payment_analysis.sort_values("churn_rate", ascending=False))

# Analyze churn by tech support
support_analysis = df.groupby("TechSupport").agg(
    total_customers=("Churn", "count"),
    churned_customers=("Churn", lambda x: (x == "Yes").sum())
)

support_analysis["churn_rate"] = (
    support_analysis["churned_customers"]
    / support_analysis["total_customers"] * 100
).round(2)

print("\n===== CHURN BY TECH SUPPORT =====")
print(support_analysis.sort_values("churn_rate", ascending=False))

# Create readable customer type labels
df["CustomerType"] = df["SeniorCitizen"].map({
    0: "Non-Senior Citizen",
    1: "Senior Citizen"
})

# Analyze churn by customer type
senior_analysis = df.groupby("CustomerType").agg(
    total_customers=("Churn", "count"),
    churned_customers=("Churn", lambda x: (x == "Yes").sum())
)

senior_analysis["churn_rate"] = (
    senior_analysis["churned_customers"]
    / senior_analysis["total_customers"] * 100
).round(2)

print("\n===== CHURN BY SENIOR CITIZEN STATUS =====")
print(senior_analysis.sort_values("churn_rate", ascending=False))

# Analyze churn by online security
security_analysis = df.groupby("OnlineSecurity").agg(
    total_customers=("Churn", "count"),
    churned_customers=("Churn", lambda x: (x == "Yes").sum())
)

security_analysis["churn_rate"] = (
    security_analysis["churned_customers"]
    / security_analysis["total_customers"] * 100
).round(2)

print("\n===== CHURN BY ONLINE SECURITY =====")
print(security_analysis.sort_values("churn_rate", ascending=False))

# Create monthly charge groups
df["ChargeGroup"] = pd.cut(
    df["MonthlyCharges"],
    bins=[0, 30, 60, 90, float("inf")],
    labels=["Below $30", "$30-$59.99", "$60-$89.99", "$90+"],
    right=False
)

# Analyze churn by monthly charge group
charge_analysis = df.groupby("ChargeGroup", observed=False).agg(
    total_customers=("Churn", "count"),
    churned_customers=("Churn", lambda x: (x == "Yes").sum())
)

charge_analysis["churn_rate"] = (
    charge_analysis["churned_customers"]
    / charge_analysis["total_customers"] * 100
).round(2)

print("\n===== CHURN BY MONTHLY CHARGES =====")
print(charge_analysis.sort_values("churn_rate", ascending=False))

# Analyze churn by gender
gender_analysis = df.groupby("gender").agg(
    total_customers=("Churn", "count"),
    churned_customers=("Churn", lambda x: (x == "Yes").sum())
)

gender_analysis["churn_rate"] = (
    gender_analysis["churned_customers"]
    / gender_analysis["total_customers"] * 100
).round(2)

print("\n===== CHURN BY GENDER =====")
print(gender_analysis.sort_values("churn_rate", ascending=False))

# Analyze churn by partner status
partner_analysis = df.groupby("Partner").agg(
    total_customers=("Churn", "count"),
    churned_customers=("Churn", lambda x: (x == "Yes").sum())
)

partner_analysis["churn_rate"] = (
    partner_analysis["churned_customers"]
    / partner_analysis["total_customers"] * 100
).round(2)

print("\n===== CHURN BY PARTNER STATUS =====")
print(partner_analysis.sort_values("churn_rate", ascending=False))

# Analyze churn by dependents
dependents_analysis = df.groupby("Dependents").agg(
    total_customers=("Churn", "count"),
    churned_customers=("Churn", lambda x: (x == "Yes").sum())
)

dependents_analysis["churn_rate"] = (
    dependents_analysis["churned_customers"]
    / dependents_analysis["total_customers"] * 100
).round(2)

print("\n===== CHURN BY DEPENDENTS =====")
print(dependents_analysis.sort_values("churn_rate", ascending=False))

# Final customer churn KPI summary
total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
retained_customers = (df["Churn"] == "No").sum()

kpi_summary = {
    "Total Customers": total_customers,
    "Churned Customers": churned_customers,
    "Retained Customers": retained_customers,
    "Churn Rate (%)": round(
        churned_customers / total_customers * 100, 2
    ),
    "Average Monthly Charges": round(
        df["MonthlyCharges"].mean(), 2
    ),
    "Average Tenure (Months)": round(
        df["tenure"].mean(), 2
    )
}

print("\n===== FINAL CUSTOMER CHURN KPI SUMMARY =====")
for metric, value in kpi_summary.items():
    print(f"{metric}: {value}")






import matplotlib.pyplot as plt

# Plot churn rate by contract type
plt.figure(figsize=(8, 5))

bars = plt.bar(
    contract_analysis.index,
    contract_analysis["churn_rate"]
)

# Display percentage labels above each bar
plt.bar_label(bars, fmt="%.2f%%", padding=4)

plt.title("Customer Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.ylim(0, 50)
plt.tight_layout()

plt.savefig("churn_by_contract.png", dpi=300, bbox_inches="tight")
plt.show()


# Visualize churn rate by customer tenure
plt.figure(figsize=(8, 5))

bars = plt.bar(
    tenure_analysis.index.astype(str),
    tenure_analysis["churn_rate"]
)

plt.bar_label(bars, fmt="%.2f%%", padding=4)

plt.title("Customer Churn Rate by Tenure")
plt.xlabel("Customer Tenure")
plt.ylabel("Churn Rate (%)")
plt.ylim(0, 55)
plt.tight_layout()

plt.savefig("churn_by_tenure.png", dpi=300, bbox_inches="tight")
plt.show()



# Visualize churn rate by internet service
plt.figure(figsize=(8, 5))

bars = plt.bar(
    internet_analysis.index,
    internet_analysis["churn_rate"]
)

plt.bar_label(bars, fmt="%.2f%%", padding=4)

plt.title("Customer Churn Rate by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Churn Rate (%)")
plt.ylim(0, 50)
plt.tight_layout()

plt.savefig("churn_by_internet_service.png", dpi=300, bbox_inches="tight")
plt.show()



# Visualize churn rate by payment method
plt.figure(figsize=(9, 5))

bars = plt.bar(
    payment_analysis.index,
    payment_analysis["churn_rate"]
)

plt.bar_label(bars, fmt="%.2f%%", padding=4)

plt.title("Customer Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")
plt.ylim(0, 55)
plt.xticks(rotation=15, ha="right")
plt.tight_layout()

plt.savefig("churn_by_payment_method.png", dpi=300, bbox_inches="tight")
plt.show()