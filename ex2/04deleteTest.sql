#alter table dept add constraint fkOnDept foreign key(leader_no) references staff(staff_no) on delete restrict on update cascade;
#alter table dept modify dept_name char(20) not null;
#alter table dept modify leader_no int not null;
#alter table project modify project_name char(20) not null;
#alter table job modify work_span int not null;
#desc staff;
#desc dept;
#desc project;
#desc job;
#delete from staff where staff_no=10003;
#delete from dept where leader_no=10006;
#delete from project where dept_no=101;
#insert into staff values(null,10013,32,100000,101);
#insert into job values(10013,2,3);
delete from job where staff_no=10012 and project_no=2;