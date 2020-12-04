Select
	 Customers.CustomerID
	 ,Orders.CustomerID
	 -- ,Orders.EmployeeID
 From Customers
	left join Orders
		on Orders.CustomerID = Customers.CustomerID
		and Orders.EmployeeID = 4
WHERE
  Orders.CustomerID is null;

/*  OR 

Select CustomerID
From Customers
Where CustomerID not in (select CustomerID from Orders where EmployeeID = 4);
*/