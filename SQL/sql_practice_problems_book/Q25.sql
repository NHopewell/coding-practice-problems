SELECT
	ShipCountry
    , avg(Freight)
FROM Orders
GROUP BY 1
ORDER BY 2 DESC
LIMIT 3;