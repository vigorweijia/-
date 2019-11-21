use ex2;
create table Staff(
	staff_name char(20),
    staff_no int,
    age int,
    salary int,
    dept_no int,
    primary key(staff_nodept_nameleader_nodept)
);
create table Dept(
	dept_name char(20),
    dept_no int,
    leader_no int,
    primary key(leader_no)
);
create table Project(
	project_name char(20),
    project_no int,
    dept_no int,
    primary key(project_no)
);
create table Job(
	staff_no int,
    project_no int,
    work_span int
);