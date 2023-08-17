-- Create user user_0d_1
CREATE USER 'user_0d_1'@'localhost';

-- Grant privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Create user user_0d_2
CREATE USER 'user_0d_2'@'localhost';

-- Grant privileges to user_0d_2 (adjust privileges as needed)
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';

