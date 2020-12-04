SELECT 
	ShipCountry
    , avg(Freight) as AverageFreight
FROM Orders
WHERE year(OrderDate) = 2015
GROUP BY ShipCountry
ORDER BY AverageFreight DESC
LIMIT 3;