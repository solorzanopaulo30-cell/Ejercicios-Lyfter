-- SQLite
PRAGMA foreign_keys = ON;


DELETE FROM Reviews;
DELETE FROM Products_Per_Invoice;
DELETE FROM Invoices;
DELETE FROM Products;
DELETE FROM Categories;
DELETE FROM Payment_Methods;
DELETE FROM Users;
DELETE FROM sqlite_sequence;

INSERT INTO Users (Full_Name, Email, Registration_Date) VALUES
('Ana', 'ana@mail.com', '2026-10-01'),
('Luis', 'luis@mail.com', '2026-10-02');

INSERT INTO Payment_Methods (Method_Type, Bank_Name) VALUES
('Tarjeta', 'BAC'),
('PayPal', NULL);

INSERT INTO Categories (Name, Description) VALUES
('Periféricos', 'Teclados, mouses y accesorios para la computadora'),
('Monitores', 'Pantallas de distintos tamaños y resoluciones'),
('Accesorios', 'Cables, bases y otros complementos');

INSERT INTO Products (Code, Name, Price_Cents, Entry, Brand, Stock) VALUES
(1, 'Teclado', 2500000, '2026-09-01', 'Logitech', 10),
(2, 'Monitor', 8000000, '2026-09-01', 'Samsung', 5),
(3, 'Mouse', 1200000, '2026-09-01', 'Logitech', 20);

INSERT INTO Invoices (Invoice_Number, Purchase_Date, Total_Amount_Cents, User_ID, Payment_Method_ID, Buyer_Phone, Employee_Code) VALUES
(1, '2026-10-03', 10400000, 1, 1, '+506 7000-0001', 101),
(2, '2026-10-04', 2500000, 1, 2, '+506 7000-0001', 102),
(3, '2026-10-05', 6200000, 2, 1, '+506 7000-0002', 101);

INSERT INTO Products_Per_Invoice (Quantity, Total_Amount_Cents, Invoice_Number, Product_Code) VALUES
(1, 8000000, 1, 2),
(2, 2400000, 1, 3),
(1, 2500000, 2, 1),
(2, 5000000, 3, 1),
(1, 1200000, 3, 3);

INSERT INTO Products (Code, Name, Price_Cents, Entry, Brand, Stock) VALUES
(4, 'Apple Magic Mouse', 6500000, '2026-09-10', 'Apple', 15),
(5, 'Cable USB-C', 450000, '2026-09-10', 'Anker', 50),
(6, 'Adaptador', 650000, '2026-09-10', 'SpaceX', 50),
(7, 'Double Screen Milk', 450000, '2026-09-10', 'Dos Pinos', 50),
(8, 'Duele schock', 450000, '2026-09-10', 'Alex Syntec', 50),
(9, 'Cable Light', 250000, '2026-09-10', 'F50', 50),
(10, 'Switch 2', 950000, '2026-09-10', 'Nintendo', 50);