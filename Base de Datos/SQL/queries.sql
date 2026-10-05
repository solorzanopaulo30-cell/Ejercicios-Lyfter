-- SQLite


-- 3. Alter agregar telefono y codigo de empleado (Tiene que ser una sola vez)
ALTER TABLE Invoices ADD COLUMN Buyer_Phone TEXT;
ALTER TABLE Invoices ADD COLUMN Employee_Code INT;

PRAGMA table_info(Invoices);

-- 4.1 Todos los productos
SELECT * FROM Products;

-- 4.2 Productos con precio mayor a 50000 (en centavos: 5000000)
SELECT * FROM Products WHERE Price_Cents > 5000000;

-- 4.3 Obtenga todas las compras de un mismo producto por id.
SELECT * FROM Products_Per_Invoice WHERE Product_Code = 1;

-- 4.4 Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT Product_Code, SUM(Quantity) FROM Products_Per_Invoice GROUP BY Product_Code;

-- 4.5 Obtenga todas las facturas realizadas por el mismo comprador
SELECT * FROM Invoices WHERE User_ID = 1;

-- 4.6  Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT * FROM Invoices ORDER BY Total_Amount_Cents DESC;

-- 4.7 Obtenga una sola factura por número de factura.
SELECT * FROM Invoices WHERE Invoice_Number = 2;

