-- Converts hbth_0c_0 database to UTF8
-- collate utf8mb4_unicode_ci in your MYSQL server
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
