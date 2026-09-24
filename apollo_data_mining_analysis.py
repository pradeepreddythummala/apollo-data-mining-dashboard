import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# APOLLO DATA MINING ANALYSIS
# ============================================================

print("APOLLO DATA MINING ANALYSIS")
print("=" * 50)

# ============================================================
# 1. LOAD DATASET
# ============================================================

file_path = "apollo_contacts.csv"

df = pd.read_csv(file_path)

# ============================================================
# 2. DATASET OVERVIEW
# ============================================================

print("\nDATASET OVERVIEW")
print("-" * 30)

print("Total contacts:", len(df))
print("Total columns:", len(df.columns))

# ============================================================
# 3. EMAIL STATUS
# ============================================================

print("\nEMAIL STATUS")
print("-" * 30)

email_status = df["Email Status"].value_counts()

print(email_status)

verified_count = (df["Email Status"] == "Verified").sum()
verified_rate = (verified_count / len(df)) * 100

print(f"\nVerified contacts: {verified_count}")
print(f"Verified rate: {verified_rate:.1f}%")

# ============================================================
# 4. TOP COMPANIES
# ============================================================

print("\nTOP COMPANIES")
print("-" * 30)

company_counts = df["Company Name"].value_counts().head(10)

print(company_counts)

# ============================================================
# 5. COMPANY SUMMARY
# ============================================================

print("\nCOMPANY SUMMARY")
print("-" * 30)

unique_companies = df["Company Name"].nunique()

print("Total unique companies:", unique_companies)

if not company_counts.empty:
    top_company = company_counts.index[0]
    top_company_count = company_counts.iloc[0]

    print("Company with most contacts:", top_company)
    print("Number of contacts:", top_company_count)

# ============================================================
# 6. TOP JOB TITLES
# ============================================================

print("\nTOP JOB TITLES")
print("-" * 30)

title_counts = df["Title"].value_counts().head(10)

print(title_counts)

# ============================================================
# 7. SENIORITY
# ============================================================

print("\nSENIORITY")
print("-" * 30)

if "Seniority" in df.columns:
    seniority_counts = df["Seniority"].value_counts()
    print(seniority_counts)
else:
    print("Seniority column not found.")

# ============================================================
# 8. LOCATION
# ============================================================

print("\nLOCATION")
print("-" * 30)

if "City" in df.columns:

    print("\nCities:")
    print(df["City"].value_counts())

if "State" in df.columns:

    print("\nStates:")
    print(df["State"].value_counts())

# ============================================================
# 9. INDUSTRY
# ============================================================

print("\nINDUSTRY")
print("-" * 30)

if "Industry" in df.columns:
    industry_counts = df["Industry"].value_counts()
    print(industry_counts)
else:
    print("Industry column not found.")

# ============================================================
# 10. DATA QUALITY ANALYSIS
# ============================================================

print("\nDATA QUALITY ANALYSIS")
print("-" * 30)

print("Total records:", len(df))

# ------------------------------------------------------------
# Email quality
# ------------------------------------------------------------

print("\nEmail quality:")

print(df["Email Status"].value_counts())

# ------------------------------------------------------------
# Missing values
# ------------------------------------------------------------

print("\nMissing values in important columns:")

important_columns = [
    "Title",
    "Company Name",
    "Email",
    "Email Status",
    "City",
    "State",
    "Industry"
]

for col in important_columns:

    if col in df.columns:

        missing = df[col].isna().sum()

        print(f"{col}: {missing} missing")

# ============================================================
# 11. DATA QUALITY PERCENTAGE
# ============================================================

print("\nDATA QUALITY PERCENTAGE")
print("-" * 30)

if len(df) > 0:

    email_verified_percentage = (
        (df["Email Status"] == "Verified").sum()
        / len(df)
    ) * 100

    print(
        f"Verified email percentage: "
        f"{email_verified_percentage:.1f}%"
    )

    missing_email_percentage = (
        df["Email"].isna().sum()
        / len(df)
    ) * 100

    print(
        f"Missing email percentage: "
        f"{missing_email_percentage:.1f}%"
    )

# ============================================================
# 12. CONTACT SUMMARY
# ============================================================

print("\nCONTACT SUMMARY")
print("-" * 30)

print("Total contacts:", len(df))
print("Verified contacts:", verified_count)
print("Non-verified contacts:", len(df) - verified_count)

# ============================================================
# 13. EXPORT COMPANY SUMMARY
# ============================================================

company_summary = (
    df["Company Name"]
    .value_counts()
    .reset_index()
)

company_summary.columns = [
    "Company Name",
    "Contact Count"
]

company_summary.to_csv(
    "company_summary.csv",
    index=False
)

print("\nCompany summary saved as: company_summary.csv")

# ============================================================
# 14. EXPORT SENIORITY SUMMARY
# ============================================================

if "Seniority" in df.columns:

    seniority_summary = (
        df["Seniority"]
        .value_counts()
        .reset_index()
    )

    seniority_summary.columns = [
        "Seniority",
        "Contact Count"
    ]

    seniority_summary.to_csv(
        "seniority_summary.csv",
        index=False
    )

    print("Seniority summary saved as: seniority_summary.csv")

# ============================================================
# 15. EXPORT JOB TITLE SUMMARY
# ============================================================

title_summary = (
    df["Title"]
    .value_counts()
    .reset_index()
)

title_summary.columns = [
    "Job Title",
    "Contact Count"
]

title_summary.to_csv(
    "title_summary.csv",
    index=False
)

print("Job title summary saved as: title_summary.csv")

# ============================================================
# 16. EMAIL STATUS CHART
# ============================================================

plt.figure(figsize=(8, 5))

email_status.plot(kind="bar")

plt.title("Email Status Distribution")
plt.xlabel("Email Status")
plt.ylabel("Number of Contacts")

plt.tight_layout()

plt.savefig("email_status.png")

plt.close()

print("Email status chart saved as: email_status.png")

# ============================================================
# 17. TOP COMPANIES CHART
# ============================================================

plt.figure(figsize=(10, 6))

company_counts.plot(kind="bar")

plt.title("Top Companies by Number of Contacts")
plt.xlabel("Company")
plt.ylabel("Number of Contacts")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("top_companies.png")

plt.close()

print("Top companies chart saved as: top_companies.png")

# ============================================================
# 18. FINAL MESSAGE
# ============================================================

print("\n" + "=" * 50)

print("Analysis completed successfully!")

print("=" * 50)