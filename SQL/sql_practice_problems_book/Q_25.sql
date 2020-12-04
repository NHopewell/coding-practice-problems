SELECT ShipCountry, ( SUM(Freight)/COUNT(OrderID) ) AS AverageFrieght
FROM Orders
GROUP BY ShipCountry
ORDER BY 2 DESC
LIMIT 3;

