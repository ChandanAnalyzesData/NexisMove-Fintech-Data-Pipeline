-- Query 1: Audit User Compliance
-- Objective: Identify all users who are actively transacting but have a 'Pending' KYC status.
SELECT user_id, full_name, kyc_status 
FROM users 
WHERE kyc_status = 'Pending';

-- Query 2: High-Value Transaction Monitoring
-- Objective: Flag any financial movement exceeding 50,000 INR for manual review.
SELECT transaction_id, sender_id, amount, status, timestamp 
FROM transactions 
WHERE amount > 50000.00;

-- Query 3: System Health Check (Orphan Hunting)
-- Objective: Find transactions linked to user IDs that do not exist in the master directory.
SELECT t.transaction_id, t.sender_id, t.amount 
FROM transactions t
LEFT JOIN users u ON t.sender_id = u.user_id
WHERE u.user_id IS NULL;