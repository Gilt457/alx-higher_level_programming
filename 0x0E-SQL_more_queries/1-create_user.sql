-- This code creates a new user named user_0d_1 on the local MySQL server and gives them full access to all databases and tables.
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
