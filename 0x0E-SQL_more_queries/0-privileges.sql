-- Create user user_0d_2
CREATE USER 'user_0d_2'@'localhost';

-- Grant privileges to user_0d_2 (adjust privileges as needed)
GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO 'user_0d_2'@'localhost';

-- List privileges for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

