-- 1. Todos los libros y sus autores
SELECT b.ID AS BookID, b.Name AS BookName, a.Name AS AuthorName
FROM Books b
LEFT JOIN Authors a ON b.Author = a.ID;

-- 2. Libros sin autor
SELECT * FROM Books 
WHERE Author IS NULL;

-- 3. Autores sin libros
SELECT a.ID, a.Name FROM Authors a
LEFT JOIN Books b ON a.ID = b.Author
WHERE b.ID IS NULL;

-- 4. Libros que han sido rentados
SELECT DISTINCT b.ID, b.Name FROM Books b
JOIN Rents r ON b.ID = r.BookID;

-- 5. Libros que nunca han sido rentados
SELECT b.ID, b.Name FROM Books b
LEFT JOIN Rents r ON b.ID = r.BookID
WHERE r.ID IS NULL;

-- 6. Clientes que nunca han rentado un libro
SELECT c.ID, c.Name, c.Email FROM Customers c
LEFT JOIN Rents r ON c.ID = r.CustomerID
WHERE r.ID IS NULL;

-- 7. Libros rentados en estado "Overdue"
SELECT DISTINCT b.ID, b.Name, r.State FROM Books b
JOIN Rents r ON b.ID = r.BookID
WHERE r.State = 'Overdue';