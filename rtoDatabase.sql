create database rto;

use rto;

create table vehicle_details(
vehicle_no varchar(12),
registration_date date,
vehicle_class varchar(30),
owner_name varchar(50),
mobile_no varchar(11),
email_id varchar(50),
license_no varchar(30),
address varchar(100),
city varchar(20),
state varchar(30)
); 


insert into vehicle_details values('KL65K7111','2012-09-13','LMV-NT','Rajesh Shah','7620989478','rajeshshah@gmail.com','KL6520115473898',"Rajmoti apartments",'Kochi','Kerela');

use rto;
 select * from vehicle_details;
 
 insert into vehicle_details values('GJ15PP2948','2002-05-11','LMV-NT','Ankit Bajpayee','99213400077','18it050@charusat.edu.in','GJ1520107894242',"Rajmoti apartments",'Valsad','Gujarat');
 
 insert into vehicle_details values('GJ15CG4272','2019-06-10','LMV-NT','Sudhakar Khetan','9879360355','sudhakarkhetan@gmail.com','GJ151112234875',"Asopalav Society",'Vapi','Gujarat');
 insert into vehicle_details values('KL59T997','2015-02-28','LMV-NT','Sanvi Panchal','77456008899','18it052@charusat.edu.in','KL591112223334',"Evershine towers",'Kochi','Kerela');