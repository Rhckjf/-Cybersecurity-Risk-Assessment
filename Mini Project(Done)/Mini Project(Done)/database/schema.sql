CREATE DATABASE IF NOT EXISTS risk_assessment;
USE risk_assessment;

CREATE TABLE assets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    criticality ENUM('Low', 'Medium', 'High') NOT NULL
);

CREATE TABLE threats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    likelihood ENUM('Low', 'Medium', 'High') NOT NULL,
    impact ENUM('Low', 'Medium', 'High') NOT NULL
);

CREATE TABLE risks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    asset_id INT,
    threat_id INT,
    risk_level ENUM('Low', 'Medium', 'High'),
    FOREIGN KEY (asset_id) REFERENCES assets(id),
    FOREIGN KEY (threat_id) REFERENCES threats(id)
);