-- Step 1: Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Step 2: Grant all privileges on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
