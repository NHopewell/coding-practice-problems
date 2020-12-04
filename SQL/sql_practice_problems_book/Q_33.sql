SELECT
	c.CustomerID,
    c.CompanyName,
	sum(od.UnitPrice * od.Quantity) AS TotalOrderAmount
FROM Customers c
	JOIN Orders o
		ON c.CustomerID = o.CustomerID
	JOIN OrderDetails od
		ON o.OrderID = od.OrderID
WHERE 
	o.OrderDate BETWEEN '2016-01-01' AND '2016-12-31'
GROUP BY 
	c.CustomerID
HAVING TotalOrderAmount > 15000
ORDER BY TotalOrderAmount DESC;