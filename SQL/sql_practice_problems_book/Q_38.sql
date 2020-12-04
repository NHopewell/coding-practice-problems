SELECT 
	OrderID
FROM OrderDetails
WHERE
	Quantity >= 60
GROUP BY 
	OrderID, 
    Quantity
HAVING COUNT(OrderID) >= 2
