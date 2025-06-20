import sqlite3
import pandas as pd

try:
    #convert csv files to dfs
    batting_average = pd.read_csv('csv/bat_avg_cleaned.csv')
    home_runs = pd.read_csv('csv/home_runs_cleaned.csv')
    rbi = pd.read_csv('csv/rbi_cleaned.csv')
    stolen_bases = pd.read_csv('csv/stol_bases_cleaned.csv')
    total_bases = pd.read_csv('csv/tot_bases_cleaned.csv')


    #create database and connect to it
    with sqlite3.connect('db/baseball.db') as conn:
        print('Database created and connected successfully')
        #turn on foreign key constraints
        conn.execute("PRAGMA foreign_keys = 1")
        #create cursor
        cursor = conn.cursor()

        #clear existent tables from db
        cursor.execute("DROP TABLE IF EXISTS batting_average")
        cursor.execute("DROP TABLE IF EXISTS home_runs")
        cursor.execute("DROP TABLE IF EXISTS rbi")
        cursor.execute("DROP TABLE IF EXISTS stolen_bases")
        cursor.execute("DROP TABLE IF EXISTS total_bases")

        #create a table for each stat
        cursor.execute("""
            CREATE TABLE batting_average (
            id INTEGER PRIMARY KEY,
            stat TEXT,
            year INTEGER,
            player TEXT,
            team TEXT,
            number FLOAT 
            )
        """)

        cursor.execute("""
            CREATE TABLE home_runs (
            id INTEGER PRIMARY KEY,
            stat TEXT,
            year INTEGER,
            player TEXT,
            team TEXT,
            number INTEGER 
            )
        """)

        cursor.execute("""
            CREATE TABLE rbi (
            id INTEGER PRIMARY KEY,
            stat TEXT,
            year INTEGER,
            player TEXT,
            team TEXT,
            number INTEGER 
            )
        """)

        cursor.execute("""
            CREATE TABLE stolen_bases (
            id INTEGER PRIMARY KEY,
            stat TEXT,
            year INTEGER,
            player TEXT,
            team TEXT,
            number INTEGER 
            )
        """)

        cursor.execute("""
            CREATE TABLE total_bases (
            id INTEGER PRIMARY KEY,
            stat TEXT,
            year INTEGER,
            player TEXT,
            team TEXT,
            number INTEGER 
            )
        """)

        #loop through rows of each df and insert into proper table
        cursor.executemany("""
            INSERT INTO batting_average (stat, year, player, team, number) 
            VALUES (?, ?, ?, ?, ?)""",
            batting_average.itertuples(index=False, name=None)
        )

        cursor.executemany("""
            INSERT INTO home_runs (stat, year, player, team, number) 
            VALUES (?, ?, ?, ?, ?)""",
            home_runs.itertuples(index=False, name=None)
        )

        cursor.executemany("""
            INSERT INTO rbi (stat, year, player, team, number) 
            VALUES (?, ?, ?, ?, ?)""",
            rbi.itertuples(index=False, name=None)
        )

        cursor.executemany("""
            INSERT INTO stolen_bases (stat, year, player, team, number) 
            VALUES (?, ?, ?, ?, ?)""",
            stolen_bases.itertuples(index=False, name=None)
        )

        cursor.executemany("""
            INSERT INTO total_bases (stat, year, player, team, number) 
            VALUES (?, ?, ?, ?, ?)""",
            total_bases.itertuples(index=False, name=None)
        )

        #commit changes
        conn.commit()
    
    print('All csv files have been loaded into baseball/db.')

except Exception as e:
    print(f'An error occured: {type(e)} - {e}')


