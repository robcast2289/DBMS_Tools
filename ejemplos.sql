create user roberto@localhost identified by '123456'


GRANT CREATE ON *.* TO roberto@localhost;
GRANT ALL PRIVILEGES ON Facultad.* TO roberto@localhost;
GRANT ALL PRIVILEGES ON BBDDUniversidad.* TO roberto@localhost;

REVOKE CREATE ON *.* FROM roberto@localhost;


create table curso (
idcurso decimal(2,0) not null primary key,
nombreDescriptivo varchar(60) not null,
asignaturas decimal(3,0) not null
) engine=ndbcluster