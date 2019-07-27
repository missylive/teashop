create table customer (
email varchar(64) not null,
customer_name varchar(255) not null,
phone int(10),
address varchar(255),
primary key (email)
);
insert into customer (email, customer_name, phone)
values ('sam999@gmail.com', 'Sam', 2817779999,'3959 main street Houston TX 77005'),
('mike888@gmail.com', 'Mike', 2818887777,'2020 Sam Houston street Houston TX 77020'),
('mary666@gmail.com', 'Mary', '2816667777','5858 Allen PKWY Houston TX 77027'),
('Jessy555@hotmail.com','Jessy', '2815557777','3636 Bay area road Clear Lake TX 77588'),
('amy333@hotmail.com', 'Amy', '2813335555','8989 Richmond road Houston TX 77025');

create table employee (
employee_id int(10),
employee_name varchar(128),
phone int(10),
primary key (employee_id)
);
insert into employee (employee_id, employee_name, phone)
values (00001, 'Kelvin','7138889999' ),
(00002, 'Judy','7137778888'),
(00003, 'Tom','7136667777');

create table menu (
menu_item_number int(10)not null,
item_name varchar(128)not null,
price int(10)not null,
drinkstatus boolean,
drink_type varchar(255),
drink_description varchar(255),
primary key (menu_item_number)
);

insert into menu (menu_item_number, item_name, price,drinkstatus, drink_type, drink_description)
values(1001,'Black Tea',3.5,true,'Orginal tea','black tea'),
(1002,'Green Tea',3.5,true,'Orginal tea','Green Tea'),
(1003,'Oolong Tea',4,true,'Orginal tea','Oolong Tea'),
(1004,'Milk Tea',4.5,true,'Cream tea','black tea mixed with cream'),
(1005,'Green Tea Latta',4.5,true,'Cream tea','green tea mixed with cream'),
(1006,'Chocolate Latta',6,true,'Cream tea','Chocolate mixed with milk'),
(1007,'Honey Green Tea',4.5,true,'Flavored tea','real honey with green tea'),
(1008,'Honey Black Tea',4.5,true,'Flavored tea','real honey with black tea'),
(1009,'Honey Tea',4,true,'Flavored tea','honey tea'),
(1010,'Avocado Smooties',4.5,true,'Smooties','avocado smooties'),
(1011,'Coconut Smooties',4.5,true,'Smooties','coconut smooties'),
(1012,'Banana Smooties',4.5,true,'Smooties','banana with creamy smooties'),
(1014,'Mango Smooties',4.5,true,'Smooties','mango smooties'),
(1015,'Coffee Smooties',4.5,true,'Smooties','coffee smooties'),
(1016,'cookies Smooties',4.5,true,'Smooties','oreo cookies smooties'),
(1017,'Strawberry Smooties',4.5,true,'Smooties','strawberry with creamy smooties')
;

create table add_on_item (
add_on_number int(10)not null,
food_description varchar(255),
price int(10)not null,
foodstatus boolean,
primary key (add_on_number)
);

insert into add_on_item (add_on_number,food_description,price,foodstatus)
values(2001,'tapioca',1.25,true),
(2002,'honey',1.25,true),
(2003,'extra sugar',0.5,true),
(2004,'milk',1.25,true),
(2005,'creamy',1.25,true),
(2006,'coffee jelly',1.25,true),
(2007,'grass jelly',1.25,true),
(2008,'lemon',0.5,true),
(2009,'taro jelly',1.25,true),
(2010,'ice',0,true);

create table orders(
order_number int auto_increment primary key,
menu_item_number int(10)not null,
order_time timestamp,
order_date datetime not null,
order_type varchar(255),
email varchar(255),
employee_id int(10),
discount (10),
add_on_number int(10),
tax double(10),
total_price real(10),
tips double(10),
notes varchar(255),
primary key (order_number)
);

create table bill (
bill_number int(10)not null,
order_number int(10)not null,
food_description varchar(255),
amount int(10)not null,
payment_status boolean,
primary key (bill_number)
);

create table cash_payment (
bill_number int(10)not null,
amount int(10)not null,
primary key (bill_number)
);

create table cc_payment (
bill_number int(10)not null,
card_number int(16),
expire_date date,
cvv int(3),
amount int(10)not null,
primary key (bill_number)
);

