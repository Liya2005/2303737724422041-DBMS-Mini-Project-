CREATE DATABASE hotels;

USE hotels;

CREATE TABLE hotels_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    capacity INT NOT NULL,
    location VARCHAR(100)
);
INSERT INTO submarine_details (name, description, capacity, location)
VALUES 
('Nautilus', 'Advanced nuclear submarine.', 150, 'Pacific Ocean'),
('Deep Explorer', 'Designed for deep-sea exploration.', 50, 'Indian Ocean'),
('Aegir', 'State-of-the-art stealth submarine.', 200, 'Atlantic Ocean'),
('Poseidon', 'Equipped with high-tech sensors.', 180, 'Arctic Ocean'),
('Sea Wolf', 'Military-grade attack submarine.', 120, 'Mediterranean Sea');

select * from submarine_details;