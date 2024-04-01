
-- - Table : Customers, Orders
-- + 조건 : 주문 갯수가 5개 이상인 CustomerName 찾기

SELECT CTM.CustomerName
FROM (
        SELECT CustomerName, CustomerID
        FROM Customers
        WHERE CustomerID IN (
            SELECT CustomerID
            FROM Orders
            GROUP BY CustomerID
            HAVING COUNT(CustomerID) >= 5
            ORDER BY CustomerID ASC
            )
    ) AS CTM
;

-- - Table : Orders
-- + 조건 : 주문 갯수가 20개 이상인 회사 LastName과 갯수

SELECT EMPLY.LastName
FROM (
	SELECT LastName, EmployeeID
    FROM Employees
    WHERE EmployeeID IN (
                    SELECT EmployeeID
                    FROM Orders
                    GROUP BY EmployeeID
                    HAVING COUNT(EmployeeID) >=20
)
)AS EMPLY
;

-- - Table : Suppliers
-- + 조건 : CategoryID를 가장 많이 제공 상위 2개 회사 정보

SELECT *
FROM Suppliers
WHERE SupplierID IN (
    SELECT SPID.SupplierID
    FROM (
    SELECT SupplierID, COUNT(CategoryID)
    FROM Products
    GROUP BY CategoryID
    ORDER BY COUNT(CategoryID) DESC
    LIMIT 2
) AS SPID
);