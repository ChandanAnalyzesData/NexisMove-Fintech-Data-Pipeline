import sqlite3
import pandas as pd

# 1. Establish database connection
db_path = "nexismove.db"
conn = sqlite3.connect(db_path)

# 2. Helper function to read a specific query from our SQL file
def get_sql_query(query_index):
    """
    Reads the queries/risk_analysis.sql file, splits it by semicolon,
    and returns the selected query.
    """
    with open("queries/risk_analysis.sql", "r") as file:
        # Read the file and split it into individual query statements
        sql_content = file.read()
        queries = [q.strip() for q in sql_content.split(";") if q.strip()]
        return queries[query_index]

# 3. Execute Query 1: KYC Status
print("\n🔍 --- AUDIT 1: PENDING KYC USERS ---")
query_1 = get_sql_query(0)
# pandas.read_sql_query runs the SQL string directly against the database file
df_kyc = pd.read_sql_query(query_1, conn)
print(df_kyc)

# 4. Execute Query 2: High-Value Transactions
print("\n🔍 --- AUDIT 2: HIGH-VALUE TRANSACTIONS (>= 50,000 INR) ---")
query_2 = get_sql_query(1)
df_high_val = pd.read_sql_query(query_2, conn)
print(df_high_val)

# 5. Execute Query 3: Orphan Hunt
print("\n🔍 --- AUDIT 3: ORPHANED TRANSACTIONS (NO MATCHING SENDER) ---")
query_3 = get_sql_query(2)
df_orphans = pd.read_sql_query(query_3, conn)
print(df_orphans)

# Close connection
conn.close()