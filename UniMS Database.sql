create database UniMs

use UniMs

create table LoginP_ (ID int NOt NULL,uname varchar(50),urole varchar(50), PRIMARY KEY (ID))
drop table ResultS_ 
ALTER table LoginP_ ADD PRIMARY KEY (ID)
SELECT *from LoginP_

create table EmployeeP_(ID int NOT NULL, LName varchar(50), Email varchar(50), NPhone varchar(50), Depart_ varchar(50), PRIMARY KEY (ID))
SELECT *FROM EmployeeP_
ALTER table EmployeeP_ add urole varchar(50), address varchar (50) 
SELECT *FROM EmployeeP_

create table StudentP_(ID int NOT NULL, Sname varchar(50), address varchar(50),Email varchar(50), NPhone varchar(50), Semester varchar(50)) 
SELECT * From StudentP_
alter table StudentP_ add PRIMARY KEY (ID)

create table SubjectL_ (Semester varchar(50), subj1 varchar(50), subj2 varchar(50), subj3 varchar(50), subj4 varchar(50), sub5 varchar(50)) 
select *from SubjectL_

create table ResultS_ (ID int NOT NULL, BMelayu int, English int, Math int, Science int,Geometry int,Arts int ,History int,Result varchar(50),Grade varchar(50),PRIMARY KEY (ID))
SELECT *FROM ResultS_
alter table ResultS_ add Arts int ,History int),Result varchar(50),Grade varchar(50)  

CREATE TABLE Finance_ (ID int Not null, Cfee int ,PRIMARY KEY (ID))
SELECT *FROM Finance_


Alter table Finance_ add TFee int 

ALTER TABLE EmployeeP_ ADD DOB VARCHAR(50), Age int

ALTER TABLE StudentP_ ADD DOB VARCHAR(50), Age 

Alter table  StudentP_ add ImageS_ image 

select *from StudentP_

INSERT INTO EmployeeP_ (urole) VALUES ('hai')

select *from EmployeeP_

Alter table  EmployeeP_ alter column ImageE_ image NOT NULL


