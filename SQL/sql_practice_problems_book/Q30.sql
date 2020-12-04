SELECT
	c.CustomerId
    , o.CustomerId
FROM Customers c
LEFT JOIN Orders o
	ON c.CustomerId = o.CustomerId
WHERE c.CustomerId NOT IN (SELECT CustomerId from Orders)