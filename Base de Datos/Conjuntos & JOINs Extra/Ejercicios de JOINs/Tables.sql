-- SQLite
PRAGMA foreign_keys = ON;


------------------------------------------------------------------------


DROP TABLE IF EXISTS Rents;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Authors;

------------------------------------------------------------------------


CREATE TABLE Authors (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(25) NOT NULL
);


CREATE TABLE Customers (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(25),
    Email VARCHAR(25)
);


CREATE TABLE Books (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(25) NOT NULL,
    Author INT,
    FOREIGN KEY (Author) REFERENCES Authors(ID)
);


CREATE TABLE Rents (
    ID INTEGER PRIMARY KEY,
    BookID INT NOT NULL,
    CustomerID INT NOT NULL,
    State VARCHAR(25) NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Books (ID),
    FOREIGN KEY (CustomerID) REFERENCES Customers (ID)
);