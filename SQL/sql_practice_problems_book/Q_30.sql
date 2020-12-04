SELECT
	c.CustomerID AS Customer_CustomerID,
    o.CustomerID AS Orders_CustomerID
FROM Customers c
    LEFT JOIN Orders o
		ON c.CustomerID = o.CustomerID
WHERE c.CustomerID NOT IN (
	SELECT CustomerID from Orders);
