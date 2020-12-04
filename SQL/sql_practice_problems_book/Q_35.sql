/* THIS DOES NOT ACTUALLY WORK  BECAUSE MAX(orderdate) wont neccessarily return last day of month, just latest date of order, even if its not on the last day)
SELECT
	e.EmployeeID,
    o.OrderID,
    o.OrderDate
FROM Employees e
	JOIN Orders o
		ON e.EmployeeID = o.EmployeeID
WHERE o.OrderDate IN 
(
	SELECT MAX(OrderDate)
    FROM Orders
    GROUP BY
		MONTH(OrderDate),
        YEAR(OrderDate)
)
ORDER BY 
	e.EmployeeID,
	o.OrderID;
*/
SELECT
	e.EmployeeID,
    o.OrderID,
    o.OrderDate
FROM Employees e
	JOIN Orders o
		ON e.EmployeeID = o.EmployeeID
WHERE o.OrderDate = LAST_DAY(o.OrderDate)
ORDER BY 
	e.EmployeeID,
	o.OrderID;
