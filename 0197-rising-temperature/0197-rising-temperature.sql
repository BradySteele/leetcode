# Write your MySQL query statement below
SELECT Weather.Id AS Id
FROM Weather
JOIN Weather AS Yesterday
ON DATEDIFF(Weather.RecordDate, Yesterday.RecordDate) = 1
WHERE Weather.Temperature > Yesterday.Temperature;