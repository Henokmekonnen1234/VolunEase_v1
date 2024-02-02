-- creates database for volunease
CREATE DATABASE IF NOT EXISTS volunease_db;
CREATE USER IF NOT EXISTS 'volunease_user'@'localhost'
IDENTIFIED BY 'volunease33455';
GRANT ALL PRIVILEGES ON `volunease_db`.* TO 'volunease_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'volunease_user'@'localhost';