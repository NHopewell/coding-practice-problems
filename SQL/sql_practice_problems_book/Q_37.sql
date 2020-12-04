SELECT 
	OrderID
FROM OrderDetails
ORDER BY 
	rand()
LIMIT 10;