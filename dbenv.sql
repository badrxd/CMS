-- Create the user if it doesn't exist
SELECT 'CREATE DATABASE cms' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'cms')\gexec
-- Check if the role exists
SELECT 'CREATE USER admin WITH PASSWORD `admin`' WHERE NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'admin')\gexec
-- Grant all privileges on the 
GRANT ALL PRIVILEGES ON DATABASE cms TO admin;


CREATE TABLE Staff (
    id varchar(255) NOT NULL,
    name varchar(255) NOT NULL
    
);

INSERT INTO Staff (id,name) VALUES ('1994A', 'omar');
