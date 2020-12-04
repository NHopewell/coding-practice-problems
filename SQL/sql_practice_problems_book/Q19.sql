SELECT
	o.OrderId
    , date(o.OrderDate)
    , s.CompanyName AS Shipper
FROM Orders o
JOIN Shippers s
	ON o.ShipVia = s.ShipperId
WHERE OrderId < 10270
ORDER BY OrderId;