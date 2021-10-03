-- Add new column
ALTER TABLE player_bios
ADD height_inches NUMERIC;

-- Populate height_inches
UPDATE player_bios
SET height_inches = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer;

-- Replace old height column
ALTER TABLE player_bios
DROP height;

ALTER TABLE player_bios
RENAME COLUMN height_inches TO height;

-- Display first 5 names
SELECT firstname, lastname, height
FROM player_bios
ORDER BY id
LIMIT 5;

/*

 firstname | lastname | height 
-----------+----------+--------
 Aaron     | Brooks   |     72
 Aaron     | Gordon   |     81
 Aaron     | Harrison |     78
 Adreian   | Payne    |     82
 Al        | Horford  |     82
(5 rows)

*/