-- using database edyoda
use edyoda;

-- creating Tables and inserting data 

CREATE TABLE IF NOT EXISTS SalesPeople (
Snum int primary key,
Sname varchar(50) unique,
city varchar(50),
comm int);

insert into salespeople values
(1001,'peel','London',12),
(1002,'Serres','Sanjose',13),
(1004,'Motika','London',11),
(1007,'Refkin','Barcelona',15),
(1003,'Aexlord','Newyork',10);

select * from SalesPeople;

create Table if not exists Customers (
Cnum int primary key,
Cname varchar (50),
city varchar(50) not null,
Snum int,
foreign key (Snum) references salespeople(Snum));



insert into Customers values
(2001,'Hoffman','London',1001),
(2002,'Giovanni','Rome',1003),
(2003,'Liu','Sanjose',1002),
(2004,'Grass','Berlin',1002),
(2006,'Celmens','London',1001),
(2007,'Pereira','Rome',1004),
(2008,'Cisneros','Sanjose',1007);

select * from Customers;

create table Orders (
Onum int primary key,
Amt float null,
Odate date,
Cnum int,
foreign key (Cnum) references Customers(Cnum),
Snum int,
foreign key (Snum) references salespeople(Snum));


insert into orders values
(3001,18.69,'1990-10-03',2008,1007),
(3003,767.19,'1990-10-03',2001,1001),
(3002,1900.10,'1990-10-03',2007,1004),
(3005,5160.45,'1990-10-03',2003,1002),
(3006,1098.16,'1990-10-03',2008,1007),
(3009,1713.23,'1990-10-04',2002,1003),
(3007,75.75,'1990-10-04',2004,1002),
(3008,4273.00,'1990-10-05',2006,1001),
(3010,1309.95,'1990-10-06',2004,1002),
(3011,9891.88,'1990-10-06',2006,1001);
select * from Orders;


--  1>Count the number of Salesperson whose name begin with ‘a’/’A’.

SELECT Sname,count(Sname)
FROM SalesPeople
where Sname like 'a%' or Sname like 'A%'
group by Sname;

-- answer --> Aexlord  1



-- 2>Display all the Salesperson whose all orders worth is more than Rs. 2000.

select Sname 
from salespeople 
where snum in (select Snum from orders where Amt>2000);

-- answer peel,serres

--  3>Count the number of Salesperson belonging to Newyork.

select count(sname)
from Salespeople
where city in ('newyork');
-- answer 1


--  4>Display the number of Salespeople belonging to London and belonging to Paris.

select Sname,city
from Salespeople
where city in ('newyork','paris');
 -- answer 1 Aexlord,newyork


--  5>Display the number of orders taken by each Salesperson and their date of orders.

SELECT COUNT(Onum), Odate
FROM Orders
group by Odate;
-- answer 
-- 5	1990-10-03
-- 2	1990-10-04
-- 1	1990-10-05
-- 2	1990-10-06