ALTER TABLE player_bios
ADD position TEXT;

UPDATE player_bios
SET position = new_table.position
FROM new_table
WHERE new_table.player = player_bios.id;

SELECT firstname, lastname, position
FROM player_bios
ORDER BY id
LIMIT 5;

/*

 firstname | lastname | position 
-----------+----------+----------
 Aaron     | Brooks   | PG
 Aaron     | Gordon   | PF
 Aaron     | Harrison | SG/SF
 Adreian   | Payne    | PF
 Al        | Horford  | C
(5 rows)

*/