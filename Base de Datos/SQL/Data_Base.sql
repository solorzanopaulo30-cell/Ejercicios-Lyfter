-- SQLite
PRAGMA foreign_keys = ON;
-- LIMITANTE: SQLite no revisa las llaves foráneas por defecto, así que permite guardar
-- datos que apuntan a filas que no existen (por ejemplo, una factura de un usuario inexistente).
-- SOLUCIÓN: activar la revisión con PRAGMA en cada conexión a la base de datos.



DROP TABLE IF EXISTS Reviews;
DROP TABLE IF EXISTS Products_Per_Cart;
DROP TABLE IF EXISTS Products_Per_Invoice;
DROP TABLE IF EXISTS Invoices;
DROP TABLE IF EXISTS Shopping_Cart;
DROP TABLE IF EXISTS Payment_Methods;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Products;


-- LIMITANTE: SQLite no tiene un tipo DECIMAL real, guarda los números con decimales de forma aproximada.
-- SOLUCIÓN: el dinero se guarda en centavos como INTEGER (₡1250.50 = 125050).
CREATE TABLE Products (
    Code INT PRIMARY KEY,
    Name TEXT NOT NULL,
    Price_Cents INTEGER NOT NULL,
    Entry DATE NOT NULL, 
    Brand TEXT NOT NULL,
    Stock INT NOT NULL
);

-- LIMITANTE: en SQLite, "INT PRIMARY KEY" no genera el ID automáticamente.
-- SOLUCIÓN: usar "INTEGER PRIMARY KEY AUTOINCREMENT"
CREATE TABLE Users (
    User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Full_Name TEXT NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Registration_Date DATE NOT NULL
);


CREATE TABLE Payment_Methods (
    Method_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Method_Type VARCHAR(50) NOT NULL,
    Bank_Name TEXT 
);


CREATE TABLE Invoices (
    Invoice_Number INT PRIMARY KEY,
    Purchase_Date DATE NOT NULL,
    Total_Amount_Cents INTEGER NOT NULL,
    User_ID INT NOT NULL,
    Payment_Method_ID INT NOT NULL,
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID),
    FOREIGN key (Payment_Method_ID) REFERENCES Payment_Methods(Method_ID)
);


CREATE TABLE Products_Per_Invoice (
    Quantity INT DEFAULT 0,
    Total_Amount_Cents INTEGER NOT NULL,
    Invoice_Number INT NOT NULL,
    Product_Code INT NOT NULL,
    PRIMARY KEY (Invoice_Number, Product_Code),
    FOREIGN KEY (Invoice_number) REFERENCES Invoices(invoice_number),
    FOREIGN KEY (Product_code) REFERENCES Products(code)
);


CREATE TABLE Shopping_Cart (
    Buyer_Email VARCHAR(255) PRIMARY KEY
);


CREATE TABLE Products_Per_Cart (
    Buyer_Email VARCHAR(255) NOT NULL,
    Product_Code INTEGER NOT NULL,
    PRIMARY KEY (Buyer_Email, Product_code),
    FOREIGN KEY (Buyer_Email) REFERENCES Shopping_Cart(Buyer_email),
    FOREIGN KEY (Product_Code) REFERENCES Products(Code)
);


CREATE TABLE Reviews (
    Review_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Product_CODE INT NOT NULL,
    Comment VARCHAR(255) NOT NULL,
    Rating INTEGER NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    Date DATE NOT NULL,
    User_ID INTEGER NOT NULL,
    FOREIGN KEY (Product_Code) REFERENCES Products(Code),
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
);


