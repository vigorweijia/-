#use ex2;
delimiter //
create trigger ins_job 
before insert on job for each row
begin
	if new.work_span > 24 then 
		set new.work_span = 24;
	end if;
end;
//
delimiter ;

delimiter //
create trigger ins_new_job
after insert on job for each row
begin
	if exists(select * from dept where dept.leader_no = new.staff_no) then
		update staff set salary = salary * 1.08 where new.staff_no = staff.staff_no;
	else
		update staff set salary = salary * 1.05 where new.staff_no = staff.staff_no;
    end if;
end;
//
delimiter ;