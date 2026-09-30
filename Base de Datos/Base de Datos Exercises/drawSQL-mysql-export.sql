CREATE TABLE `Products`(
    `Code` INT NOT NULL,
    `Name` TEXT NOT NULL,
    `Price` DECIMAL(8, 2) NOT NULL,
    `Entry` DATE NOT NULL,
    `Brand` TEXT NOT NULL,
    `Stock` INT NOT NULL,
    PRIMARY KEY(`Code`)
);
CREATE TABLE `Invoices`(
    `Invoice Number` INT NOT NULL,
    `Purchase Date` DATE NOT NULL,
    `Buyer email` VARCHAR(255) NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL,
    PRIMARY KEY(`Invoice Number`)
);
CREATE TABLE `Products Per Invoice`(
    `Quantity` INT NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL,
    `Invoice Number` INT NOT NULL,
    `Product Code` INT NOT NULL,
    PRIMARY KEY(`Invoice Number`, `Product Code`)
);
CREATE TABLE `Shopping Cart`(
    `Buyer email` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`Buyer email`)
);
CREATE TABLE `Products Per Cart`(
    `Buyer email` VARCHAR(255) NOT NULL,
    `Product Code` INT NOT NULL,
    PRIMARY KEY(`Buyer email`, `Product Code`)
);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_invoice number_foreign` FOREIGN KEY(`Invoice Number`) REFERENCES `Invoices`(`Invoice Number`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Products Per Cart` ADD CONSTRAINT `products per cart_buyer email_foreign` FOREIGN KEY(`Buyer email`) REFERENCES `Shopping Cart`(`Buyer email`);
ALTER TABLE
    `Products Per Cart` ADD CONSTRAINT `products per cart_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Products`(`Code`);