# sort by year (line graph) for each statistic
# sort by team for each statistic (bar graph)
# top 10 all-time best players or teams for each statistic (bar graph)
#% stolen bases out of total bases (stacked bar graph)

#Spanish characters: ñ, á, é, í, ó, ú

import sqlite3
import pandas as pd

#connect to sqlite db
def get_connection():
    try:
        return sqlite3.connect('db/baseball.db')
    except sqlite3.Error as e:
        print(f'Error connecting to database / Error de conexión: {e}')
        return None

#set variable to turn language display on and off
display_language = True

#choose a language
def choose_language():
    print("""
        Elige idioma: \n
        1. English
        2. Español
        3. Exit / Salir
    """)

#set up query options for user
def show_query_options_english():
    display_language = False
    print("""
        Select a number to choose a query (ex., 2): \n
        1. Top 5 players by stat
        2. Top teams by year
        3. Players who were in the top for multiple years
        4. Exit
          """)

def show_query_options_spanish():
    display_language = False
    print("""
        Selecciona un número para elegir una consulta (ej., 2): \n
        1. Los 5 mejores jugadores por estadística
        2. Mejores equipos por año
        3. Jugadores que estuvieron entre los mejores durante varios años
        4. Salir
          """)

#set up query for filtering top players by stat
#English
def query_top_players_by_stat_en(conn):
    display_language = False
    try:
        stat = input('Enter stat (Batting Average, Home Runs, RBI, Stolen Bases, or Total Bases):').lower().strip()
        if stat == 'batting average':
            cursor = conn.execute("""
                SELECT player, year, number FROM batting_average ORDER BY number DESC LIMIT 5
            """)
            results = cursor.fetchall()
            if results:
                print(f"\n Top 5 Players by {stat.title()}: \n")
                for row in results:
                    print(f'{row[0]} ({row[1]}) - {row[2]}')
            else:
                print('No results found.')
        elif stat == 'home runs':
            cursor = conn.execute("""
                SELECT player, year, number FROM home_runs ORDER BY number DESC LIMIT 5
            """)
            results = cursor.fetchall()
            if results:
                print(f"\n Top 5 Players by {stat.title()}: \n")
                for row in results:
                    print(f'{row[0]} ({row[1]}) - {row[2]}')
            else:
                print('No results found.')
        elif stat == 'rbi':
            cursor = conn.execute("""
                SELECT player, year, number FROM rbi ORDER BY number DESC LIMIT 5
            """)
            results = cursor.fetchall()
            if results:
                print(f"\n Top 5 Players by {stat.title()}: \n")
                for row in results:
                    print(f'{row[0]} ({row[1]}) - {row[2]}')
            else:
                print('No results found.')
        elif stat == 'stolen bases':
            cursor = conn.execute("""
                SELECT player, year, number FROM stolen_bases ORDER BY number DESC LIMIT 5
            """)
            results = cursor.fetchall()
            if results:
                print(f"\n Top 5 Players by {stat.title()}: \n")
                for row in results:
                    print(f'{row[0]} ({row[1]}) - {row[2]}')
            else:
                print('No results found.')
        elif stat == 'total bases':
            cursor = conn.execute("""
                SELECT player, year, number FROM total_bases ORDER BY number DESC LIMIT 5
            """)
            results = cursor.fetchall()
            if results:
                print(f"\n Top 5 Players by {stat.title()}: \n")
                for row in results:
                    print(f'{row[0]} ({row[1]}) - {row[2]}')
            else:
                print('No results found.')
        else:
            print('Invalid input. Try again.')
        
    except Exception as e:
        print(f'Error: {type(e).__name__} - {e}')

