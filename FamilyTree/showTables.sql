SELECT * 
  FROM sqlite_master 
 WHERE type='table';
   
SELECT *
  FROM Person;

/*Married Couples  */
SELECT *
  FROM Person A, Person B
 WHERE A.MarriedTo = B.Pid
   AND A.Sex = 'M';

/* children of a designated Person */   
 SELECT *
   FROM  PersonChild PC, Person P
  WHERE PC.Pid=1000
    AND PC.PChildid = P.Pid;
    
    