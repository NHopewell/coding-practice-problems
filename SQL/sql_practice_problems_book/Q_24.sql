SELECT 
	CustomerID, 
    CompanyName, 
    Region
FROM Customers
GROUP BY Region, CustomerID
ORDER BY ( CASE 
	WHEN Region IS NULL then 1
		else 0
    END),
    Region,
    CustomerID;

