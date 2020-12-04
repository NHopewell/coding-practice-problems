SELECT
	ProductId
    , ProductName
    , UnitsInStock
    , ReorderLevel
FROM Products
WHERE UnitsInStock <= ReorderLevel
ORDER BY ProductId;