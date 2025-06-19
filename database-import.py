import sqlite3
import csv

#create database and connect to it
with sqlite3.connect('db/baseball.db') as conn:
    print('Database created and connected successfully')
    #create cursor
    cursor = conn.cursor()

#create tables
#batting avg
cursor.execute("""
CREATE TABLE IF NOT EXISTS batting_average (
    stat TEXT,
    year TEXT,
    player_name TEXT,
    team TEXT,
    number FLOAT                
)
""")
#home runs
cursor.execute("""
CREATE TABLE IF NOT EXISTS home_runs (
    stat TEXT,
    year TEXT,
    player_name TEXT,
    team TEXT,
    number INTEGER                
)
""")
#rbi
cursor.execute("""
CREATE TABLE IF NOT EXISTS rbi (
    stat TEXT,
    year TEXT,
    player_name TEXT,
    team TEXT,
    number INTEGER                
)
""")
#stolen bases
cursor.execute("""
CREATE TABLE IF NOT EXISTS stolen_bases (
    stat TEXT,
    year TEXT,
    player_name TEXT,
    team TEXT,
    number INTEGER                
)
""")
#total bases
cursor.execute("""
CREATE TABLE IF NOT EXISTS total_bases (
    stat TEXT,
    year TEXT,
    player_name TEXT,
    team TEXT,
    number INTEGER               
)
""")
print('All tables created successfully')