--key transforms: clean up game name, load key data into clean table & game tables

--clean game name format, load it all into the cleaned general table
DELETE FROM game_data_clean;   --important for idempotent script

INSERT INTO game_data_clean
    (game,
    month_year,
    downloads,
    revenue,
    average_session_duration,
    sessions_per_day
    )
SELECT
    replace(game, '_', ' ') AS game,    --this replaces underscore with space
    month AS month_year,
    downloads,
    revenue,
    average_session_duration,
    sessions_per_day
FROM gen_game_data;

--load data into per-game tables
--space blaster
DELETE FROM space_blaster;
INSERT INTO space_blaster
SELECT * FROM game_data_clean
WHERE  game = 'space blaster';

--merge master
DELETE FROM merge_master;
INSERT INTO merge_master
SELECT * FROM game_data_clean
WHERE  game = 'merge master';

--match 3 forever
DELETE FROM match_3_forever;
INSERT INTO match_3_forever
SELECT * FROM game_data_clean
WHERE  game = 'match 3 forever';

--casino slots
DELETE FROM casino_slots;
INSERT INTO casino_slots
SELECT * FROM game_data_clean
WHERE  game = 'casino slots';

--strategy champs
DELETE FROM strategy_champs;
INSERT INTO strategy_champs
SELECT * FROM game_data_clean
WHERE  game = 'strategy champs';
