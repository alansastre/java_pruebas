DROP SCHEMA IF EXISTS many_to_one1;
CREATE SCHEMA many_to_one1;
USE many_to_onel;

-- CREATE TABLE AUTHOR
CREATE TABLE IF NOT EXISTS AUTHOR (
     AUTHOR_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
     FIRST_NAME VARCHAR(50),
	 EMAIL VARCHAR(50),
     biografhy TEXT
     );
      
     -- CREATE TABLE BOOK
     CREATE TABLE IF NOT EXISTS BOOK (
        BOOK_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       TITLE VARCHAR(300),
       SINOPSIS TEXT,
       NUM_PAGES INT,
	   AUTHOR_ID INT, 
       -- COLUMNA PARA ASOCIAR CON LA TABLA AUTOR
       -- FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHOR (AUTHOR_ID)
	
     -- OPCION 1: FOREING KEY CON NOMBRE AUTOGENERADO
      -- FOREING KEY (AUTHOR_ID) REFERENCES AUTHOR(AUTHOR_ID)
     -- OPCION 2: FOREING KEY CON NOMBRE ESPECIFICO
     CONSTRAINT FK_BOOK_AUTOR FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHOR(AUTHOR_ID)
     );


insert INTO AUTHOR(FIRST_NAME, EMAIL, biografhy) 
VALUES
('AUTHOR1','1AL@COMPANY.COM','BIOGRAFIA'),
('AUTHOR2','2AL@COMPANY.COM','BIOGRAFIA'),
('AUTHOR3','3AL@COMPANY.COM','BIOGRAFIA');
SELECT * FROM AUTHOR;

insert INTO BOOK (TITLE, SINOPSIS, NUM_PAGES, AUTHOR_ID)
VALUES
('book 1','lorem ipsum dolor', 500, 1), -- Auhor 1
('book 2','lorem dolor', 800, 1),-- Auhor 1
('book 3','otra descrip',700, 2),-- Auhor 2
('book 4','otra descrip',700, 3),-- Auhor 2
('book 5','otra descrip',700, 3),-- Auhor 3
('book 6','otra descrip',700, 2);-- Auhor 3

select * from book;
select * from book WHERE thor_id = 2;

-- CREAR BASE DE DATOS MANY_TO_ONE2


DROP SCHEMA IF EXISTS many_to_one2;
CREATE SCHEMA many_to_one2;
USE many_to_one2;

-- CREAR TABLE COMPANY
CREATE TABLE IF NOT EXISTS company (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cif VARCHAR(9) NOT NULL,
      phone VARCHAR(17)
);
-- CREAR TABLE EMPLOYEE, CON FOREING KEY A COMPANY
CREATE TABLE IF NOT EXISTS employee (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  nif VARCHAR(9) NOT NULL,
  salary DECIMAL (12, 2),
  id_company INT,
  FOREIGN KEY (id_company) references company(id)
  );

-- insert company

insert into company (cif, phone) values
('4556677','67899789'),
('4556677','67899789');

-- insert employee

insert into employee (nif, salary, id_company) values
('4556677',null,'1' ),
('4556677','280000','1');

select * from company;
select * from employee;
-- insert employee poniendo una company que no existe y comprobar que da error
-- Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`many_to_one2`.`employee`, CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`id_company`) REFERENCES `company` (`id`))	0.015 sec

insert into employee (nif, salary, id_company) 
values
('1111111',null, 44 );

-- delete company que tenga employees asociados y comprobar que no deja borrar
-- Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`many_to_one2`.`employee`, CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`id_company`) REFERENCES `company` (`id`))	0.015 sec

delete from company where id=1;

-- contar el numero de empleados agrupados por company id
select count(*)from employee group by id_company

-- para poder borar la company 1 primero hay que poner a NULL el Id_company en employee
update employee set id_company= null where id = 1; -- desasociado la empresa
 update employee set id_company= null where id = 2; -- desasociado la empresa
 
 select * from employee;
 -- ahora deberia dejar de borrar la empresa porque hemos desasociado los employee
 delete from company where id = 1;
 select * from company; 
