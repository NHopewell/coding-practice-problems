SELECT 
	OrderID,
	COUNT(ProductID) AS TotalOrderDetails
FROM OrderDetails
GROUP BY OrderID
ORDER BY 
	TotalOrderDetails DESC
LIMIT 10;