-- 1. 비 진성고객 리스트


SELECT Customers.*
FROM Customers
	LEFT JOIN Orders
    ON Orders.CustomerID =  Customers.CustomerID
GROUP BY Customers.CustomerID
HAVING COUNT(Orders.OrderID) <= 1;

--  2. 판매자 중 수익 낮은 순위자 3명 정보, 총 판매액

SELECT Suppliers.*, ALLs.AllPrice
FROM Suppliers
LEFT JOIN (
    SELECT OrderDetails.ProductID, SUM(Products.Price) AS AllPrice
    FROM OrderDetails
    LEFT JOIN Products 
    ON Products.ProductID = OrderDetails.ProductID
    GROUP BY OrderDetails.ProductID
) AS ALLs ON ALLs.ProductID = Suppliers.SupplierID
ORDER BY ALLs.AllPrice
LIMIT 3
;


-- 3. 배송 회사별 총 배송 건수와 총 제품 금액 정보

SELECT Orders.ShipperID,SUM(ALLOders.ALLPrice) AS 	ShipperALLPrice
FROM Orders
LEFT JOIN (SELECT OrderDetails.OrderID, SUM(Products.Price) AS ALLPrice
FROM OrderDetails
LEFT JOIN Products ON Products.ProductID = OrderDetails.ProductID
GROUP BY OrderID) ALLOders ON ALLOders.OrderID = Orders.OrderID
GROUP BY ShipperID


-- 4. 제품 회사별 총 판매액과 정보

SELECT Suppliers.*,  SUM(Products.Price*SALES.CNT) AS ALLPrice
FROM Suppliers
LEFT JOIN Products
ON Products.SupplierID = Suppliers.SupplierID
LEFT JOIN (
          SELECT ProductID, COUNT(ProductID) AS CNT
          FROM OrderDetails
          GROUP BY ProductID) AS SALES ON SALES.ProductID=Products.ProductID
GROUP BY SupplierID


-- 5. 카테고리별 상품 ID, 가격정보

SELECT Categories.CategoryID, Products.Price*ProductSales.CNT AS CATESUM
FROM Categories
LEFT JOIN Products
ON Products.CategoryID = Categories.CategoryID
LEFT JOIN (SELECT ProductID, COUNT(ProductID) AS CNT
          FROM OrderDetails
          GROUP BY ProductID) AS ProductSales ON ProductSales.ProductID = Products.ProductID
GROUP BY CategoryID