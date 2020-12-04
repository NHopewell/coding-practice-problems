SELECT
	c.CustomerID,
    c.CompanyName,
    o.OrderID,
	sum(od.UnitPrice * od.Quantity) AS TotalOrderAmount
FROM Customers c
	JOIN Orders o
		ON c.CustomerID = o.CustomerID
	JOIN OrderDetails od
		ON o.OrderID = od.OrderID
WHERE 
	o.OrderDate BETWEEN '2016-01-01' AND '2016-12-31'
    /*  
    CANT USE WHERE WITH GROUP BY - notice orderdate above is not in groupby 
    
		AND
		CASE 
			WHEN
				( sum(od.UnitPrice * od.Quantity) - (sum(od.UnitPrice * od.Quantity)*(od.Discount))) >= 10000 then 1 
            else 0 
		END = 1 
	*/
GROUP BY 
	c.CustomerID, 
    c.CompanyName, 
    o.OrderID, 
    od.Discount
HAVING ( sum(od.UnitPrice * od.Quantity) - (sum(od.UnitPrice * od.Quantity)*(od.Discount)) ) > 10000
ORDER BY TotalOrderAmount DESC;