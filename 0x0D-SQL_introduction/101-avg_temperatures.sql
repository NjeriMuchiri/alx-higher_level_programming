-- Displays the average temperature (Fahrenheit)
-- importing in hbtn_0c_0 database 
SELECT city, AVG(value) AS avg_temper
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
