-- SQLite

-- 2. Agrupamiento y conteo cruzado
-- Obtenga el número total de veces que cada cliente ha rentado un libro
-- Ordene de mayor a menor y limite el resultado a los 3 clientes más activos
SELECT Customers.Name AS Cliente, COUNT(*) AS Total
FROM Rents
JOIN Customers ON Rents.CustomerID = Customers.ID
GROUP BY Customers.ID
ORDER BY Total DESC
LIMIT 3;

-- 3. Consulta con múltiples JOINS anidados
-- Nombre del cliente, nombre del libro, nombre del autor y estado del alquiler
-- Debe manejar el caso en que un libro no tenga autor (por eso el LEFT JOIN)
SELECT Customers.Name AS Cliente, Books.Name AS Libro, Authors.Name AS Autor, Rents.State AS Estado
FROM Rents
JOIN Customers ON Rents.CustomerID = Customers.ID
JOIN Books ON Rents.BookID = Books.ID
LEFT JOIN Authors ON Books.Author = Authors.ID;