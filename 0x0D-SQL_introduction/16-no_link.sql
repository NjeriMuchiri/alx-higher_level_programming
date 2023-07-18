-- lists al records of the table second_table
--lists all records of the table second_table who have the name value
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL ORDER BY `score` DESC;
