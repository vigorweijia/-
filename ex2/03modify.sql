alter table job add constraint pkOnJob primary key (staff_no,project_no);

alter table dept drop primary key;
alter table dept modify dept_no int primary key;

alter table staff modify staff_name char(20) not null;

alter table staff add constraint fkOnStaff foreign key(dept_no) references dept(dept_no) on delete restrict on update cascade;
alter table project add constraint fkOnProject foreign key(dept_no) references dept(dept_no) on delete restrict on update cascade;
alter table job add constraint fk1OnJob foreign key(staff_no) references staff(staff_no) on delete restrict on update cascade;
alter table job add constraint fk2OnJob foreign key(project_no) references project(project_no) on delete restrict on update cascade;