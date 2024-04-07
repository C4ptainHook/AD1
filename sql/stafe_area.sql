CREATE SCHEMA IF NOT EXISTS Stage;

CREATE TABLE Stage.metacritic_review(
id SERIAL PRIMARY KEY,
metascore INT,
game TEXT,
platform TEXT
)

CREATE TABLE Stage.requirements(
id SERIAL PRIMARY KEY,
steam_game_id TEXT,
pc_req TEXT,
mac_req TEXT,
linux_req TEXT,
min_req TEXT
)

CREATE TABLE Stage.all_steam(
id SERIAL PRIMARY KEY,
game TEXT,
link TEXT,
release TEXT,
rating TEXT,
publisher TEXT,
developer TEXT,
technologies TEXT,
all_time_peak TEXT,
all_time_peak_date TEXT	
)

CREATE TABLE Stage.play_time_by_player(
id SERIAL PRIMARY KEY,
game_id TEXT,
game TEXT,
action_type TEXT,
time TEXT	
)

CREATE TABLE Stage.genres(
id SERIAL PRIMARY KEY,
game TEXT,
release_date TEXT,
developer TEXT,
genres TEXT,
summary TEXT
)

CREATE TABLE Stage.regions(
id SERIAL PRIMARY KEY,
game TEXT,
platforms TEXT,
year_of_release TEXT,
genre TEXT,
publisher TEXT,
na_players TEXT,
eu_players TEXT,
jp_players TEXT,
other_players TEXT,
global_players TEXT,
developer TEXT,
rating TEXT	
)

CREATE TABLE Stage.mdn_play_time(
id SERIAL PRIMARY KEY,
steam_game_id TEXT,
game TEXT,
release_date TEXT,
developer TEXT,
publisher TEXT,
platforms TEXT,
genres TEXT,
avg_play_time TEXT,
median_play_time TEXT,
owners TEXT
)

CREATE TABLE Stage.time_to_beat(
id SERIAL PRIMARY KEY,
achivements TEXT,
description TEXT,
developers TEXT,
gfq_difficulty TEXT,
gfq_rating TEXT,
grnk_score TEXT,
hltb_complete TEXT,
hltb_single TEXT,
igdb_score TEXT,
igdb_single TEXT,
igdb_uscore TEXT,
languages TEXT,
game TEXT,
platforms TEXT,
published_hltb_date TEXT,
publishers TEXT,
tags TEXT,
voiceovers TEXT	
)
