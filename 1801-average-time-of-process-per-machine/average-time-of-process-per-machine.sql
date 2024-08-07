select s.machine_id, round(avg(e.timestamp-s.timestamp),3) as processing_time
from Activity s join Activity e 
on (s.machine_id = e.machine_id) and (s.process_id = e.process_id)
where lower(s.activity_type) = 'start' 
and lower(e.activity_type) = 'end'
group by s.machine_id;