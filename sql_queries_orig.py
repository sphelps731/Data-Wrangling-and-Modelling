# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays CASCADE;"
user_table_drop =  "DROP TABLE IF EXISTS users;"
song_table_drop =  "DROP TABLE IF EXISTS songs CASCADE;"
artist_table_drop =  "DROP TABLE IF EXISTS artists;"
time_table_drop =  "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE songplays (songplay_id SERIAL PRIMARY KEY, \
                         start_time timestamp NOT NULL, user_id varchar NOT NULL, \
                         level varchar, song_id varchar NOT NULL, \
                         artist_id varchar NOT NULL, session_id varchar NOT NULL, location \
                         varchar, user_agent varchar, UNIQUE(user_id), \
                         UNIQUE(song_id), UNIQUE(artist_id))")
                         

user_table_create = ("CREATE TABLE users (user_id varchar PRIMARY KEY, \
                     first_name varchar NOT NULL, last_name varchar NOT NULL, \
                     level varchar, FOREIGN KEY (user_id) REFERENCES songplays (user_id))")

song_table_create = ("CREATE TABLE songs (song_id varchar PRIMARY KEY, title text, \
                     artist_id varchar NOT NULL, year int, \
                     duration int NOT NULL,\
                     UNIQUE(artist_id),\
                     FOREIGN KEY(song_id) REFERENCES songplays(song_id))")
#                    

artist_table_create = ("CREATE TABLE artists (artist_id varchar PRIMARY KEY, name varchar, \
                       location varchar, latitude DECIMAL(8,6), longitude DECIMAL(9,6), \
                       FOREIGN KEY (artist_id) REFERENCES songplays(artist_id),\
                       FOREIGN KEY (artist_id) REFERENCES songs(artist_id))")

time_table_create = ("CREATE TABLE time (start_time timestamp PRIMARY KEY, hour int, day int, \
                    week int, month int,  year int, weekday int)")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration)\
                        VALUES(%s, %s, %s, %s, %s)""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]