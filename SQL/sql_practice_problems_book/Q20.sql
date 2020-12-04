SELECT
	distinct(c.CategoryName) as CategoryName
    , count(p.ProductId) as TotalProducts
FROM Categories c
JOIN Products p
	ON c.CategoryID = p.CategoryID
GROUP BY 1
ORDER BY 2 DESC;