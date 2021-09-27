ALTER TABLE rdata
ADD y boolean DEFAULT false;

SELECT * FROM rdata;

/* 
 id |   a   |   b   |   moment   |   x    | y 
----+-------+-------+------------+--------+---
  1 | angry | red   | 2020-03-01 | 150.01 | f
  2 | sad   | blue  | 2020-03-01 | 253.14 | f
  3 | happy | yelow | 2000-09-01 | 444.44 | f
  5 | envy  | green | 2000-09-01 | 294.33 | f
(4 rows)
*/