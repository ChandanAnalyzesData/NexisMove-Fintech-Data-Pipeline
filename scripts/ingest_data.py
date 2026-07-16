import sqlite3
import pandas as pd

# 1. Connect to SQLite database (creates 'nexismove.db' automatically if it doesn't exist)
db_path = "nexismove.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("✅ Successfully connected to nexismove.db")

# 2. Read the SQL blueprint we committed earlier to build the tables
with open("queries/create_tables.sql", "r") as sql_file:
    sql_script = sql_file.read()

# Execute the blueprint to create our structures
cursor.executescript(sql_script)
conn.commit()
print("🏗️ Tables created successfully.")

# 3. Read our raw Excel sheets using Pandas
try:
    user_df = pd.read_excel("data/raw/NexisMove_Raw_Data.xlsx", sheet_name="User_Profiles")
    tx_df = pd.read_excel("data/raw/NexisMove_Raw_Data.xlsx", sheet_name="Transaction_Ledger")
    print("📈 Data sheets successfully loaded into Pandas DataFrames.")
except Exception as e:
    print(f"❌ Error reading Excel file: {e}")

# 4. Attempt to ingest the User Profiles into the database
try:
    user_df.to_sql("users", conn, if_exists="append", index=False)
    print("🚀 User data successfully loaded into SQL!")
except sqlite3.IntegrityError as e:
    print(f"🚨 DATABASE BLOCK: Ingestion failed due to a constraint violation!")
    print(f"Details: {e}")

# Close the database connection safely
conn.close()