UPDATE rdata SET moment = '2020-03-01'::date WHERE a = 'angry' OR a = 'sad';
UPDATE rdata SET moment = '2000-09-01'::date WHERE a = 'happy' OR a = 'envy';

SELECT * FROM rdata;

/*  id |   a   |   b   |   moment   |   x    
----+-------+-------+------------+--------
  1 | angry | red   | 2020-03-01 | 150.01
  2 | sad   | blue  | 2020-03-01 | 253.14
  3 | happy | yelow | 2000-09-01 | 444.44
  5 | envy  | green | 2000-09-01 | 294.33
(4 rows)
*/