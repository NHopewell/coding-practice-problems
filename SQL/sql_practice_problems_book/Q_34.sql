SELECT
	c.CustomerID,
    c.CompanyName,
	sum( od.UnitPrice * od.Quantity ) AS TotalWithoutDiscount,
	sum( (od.UnitPrice * od.Quantity) * (1 - od.Discount ) ) AS TotalWithDiscount
FROM Customers c
	JOIN Orders o
		ON c.CustomerID = o.CustomerID
	JOIN OrderDetails od
		ON o.OrderID = od.OrderID
WHERE 
	o.OrderDate BETWEEN '2016-01-01' AND '2016-12-31'
GROUP BY 
	c.CustomerID
HAVING TotalWithDiscount > 10000
ORDER BY TotalWithDiscount DESC;
