-- Displays the average temperature (Fahrenheit)
-- by city ordered in a descending order
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
