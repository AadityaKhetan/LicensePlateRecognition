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
 
 
 
