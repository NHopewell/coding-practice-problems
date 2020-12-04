SELECT c.CategoryName, COUNT(DISTINCT(p.ProductName)) AS TotalProducts
FROM Categories c
JOIN Products p
ON c.CategoryID = p.CategoryID
GROUP BY 1
ORDER BY 2 DESC;