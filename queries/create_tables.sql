-- 1. Create the Parent Profiles Table
CREATE TABLE users (
    user_id VARCHAR(50) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    signup_date DATE,
    kyc_status VARCHAR(20) DEFAULT 'Pending'
);

-- 2. Create the Child Transactions Ledger Table
CREATE TABLE transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,
    sender_id VARCHAR(50),
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(10) DEFAULT 'INR',
    status VARCHAR(20) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES users(user_id)
);