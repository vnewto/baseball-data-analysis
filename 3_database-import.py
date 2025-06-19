import sqlite3
import pandas as pd

#CLEAN CSV FILES FIRST

#convert csv files to dfs
batting_average = pd.read_csv('csv/batting_average.csv')
home_runs = pd.read_csv('csv/home_runs.csv')
rbi = pd.read_csv('csv/rbi.csv')
stolen_bases = pd.read_csv('csv/stolen_bases.csv')
total_bases = pd.read_csv('csv/total_bases.csv')


#create database and connect to it
with sqlite3.connect('db/baseball.db') as conn:
    print('Database created and connected successfully')
    #turn on foreign key constraints
    conn.execute("PRAGMA foreign_keys = 1")
    #create cursor
    cursor = conn.cursor()

    #import each df to sql database
    try:
        batting_average.to_sql('batting_average', conn, if_exists='replace')
        home_runs.to_sql('home_runs', conn, if_exists='replace')
        rbi.to_sql('rbi', conn, if_exists='replace')
        stolen_bases.to_sql('stolen_bases', conn, if_exists='replace')
        total_bases.to_sql('total_bases', conn, if_exists='replace')
    except Exception as e:
        print('An error occured.')
        print(e)


    #commit changes
    conn.commit()