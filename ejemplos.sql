DDL - Lenguaje de Definicion de Datos
create user roberto@localhost identified by '123';

DCL - Lenguaje de Control de Datos
GRANT ALL PRIVILEGES ON *.* TO roberto@localhost;

LOGIN USUARIO CREADO

CREATE DATABASE BaseProyecto;

DDL - Lenguaje de Definicion de Datos
CREATE TABLE curso (
idcurso DECIMAL(2,0) NOT NULL PRIMARY KEY,
nombreDescriptivo VARCHAR(60) NOT NULL,
punteo DECIMAL(3,0) NOT NULL
);

DML - Lenguaje de Manipulacion de Datos
INSERT INTO curso(idcurso,nombreDescriptivo,asignaturas) VALUES(1,'Base de datos II',80);
UPDATE curso SET punteo=100 WHERE idcurso=1;

DQL - Lenguaje de Consulta de Datos
SELECT * FROM curso;
SELECT idcurso, nombreDescriptivo, punteo FROM curso;

TRANSACCION
insert into curso(idcurso,nombreDescriptivo,asignaturas) values(2,'Sistemas Operativos II',85);
insert into curso(idcurso,nombreDescriptivo,asignaturas) values(3,'Estadistica II',90);




ALTA DISPONIBILIDAD
CREATE TABLE curso (
idcurso DECIMAL(2,0) NOT NULL PRIMARY KEY,
nombreDescriptivo VARCHAR(60) NOT NULL,
punteo DECIMAL(3,0) NOT NULL
) ENGINE=ndbcluster;
















GRANT CREATE ON *.* TO roberto@localhost;
GRANT ALL PRIVILEGES ON Facultad.* TO roberto@localhost;
GRANT ALL PRIVILEGES ON BBDDUniversidad.* TO roberto@localhost;

REVOKE CREATE ON *.* FROM roberto@localhost;


create table curso (
idcurso decimal(2,0) not null primary key,
nombreDescriptivo varchar(60) not null,
asignaturas decimal(3,0) not null
) engine=ndbcluster


insert into curso(idcurso,nombreDescriptivo,asignaturas) values(1,'Base de datos II',80);

insert into curso(idcurso,nombreDescriptivo,asignaturas) values(2,'Sistemas Operativos II',85);
insert into curso(idcurso,nombreDescriptivo,asignaturas) values(3,'Estadistica II',90);