CREATE DATABASE Open_Food_Facts;

USE Open_Food_Facts;

CREATE TABLE category(
    iD INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    CONSTRAINT id PRIMARY KEY (id)
);

CREATE TABLE product(
    iD INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    nutri_score CHAR(1) NOT NULL,
    calories TINYINT NOT NULL,
    sugars TINYINT NOT NULL,
    salts TINYINT NOT NULL,
    lipids TINYINT NOT NULL,
    proteins TINYINT NOT NULL,
    category VARCHAR(150) NOT NULL,
    description longtext NOT NULL,
    location_available VARCHAR(150) NOT NULL,
    url_image VARCHAR(255) NOT NULL,
    CONSTRAINT id PRIMARY KEY (id)
);

CREATE TABLE favourite(
    iD INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    nutri_score CHAR(1) NOT NULL,
    calories TINYINT NOT NULL,
    sugars TINYINT NOT NULL,
    salts TINYINT NOT NULL,
    lipids TINYINT NOT NULL,
    proteins TINYINT NOT NULL,
    category VARCHAR(150) NOT NULL,
    description longtext NOT NULL,
    location_available VARCHAR(150) NOT NULL,
    url_image VARCHAR(255) NOT NULL,
    CONSTRAINT id PRIMARY KEY (id)
);