SELECT OrderID, Freight
FROM Orders
WHERE ShipCountry = 'France'
ORDER BY 2 DESC
LIMIT 1;

# can also use DATE() - notice the column is a datetime not a date
