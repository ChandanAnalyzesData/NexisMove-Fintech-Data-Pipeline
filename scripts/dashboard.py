import sqlite3
import pandas as pd
import streamlit as st

# Set page layout
st.set_page_config(page_title="NexisMove Risk Operations", layout="wide")
st.title("🛡️ NexisMove // Risk & Compliance Dashboard")
st.markdown("Real-time monitoring of P2P ledger anomalies and onboarding compliance.")

# Connect to database
conn = sqlite3.connect("nexismove.db")

# Sidebar Metrics
st.sidebar.header("System Overview")
total_users = pd.read_sql_query("SELECT COUNT(*) FROM users;", conn).iloc[0, 0]
total_txs = pd.read_sql_query(
    "SELECT COUNT(*) FROM transactions;", conn
).iloc[0, 0]

st.sidebar.metric(label="Registered Users", value=total_users)
st.sidebar.metric(label="Total Ledger Transactions", value=total_txs)

# Create layout columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("🚨 Compliance Alert: Pending KYC")
    query_1 = (
        "SELECT user_id, full_name, kyc_status FROM users WHERE kyc_status ="
        " 'Pending';"
    )
    df_kyc = pd.read_sql_query(query_1, conn)
    if not df_kyc.empty:
        st.dataframe(df_kyc, use_container_width=True)
    else:
        st.success("All active users are KYC verified.")

with col2:
    st.subheader("👻 System Integrity: Orphan Transactions")
    query_3 = (
        "SELECT t.transaction_id, t.sender_id, t.amount FROM transactions t"
        " LEFT JOIN users u ON t.sender_id = u.user_id WHERE u.user_id IS"
        " NULL;"
    )
    df_orphans = pd.read_sql_query(query_3, conn)
    if not df_orphans.empty:
        st.warning("Ghost accounts detected moving funds!")
        st.dataframe(df_orphans, use_container_width=True)
    else:
        st.success("Ledger integrity verified. No orphan records found.")

# High-Value Monitoring Section
st.subheader("💰 Transaction Velocity Monitoring")
query_2 = "SELECT * FROM transactions WHERE amount >= 50000;"
df_high = pd.read_sql_query(query_2, conn)
st.dataframe(df_high, use_container_width=True)

conn.close()