#Spanish
def query_top_players_by_stat_sp(conn):
    display_language = False
    try:
        stat = input('Ingresa una estadística (Promedio de Bateo, Jonrones, Carreras Impulsadas, Bases Robadas, o Total de Bases):').lower().strip()
        if stat == 'promedio de bateo':
            cursor = conn.execute("""
                SELECT player, year, number FROM batting_average ORDER BY number DESC LIMIT 5
            """)
            results = cursor.fetchall()
            if results:
                print(f"\n Los 5 mejores jugadores por {stat.title()}: \n")
                for row in results:
                    print(f'{row[0]} ({row[1]}) - {row[2]}')
            else:
                print('No se encontraron resultados.')
        elif stat == 'jonrones':
            cursor = conn.execute("""
                SELECT player, year, number FROM home_runs ORDER BY number DESC LIMIT 5
            """)
            results = cursor.fetchall()
            if results:
                print(f"\n Los 5 mejores jugadores por {stat.title()}: \n")
                for row in results:
                    print(f'{row[0]} ({row[1]}) - {row[2]}')
            else:
                print('No se encontraron resultados.')
        elif stat == 'carreras impulsadas':
            cursor = conn.execute("""
                SELECT player, year, number FROM rbi ORDER BY number DESC LIMIT 5
            """)
            results = cursor.fetchall()
            if results:
                print(f"\n Los 5 mejores jugadores por {stat.title()}: \n")
                for row in results:
                    print(f'{row[0]} ({row[1]}) - {row[2]}')
            else:
                print('No se encontraron resultados.')
        elif stat == 'bases robadas':
            cursor = conn.execute("""
                SELECT player, year, number FROM stolen_bases ORDER BY number DESC LIMIT 5
            """)
            results = cursor.fetchall()
            if results:
                print(f"\n Los 5 mejores jugadores por {stat.title()}: \n")
                for row in results:
                    print(f'{row[0]} ({row[1]}) - {row[2]}')
            else:
                print('No se encontraron resultados.')
        elif stat == 'total de bases':
            cursor = conn.execute("""
                SELECT player, year, number FROM total_bases ORDER BY number DESC LIMIT 5
            """)
            results = cursor.fetchall()
            if results:
                print(f"\n Los 5 mejores jugadores por {stat.title()}: \n")
                for row in results:
                    print(f'{row[0]} ({row[1]}) - {row[2]}')
            else:
                print('No se encontraron resultados.')
        else:
            print('Entrada no válida. Inténtalo de nuevo.')

    except Exception as e:
        print(f'Error: {type(e).__name__} - {e}')


#set up query for filtering top teams by year
#english
def query_top_teams_by_yr_en(conn):
    display_language = False
    try:        
        #use input year
        year = input(' \n Enter year (2000-2024): ').strip()
        #filter table
        cursor = conn.execute(f"""SELECT year, ba_stat, ba_team, ba_num, hr_stat, hr_team, hr_num, r_stat, r_team, r_num, sb_stat, sb_team, sb_num, tb_stat, tb_team, tb_num 
        FROM stats_by_year 
        WHERE year = {int(year)}""")
        results = cursor.fetchall()
        if results:
            for row in results:
                print(f""" \n Top Teams in {year}: \n
                {row[2]} - {row[3]} {row[1]} 
                {row[5]} - {row[6]} {row[4]} 
                {row[8]} - {row[9]} {row[7]} 
                {row[11]} - {row[12]} {row[10]} 
                {row[14]} - {row[15]} {row[13]} 
                """)
        else:
            print('No results found.')

    except Exception as e:
        print(f'Error: {type(e).__name__} - {e}')

def query_top_teams_by_yr_sp(conn):
    display_language = False
    try:        
        #use input year
        year = input(' \n Elige un año entre 2000 y 2024: ').strip()
        #filter table
        cursor = conn.execute(f"""SELECT year, ba_stat, ba_team, ba_num, hr_stat, hr_team, hr_num, r_stat, r_team, r_num, sb_stat, sb_team, sb_num, tb_stat, tb_team, tb_num 
        FROM stats_by_year 
        WHERE year = {int(year)}""")
        results = cursor.fetchall()
        if results:
            #Promedio de Bateo, Jonrones, Carreras Impulsadas, Bases Robadas, Total de Bases
            for row in results:
                print(f"""\n Mejores equipos en {year}: \n 
                {row[2]} - {row[3]} Promedio de Bateo 
                {row[5]} - {row[6]} Jonrones 
                {row[8]} - {row[9]} Carreras Impulsadas 
                {row[11]} - {row[12]} Bases Robadas 
                {row[14]} - {row[15]} Total de Bases 
                """)
        else:
            print('No se encontraron resultados.')

    except Exception as e:
        print(f'Error: {type(e).__name__} - {e}')


