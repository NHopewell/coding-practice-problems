SELECT Country, City, COUNT(DISTINCT(CustomerID)) AS TotalCustomers
FROM Customers
GROUP BY Country, City
ORDER BY 3 DESC;