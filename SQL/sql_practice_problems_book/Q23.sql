SELECT
	ProductId
    , ProductName as 'Product Name'
    , UnitsInStock as ' Units In Stock'
    , UnitsOnOrder as 'Units On Order'
    , ReorderLevel as 'Reorder Level'
    , Discontinued
FROM Products
WHERE ((UnitsInStock + UnitsOnOrder) <= ReorderLevel) and Discontinued = 0;