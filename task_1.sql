/* query one*/
select c.name,t.name from courses as c,teachers as t;
/* I failed to solve query two */
/* query three*/
select t.name from teachers as t where t.id not in (select distinct c.teacher_id from courses as c );

