#insert into job values(10007,5,26);
#insert into job values(10003,1,15);
create user 'worker'@'localhost' identified by '123456';
grant select on ex2.staff to 'worker'@'localhost';
grant update(age) on ex2.staff to 'worker'@'localhost';
flush privileges;
