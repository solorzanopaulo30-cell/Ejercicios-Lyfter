CREATE TABLE `Products`(
    `Code` INT NOT NULL,
    `Name` TEXT NOT NULL,
    `Price` DECIMAL(8, 2) NOT NULL,
    `Entry` DATE NOT NULL,
    `Brand` TEXT NOT NULL,
    `Stock` INT NOT NULL,
    PRIMARY KEY(`Code`)
);
CREATE TABLE `Users`(
    `User ID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Full Name` TEXT NOT NULL,
    `Email` VARCHAR(255) NOT NULL UNIQUE,
    `Registration Date` DATE NOT NULL
);
CREATE TABLE `Payment Methods`(
    `Method ID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Method Type` VARCHAR(255) NOT NULL,
    `Bank Name` TEXT NULL
);
CREATE TABLE `Invoices`(
    `Invoice Number` INT NOT NULL,
    `Purchase Date` DATE NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL,
    `User ID` INT UNSIGNED NOT NULL,
    `Payment Method ID` INT UNSIGNED NOT NULL,
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
CREATE TABLE `Reviews`(
    `Review ID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Product Code` INT NOT NULL,
    `Comment` VARCHAR(255) NOT NULL,
    `Rating (1-5)` INT NOT NULL,
    `Date` DATE NOT NULL,
    `User ID` INT UNSIGNED NOT NULL,
    CHECK (`Rating (1-5)` BETWEEN 1 AND 5)
);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_user id_foreign` FOREIGN KEY(`User ID`) REFERENCES `Users`(`User ID`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_payment method id_foreign` FOREIGN KEY(`Payment Method ID`) REFERENCES `Payment Methods`(`Method ID`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_invoice number_foreign` FOREIGN KEY(`Invoice Number`) REFERENCES `Invoices`(`Invoice Number`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Products Per Cart` ADD CONSTRAINT `products per cart_buyer email_foreign` FOREIGN KEY(`Buyer email`) REFERENCES `Shopping Cart`(`Buyer email`);
ALTER TABLE
    `Products Per Cart` ADD CONSTRAINT `products per cart_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Reviews` ADD CONSTRAINT `reviews_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Reviews` ADD CONSTRAINT `reviews_user id_foreign` FOREIGN KEY(`User ID`) REFERENCES `Users`(`User ID`);