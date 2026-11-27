-- your query
WITH highest_salary AS (
SELECT department, name, salary ,
DENSE_RANK() OVER (
    PARTITION BY department
    ORDER BY salary DESC )
    AS rnk 
FROM  employees 
) 

SELECT * 
FROM highest_salary
WHERE rnk <= 3
ORDER BY department ASC, salary DESC, name ASC; 


