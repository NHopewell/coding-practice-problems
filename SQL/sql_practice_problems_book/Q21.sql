SELECT
	Country
    , City
    , count(CustomerId) as TotalCustomers
FROM Customers
GROUP BY Country, City
ORDER BY TotalCustomers DESC;