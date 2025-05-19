--create empty tables from raw, imported data
DROP TABLE IF EXISTS game_data_clean;
CREATE TABLE game_data_clean (     --clean table for all game data
    game TEXT,   --this will be the "cleaned up" version w/o underscore
    month_year TEXT,
    downloads INTEGER,
    revenue INTEGER,
    average_session_duration REAL,
    sessions_per_day REAL
 );    

--up next, tables for data on each game (empty for now)
DROP TABLE IF EXISTS space_blaster;
CREATE TABLE space_blaster AS SELECT * FROM gen_game_data WHERE 0;
DROP TABLE IF EXISTS merge_master;
CREATE TABLE merge_master AS SELECT * FROM gen_game_data WHERE 0;
DROP TABLE IF EXISTS match_3_forever;
CREATE TABLE match_3_forever AS SELECT * FROM gen_game_data WHERE 0;
DROP TABLE IF EXISTS casino_slots;
CREATE TABLE casino_slots AS SELECT * FROM gen_game_data WHERE 0;
DROP TABLE IF EXISTS strategy_champs;
CREATE TABLE strategy_champs AS SELECT * FROM gen_game_data WHERE 0;