SET SQL_SAFE_UPDATES = 0;

CREATE DATABASE IF NOT EXISTS hospital1;
USE hospital1;
show tables;
CREATE TABLE IF NOT EXISTS Employee_hospital (
    name VARCHAR(250) NOT NULL,
    id VARCHAR(50) PRIMARY KEY,   
    job varchar(250)NOT NULL
);

CREATE TABLE IF NOT EXISTS Doctor_hospital (
    name VARCHAR(250) NOT NULL,
    id VARCHAR(50) PRIMARY KEY,   
    specialization varchar(250)NOT NULL
);


CREATE TABLE IF NOT EXISTS Manager_hospital (
    name VARCHAR(250) NOT NULL,
    id VARCHAR(50) PRIMARY KEY
    );


CREATE TABLE IF NOT EXISTS DataEntry_hospital (

    name VARCHAR(250) NOT NULL,
    id VARCHAR(50) PRIMARY KEY
);

CREATE TABLE prescriptions (
    id VARCHAR(50) PRIMARY KEY,
    medication VARCHAR(255),
    dosage VARCHAR(100),
    doctor VARCHAR(255),
    date_prescribed DATE
);

CREATE TABLE IF NOT EXISTS Patient_hospital (
	name VARCHAR(250) NOT NULL,
    id VARCHAR(50) PRIMARY KEY,  
    age INT NOT NULL,
    Ailment varchar (250)NOT NULL
);

SELECT * FROM prescriptions;

INSERT INTO Doctor (id, name, age, salary, department) 
VALUES ('003', 'Ahmed', 35, 35000, 'Cardiology');


INSERT INTO Manager (id, name, age, salary, department) 
VALUES ('015', 'Ibrahim', 29, 25000, 'Administration');


INSERT INTO DataEntry (id, name, age, salary) 
VALUES ('022', 'Kamal', 23, 15000);


INSERT INTO Patient_hospital(id, name, age, Ailment) 
VALUES ('096', 'mahmoud', 60 , 'illness');

INSERT INTO prescriptions (id, medication,dosage, doctor,date_prescribed ) 
VALUES ('3', 'cold', "2 times" ,"osama" ,CURDATE());

INSERT INTO prescriptions (id, medication, dosage, doctor,date_prescribed ) 
VALUES ('2', 'hot', "3 times" , "mido",CURDATE());

INSERT INTO prescriptions (id, medication, dosage, doctor,date_prescribed ) 
VALUES ('1', 'virus', "4 times" , "ahmed",CURDATE());

DELETE FROM Patient_hospital WHERE id <10000000

