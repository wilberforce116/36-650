CREATE TABLE new_table (
    player INTEGER REFERENCES more_player_stats,
    prl NUMERIC,
    position TEXT
);

INSERT INTO new_table (player, prl)
    (SELECT id,
            round(per - 67*va/(gp*minutes), 3) FROM more_player_stats);

UPDATE new_table
SET position = CASE
        WHEN prl >= 11.3 THEN 'PF'
        WHEN prl >= 10.8 AND prl < 11.3 THEN 'PG'
        WHEN prl >= 10.6 AND prl < 10.8 THEN 'C'
        WHEN prl >= 0 AND prl < 10.6 THEN 'SG/SF'
        END;


SELECT * FROM new_table LIMIT 10;


/*
 player |  prl   | position 
--------+--------+----------
      1 | 10.995 | PG
      2 | 11.503 | PF
      3 | 10.536 | SG/SF
      4 | 11.527 | PF
      5 | 10.607 | C
      6 | 10.594 | SG/SF
      7 | 10.495 | SG/SF
      8 | 10.478 | SG/SF
      9 | 10.607 | C
     10 | 10.503 | SG/SF
(10 rows)
*/
