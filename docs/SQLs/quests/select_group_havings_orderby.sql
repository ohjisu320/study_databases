-- quest refer : https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_groupby
-- quest question
/*
- Table : Products
+ 조건 1 : CategoryID 가 10개 이상
- Table : Customers, Orders
+ 조건 2 : 주문 갯수가 5개 이상인 CustomerName 찾기
- Table : Orders, ?
+ 조건 3 : 20개 이상 주문 받은 회사 LastName 과 갯수
*/

-- 조건1 : CategoryID 가 10개 이상
SELECT COUNT(CategoryID) AS CNT, CategoryID
FROM Products
GROUP BY CategoryID
HAVING COUNT(CategoryID) >= 10;
-- Number of Records: 5 / CategoryID : 1, 2, 3, 4, 8

-- 조건2 : 주문 갯수가 5개 이상인 CustomerName 찾기
-- table : Orders
SELECT COUNT(CustomerID) AS CNT, CustomerID
FROM Orders
GROUP BY CustomerID
HAVING COUNT(CustomerID) >= 5
ORDER BY CustomerID ASC;
-- Number of Records: 9 / CustomerID : 20, 37, 41, 46, 51, 63, 65, 75, 87
-- table : Customers
SELECT CustomerID, CustomerName
FROM Customers
WHERE CustomerID IN (20, 37, 41, 46, 51, 63, 65, 75, 87);
-- Number of Records: 9 / CustomerName : Ernst Handel, Hungry Owl All-Night Grocers, La maison d'Asie, LILA-Supermercado, Mère Paillarde, QUICK-Stop, Rattlesnake Canyon Grocery, Split Rail Beer & Ale, Wartian Herkku

-- 조건 3 : 20개 이상 주문 받은 회사 LastName 과 갯수
-- table : Orders
SELECT COUNT(EmployeeID) AS CNT, EmployeeID
FROM Orders
GROUP BY EmployeeID
HAVING COUNT(EmployeeID) >= 20
ORDER BY EmployeeID ASC;
-- Number of Records: 5 / EmployeeID : 1, 2, 3, 4, 8
-- table : Employees
SELECT EmployeeID, LastName
FROM Employees
WHERE EmployeeID IN (1, 2, 3, 4, 8);
-- Number of Records: 5 / LastName : Davolio, Fuller, Leverling, Peacock, Callahan