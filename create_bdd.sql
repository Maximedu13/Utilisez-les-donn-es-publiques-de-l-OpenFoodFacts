DROP DATABASE IF EXISTS open_food_facts;
CREATE DATABASE open_food_facts;
USE open_food_facts;
CREATE TABLE category(
    iD INT NOT NULL ,
    name VARCHAR (150) NOT NULL,
    url VARCHAR (255) NOT NULL,
    PRIMARY KEY (iD)
);
CREATE TABLE product(
    iD INT NOT NULL,
    name VARCHAR (150) NOT NULL,
    brand VARCHAR (150) NOT NULL,
    nutri_score CHAR (1) NOT NULL,
    calories INT NOT NULL,
    sugars TINYINT NOT NULL,
    salts TINYINT NOT NULL,
    lipids TINYINT NOT NULL,
    proteins TINYINT NOT NULL,
    description longtext NOT NULL,
    location_available VARCHAR (150) NOT NULL,
    url_image VARCHAR (255) NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY(iD)
);
CREATE TABLE favourite(
    iD INT NOT NULL,
    name VARCHAR(150) NOT NULL,
    brand VARCHAR (150) NOT NULL,
    nutri_score CHAR(1) NOT NULL,
    calories INT NOT NULL,
    sugars TINYINT NOT NULL,
    salts TINYINT NOT NULL,
    lipids TINYINT NOT NULL,
    proteins TINYINT NOT NULL,
    description longtext NOT NULL,
    location_available VARCHAR(150) NOT NULL,
    url_image VARCHAR(255) NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY(iD)
);
ALTER TABLE product ADD CONSTRAINT product_fk
FOREIGN KEY (category_id)
REFERENCES category (iD)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
ALTER TABLE favourite ADD CONSTRAINT favourite_fk
FOREIGN KEY (category_id)
REFERENCES category (iD)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
SET FOREIGN_KEY_CHECKS=0; -- to disable them
SET FOREIGN_KEY_CHECKS=1; -- to re-enable them
