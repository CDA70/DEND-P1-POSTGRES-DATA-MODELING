#Fact Table
#    1. songplays - records in log data associated with song plays i.e. records with page NextSong 
#           songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent 
#Dimension Tables
#    2. users - users in the app
#           user_id, first_name, last_name, gender, level 
#    3. songs - songs in music database
#           song_id, title, artist_id, year, duration 
#    4. artists - artists in music database
#           artist_id, name, location, lattitude, longitude 
#    5. time - timestamps of records in songplays broken down into specific units
#           start_time, hour, day, week, month, year, weekday 


# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
# songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent 
# Serial is the same as integer except that PostgreSQL will automatically 
# generate and populate values into the SERIAL column. 
# This is similar to AUTO_INCREMENT column in MySQL or AUTOINCREMENT column in SQLite.
songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays(
    songplay_id SERIAL PRIMARY KEY, 
    start_time varchar, 
    user_id varchar, 
    level varchar, 
    song_id varchar, 
    artist_id varchar, 
    session_id varchar, 
    location varchar, 
    user_agent varchar)
""")

# user_id, first_name, last_name, gender, level
user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
    user_id varchar, 
    first_name varchar, 
    last_name varchar, 
    gender varchar, 
    level varchar)
""")

# song_id, title, artist_id, year, duration
song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
    song_id varchar, 
    title varchar, 
    artist_id varchar, 
    year int, 
    duration float)
""")

# artist_id, name, location, lattitude, longitude
artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
    artist_id varchar, 
    name varchar, 
    location varchar, 
    lattitude float, 
    longitude float)
""")

# start_time, hour, day, week, month, year, weekday
time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
    start_time varchar, 
    hour int, 
    day int, 
    week int, 
    month int,
    year int,
    weekday int)
""")

# INSERT RECORDS

# sonplay_id is a serial and filled automatically
songplay_table_insert = ("""
    INSERT INTO songplays(
        start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """)

user_table_insert = ("""
    INSERT INTO users(
        user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
    """)

song_table_insert = ("""
    INSERT INTO songs(
        song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
    """)

artist_table_insert = ("""
    INSERT INTO artists(
        artist_id, name, location, lattitude, longitude) VALUES (%s, %s, %s, %s, %s)
    """)


time_table_insert = ("""
    INSERT INTO time(
        start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """)

# FIND SONGS
# Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and  duration of a song.
song_select = ("""
    SELECT songs.song_id, artists.artist_id
    FROM (songs JOIN artists
    ON songs.artist_id = artists.artist_id)
    WHERE (songs.title=%s) AND (artists.name=%s) AND (songs.duration=%s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]