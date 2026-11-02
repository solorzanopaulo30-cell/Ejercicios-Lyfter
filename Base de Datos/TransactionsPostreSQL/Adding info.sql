TRUNCATE TABLE Bills_Products, Bills, Products, Users RESTART IDENTITY;

INSERT INTO Users (Name, Email) VALUES
('Ana Rivera', 'ana@mail.com'),
('Luis Mendez', 'luis@mail.com');

INSERT INTO Products (Name, Price, Stock) VALUES
('Teclado', 25000, 10),
('Mouse', 12000, 20),
('Monitor', 80000, 2);

SELECT * FROM Users;
SELECT * FROM Products;