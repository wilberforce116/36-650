INSERT INTO rdata (a, b, x)
VALUES ('envy', 'green', -294.33);

-- ERROR:  new row for relation "rdata" violates check constraint "rdata_x_check"
-- DETAIL:  Failing row contains (4, envy, green, 2020-01-01, -100.33).

INSERT INTO rdata (a, b, x)
VALUES ('envy', 'green', 294.33);

SELECT * FROM rdata;

/* id |   a   |   b   |   moment   |   x    
----+-------+-------+------------+--------
  1 | angry | red   | 2020-01-01 | 150.01
  2 | sad   | blue  | 2020-01-01 | 253.14
  3 | happy | yelow | 2020-01-01 | 444.44
  5 | envy  | green | 2020-01-01 | 294.33
(4 rows) */