#set up query for filtering players who who have records multiple years
def query_top_players_mult_yrs_en(conn):
    display_language = False
    try:
        cursor = conn.execute(f"""SELECT player, MIN(year) AS earliest_year, MAX(year) AS latest_year, COUNT(stat) AS num_top_records, MAX(year) - MIN(year) AS year_diff
        FROM baseball_data
        GROUP BY player
        HAVING COUNT(stat) > 1 AND (MAX(year) - MIN(year)) > 0
        ORDER BY num_top_records DESC
        LIMIT 10
        """)
        results = cursor.fetchall()
        if results:
            print("\n Players who were in the top for multiple years: \n")
            for row in results:
                print(f"Between {row[1]} and {row[2]}, {row[0]} earned {row[3]} top spots.")
        else:
            print('No results found.')
    except Exception as e:
        print(f'Error: {type(e).__name__} - {e}')

def query_top_players_mult_yrs_sp(conn):
    display_language = False
    try:
        cursor = conn.execute(f"""SELECT player, MIN(year) AS earliest_year, MAX(year) AS latest_year, COUNT(stat) AS num_top_records, MAX(year) - MIN(year) AS year_diff
        FROM baseball_data
        GROUP BY player
        HAVING COUNT(stat) > 1 AND (MAX(year) - MIN(year)) > 0
        ORDER BY num_top_records DESC
        LIMIT 10
        """)
        results = cursor.fetchall()
        if results:
            print(" \n Jugadores que ocuparon los primeros puestos durante varios años: \n")
            for row in results:
                print(f"Entre {row[1]} y {row[2]}, {row[0]} logró {row[3]} primeros puestos.")
        else:
            print('No se encontraron resultados.')
    except Exception as e:
        print(f'Error: {type(e).__name__} - {e}')


#display menu only while connected to db
def main():
    conn = get_connection()
    if not conn:
        return
    
    try:
        #while there is a connection
        while True:
            choose_language()
            lang_choice = input('Choice / Opción : ').strip()

            #if english
            if lang_choice == '1':
                #always show query options menu
                while True:
                    show_query_options_english()
                    #use user input to navigate
                    choice = input('Choice: ').strip()
                    if choice == '1':
                        query_top_players_by_stat_en(conn)
                    elif choice == '2':
                        query_top_teams_by_yr_en(conn)
                    elif choice == '3':
                        query_top_players_mult_yrs_en(conn)
                    elif choice == '4':
                        print('Exiting...')
                        #exit menu
                        break
                    else:
                        print('Invalid input. Try again.')
                
            #if spanish
            elif lang_choice == '2':
                while True:
                    show_query_options_spanish()
                    #use user input to navigate
                    choice = input('Choice: ').strip()
                    if choice == '1':
                        query_top_players_by_stat_sp(conn)
                    elif choice == '2':
                        query_top_teams_by_yr_sp(conn)
                    elif choice == '3':
                        query_top_players_mult_yrs_sp(conn)
                    elif choice == '4':
                        print('Saliendo...')
                        #exit menu
                        break
                    else:
                        print('Entrada no válida. Inténtalo de nuevo.')
            
            #if exit
            elif lang_choice == '3':
                print('Exiting / Saliendo...')
                #exit menu
                break
            
            #if invalid input:
            else:
                print('Invalid input. Try again. / Entrada no válida. Inténtalo de nuevo.')
    
    except Exception as e:
        print(e)
    
    #close connection
    finally:
        conn.close()

#only run function if script is run directly, not if it's an imported module
if __name__ == '__main__':
    main()