DROP DATABASE IF EXISTS open_food_facts;
CREATE DATABASE open_food_facts;
USE open_food_facts;
CREATE TABLE category(
    iD INT NOT NULL AUTO_INCREMENT,
    name VARCHAR (150) NOT NULL,
    url VARCHAR (255) NOT NULL,
    PRIMARY KEY (iD)
);

CREATE TABLE product(
    iD INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    brand VARCHAR(150) NOT NULL,
    nutri_score CHAR(1) NOT NULL,
    calories DECIMAL(5,2) NOT NULL,
    sugars DECIMAL(5,2) NOT NULL,
    salts DECIMAL(5,2) NOT NULL,
    lipids DECIMAL(5,2) NOT NULL,
    proteins DECIMAL(5,2) NOT NULL,
    description longtext,
    location_available VARCHAR(150) NOT NULL,
    url_image VARCHAR(255) NOT NULL,
    url_page VARCHAR(255) NOT NULL,
    stores VARCHAR(255) NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (iD)
);
CREATE TABLE favourite(
    iD INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    brand VARCHAR(150) NOT NULL,
    nutri_score CHAR(1) NOT NULL,
    calories DECIMAL(5,2) NOT NULL,
    sugars DECIMAL(5,2) NOT NULL,
    salts DECIMAL(5,2) NOT NULL,
    lipids DECIMAL(5,2) NOT NULL,
    proteins DECIMAL(5,2) NOT NULL,
    description longtext,
    location_available VARCHAR(150) NOT NULL,
    url_image VARCHAR(255) NOT NULL,
    url_page VARCHAR(255) NOT NULL,
    category_id INT NOT NULL,
    stores VARCHAR(255) NOT NULL,
    PRIMARY KEY (iD)
);
ALTER TABLE product ADD CONSTRAINT product_fk
FOREIGN KEY (category_id)
REFERENCES category (iD)
ON DELETE CASCADE
ON UPDATE CASCADE;
ALTER TABLE favourite ADD CONSTRAINT favourite_fk
FOREIGN KEY (category_id)
REFERENCES category (iD)
ON DELETE CASCADE
ON UPDATE CASCADE;
