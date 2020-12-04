SELECT ShipCountry, ( SUM(Freight)/COUNT(OrderID) ) AS AverageFrieght
FROM Orders
WHERE OrderDate LIKE '2015%'
GROUP BY ShipCountry
ORDER BY 2 DESC
LIMIT 3;

# can also use DATE() - notice the column is a datetime not a date
