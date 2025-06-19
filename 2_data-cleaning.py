import pandas as pd

#convert csv files to dataframes
bat_avg = pd.read_csv("csv/batting_average.csv")
home_runs = pd.read_csv("csv/home_runs.csv")
rbi = pd.read_csv("csv/rbi.csv")
tot_bases = pd.read_csv("csv/total_bases.csv")
stol_bases = pd.read_csv("csv/stolen_bases.csv")

#drop rows with na values 
#check length of df first, then drop na values, then recheck length to see if any were dropped
print(f'bat_avg original length: ', len(bat_avg))
bat_avg_dropped_na = bat_avg.dropna()
print(f'bat_avg_dropped_na length: ', len(bat_avg_dropped_na))
print(f'{len(bat_avg) - len(bat_avg_dropped_na)} rows containing na values were dropped from bat_avg')

print(f'home_runs original length: ', len(home_runs))
home_runs_dropped_na = home_runs.dropna()
print(f'home_runs_dropped_na length: ', len(home_runs_dropped_na))
print(f'{len(home_runs) - len(home_runs_dropped_na)} rows containing na values were dropped from home_runs')

print(f'rbi original length: ', len(rbi))
rbi_dropped_na = rbi.dropna()
print(f'rbi_dropped_na length: ', len(rbi_dropped_na))
print(f'{len(rbi) - len(rbi_dropped_na)} rows containing na values were dropped from rbi')

print(f'tot_bases original length: ', len(tot_bases))
tot_bases_dropped_na = tot_bases.dropna()
print(f'tot_bases_dropped_na length: ', len(tot_bases_dropped_na))
print(f'{len(tot_bases) - len(tot_bases_dropped_na)} rows containing na values were dropped from tot_bases')

print(f'stol_bases original length: ', len(stol_bases))
stol_bases_dropped_na = stol_bases.dropna()
print(f'stol_bases_dropped_na length: ', len(stol_bases_dropped_na))
print(f'{len(stol_bases) - len(stol_bases_dropped_na)} rows containing na values were dropped from stol_bases')


#drop duplicate values
#check length of df first, then drop na values, then recheck length to see if any were dropped
print(f'bat_avg_dropped_na original length: ', len(bat_avg_dropped_na))
bat_avg_dropped_dup = bat_avg_dropped_na.drop_duplicates()
print(f'bat_avg_dropped_dup length: ', len(bat_avg_dropped_dup))
print(f'{len(bat_avg_dropped_na) - len(bat_avg_dropped_dup)} duplicate rows were dropped from bat_avg_dropped_na')

print(f'home_runs_dropped_na original length: ', len(home_runs_dropped_na))
home_runs_dropped_dup = home_runs_dropped_na.drop_duplicates()
print(f'home_runs_dropped_dup length: ', len(home_runs_dropped_dup))
print(f'{len(home_runs_dropped_na) - len(home_runs_dropped_dup)} duplicate rows were dropped from home_runs_dropped_na')

print(f'rbi_dropped_na original length: ', len(rbi_dropped_na))
rbi_dropped_dup = rbi_dropped_na.drop_duplicates()
print(f'rbi_dropped_dup length: ', len(rbi_dropped_dup))
print(f'{len(rbi_dropped_na) - len(rbi_dropped_dup)} duplicate rows were dropped from rbi_dropped_na')

print(f'tot_bases_dropped_na original length: ', len(tot_bases_dropped_na))
tot_bases_dropped_dup = tot_bases_dropped_na.drop_duplicates()
print(f'tot_bases_dropped_dup length: ', len(tot_bases_dropped_dup))
print(f'{len(tot_bases_dropped_na) - len(tot_bases_dropped_dup)} duplicate rows were dropped from tot_bases_dropped_na')

print(f'stol_bases_dropped_na original length: ', len(stol_bases_dropped_na))
stol_bases_dropped_dup = stol_bases_dropped_na.drop_duplicates()
print(f'stol_bases_dropped_dup length: ', len(stol_bases_dropped_dup))
print(f'{len(stol_bases_dropped_na) - len(stol_bases_dropped_dup)} duplicate rows were dropped from stol_bases_dropped_na')


#check that all the rows displaying the stat name are the same - if not, fix any spelling errors
bat_avg_unique_stat_values = bat_avg_dropped_dup['stat'].unique()
print('bat_avg_unique_stat_values: ', bat_avg_unique_stat_values)
if len(bat_avg_unique_stat_values) > 1:
    print(f'Error with bat_avg stat column: contains more than one unique value.')

home_runs_unique_stat_values = home_runs_dropped_dup['stat'].unique()
print('home_runs_unique_stat_values: ', home_runs_unique_stat_values)
if len(home_runs_unique_stat_values) > 1:
    print('Error with home_run stat column: contains more than one unique value')

rbi_unique_stat_values = rbi_dropped_dup['stat'].unique()
print('rbi_unique_stat_values: ', rbi_unique_stat_values)
if len(rbi_unique_stat_values) > 1:
    print('Error with rbi stat column: contains more than one unique value')

tot_bases_unique_stat_values = tot_bases_dropped_dup['stat'].unique()
print('tot_bases_unique_stat_values: ', tot_bases_unique_stat_values)
if len(tot_bases_unique_stat_values) > 1:
    print('Error with tot_bases stat column: contains more than one unique value')

stol_bases_unique_stat_values = stol_bases_dropped_dup['stat'].unique()
print('stol_bases_unique_stat_values: ', stol_bases_unique_stat_values)
if len(stol_bases_unique_stat_values) > 1:
    print('Error with stol_bases stat column: contains more than one unique value')

#change year_text just to year
#check datatype before converting
#keep first four characters and convert to integer
print('bat_avg["year"] data type before conversion: ', bat_avg_dropped_dup.dtypes['year'])
bat_avg_dropped_dup['year'] = bat_avg_dropped_dup['year'].str[:4].astype(int)
print('bat_avg["year"] data type after conversion: ', bat_avg_dropped_dup.dtypes['year'])

print('home_runs["year"] data type before conversion: ', home_runs_dropped_dup.dtypes['year'])
home_runs_dropped_dup['year'] = home_runs_dropped_dup['year'].str[:4].astype(int)
print('home_runs["year"] data type after conversion: ', home_runs_dropped_dup.dtypes['year'])

print('rbi["year"] data type before conversion: ', rbi_dropped_dup.dtypes['year'])
rbi_dropped_dup['year'] = rbi_dropped_dup['year'].str[:4].astype(int)
print('rbi["year"] data type after conversion: ', rbi_dropped_dup.dtypes['year'])

print('tot_bases["year"] data type before conversion: ', tot_bases_dropped_dup.dtypes['year'])
tot_bases_dropped_dup['year'] = tot_bases_dropped_dup['year'].str[:4].astype(int)
print('tot_bases["year"] data type after conversion: ', tot_bases_dropped_dup.dtypes['year'])

print('stol_bases["year"] data type before conversion: ', stol_bases_dropped_dup.dtypes['year'])
stol_bases_dropped_dup['year'] = stol_bases_dropped_dup['year'].str[:4].astype(int)
print('stol_bases["year"] data type after conversion: ', stol_bases_dropped_dup.dtypes['year'])


#convert any numbers to either floats or integers (check dtypes before and after)
#batting avg should remain a float if it is already - or else, convert to float
print('bat_avg["number"] data type: ', bat_avg_dropped_dup.dtypes['number'])

#convert home runs, rbi, stolen bases, and total bases to integer
print('home_runs["number"] data type before conversion: ', home_runs_dropped_dup.dtypes['number'])
home_runs_dropped_dup['number'] = home_runs_dropped_dup['number'].astype(int)
print('home_runs["number"] data type after conversion: ', home_runs_dropped_dup.dtypes['number'])

print('rbi["number"] data type before conversion: ', rbi_dropped_dup.dtypes['number'])
rbi_dropped_dup['number'] = rbi_dropped_dup['number'].astype(int)
print('rbi["number"] data type after conversion: ', rbi_dropped_dup.dtypes['number'])

print('tot_bases["number"] data type before conversion: ', tot_bases_dropped_dup.dtypes['number'])
tot_bases_dropped_dup['number'] = tot_bases_dropped_dup['number'].astype(int)
print('tot_bases["number"] data type after conversion: ', tot_bases_dropped_dup.dtypes['number'])

print('stol_bases["number"] data type before conversion: ', stol_bases_dropped_dup.dtypes['number'])
stol_bases_dropped_dup['number'] = stol_bases_dropped_dup['number'].astype(int)
print('stol_bases["number"] data type after conversion: ', stol_bases_dropped_dup.dtypes['number'])


#combine team names so that Boston = Boston Red Sox, etc
#print unique values for teams columns
bat_avg_unique_team_values = bat_avg_dropped_dup['team'].unique()
print('bat_avg_unique_team_values: ', bat_avg_unique_team_values)

home_runs_unique_team_values = home_runs_dropped_dup['team'].unique()
print('home_runs_unique_team_values: ', home_runs_unique_team_values)

rbi_unique_team_values = rbi_dropped_dup['team'].unique()
print('rbi_unique_team_values: ', rbi_unique_team_values)

tot_bases_unique_team_values = tot_bases_dropped_dup['team'].unique()
print('tot_bases_unique_team_values: ', tot_bases_unique_team_values)

stol_bases_unique_team_values = stol_bases_dropped_dup['team'].unique()
print('stol_bases_unique_team_values: ', stol_bases_unique_team_values)


#build dictionary of key value pairs to replace old teams with newer team names
team_names = {
    'Boston': 'Boston Red Sox',
    'Seattle': 'Seattle Mariners',
    'Texas': 'Texas Rangers',
    'Minnesota': 'Minnesota Twins',
    'Detroit': 'Detroit Tigers',
    'Houston': 'Houston Astros',
    'Anaheim': 'Los Angeles Angels',
    'New York': 'New York Yankees',
    'Tampa Bay': 'Tampa Bay Rays',
    'Toronto': 'Toronto Blue Jays',
    'Baltimore': 'Baltimore Orioles',
    'Los Angeles': 'Los Angeles Angels',
    'Kansas City': 'Kansas City Royals',
    'Chicago': 'Chicago White Sox',
    'Oakland': 'Oakland Athletics',
    'Cleveland': 'Cleveland Guardians'
}

#replace values 
bat_avg_cleaned = bat_avg_dropped_dup.replace(team_names)
print('bat_avg_cleaned: \n', bat_avg_cleaned)

home_runs_cleaned = home_runs_dropped_dup.replace(team_names)
print('home_runs_cleaned: \n', home_runs_cleaned)

rbi_cleaned = rbi_dropped_dup.replace(team_names)
print('rbi_cleaned: \n', rbi_cleaned)

tot_bases_cleaned = tot_bases_dropped_dup.replace(team_names)
print('tot_bases_cleaned: \n', tot_bases_cleaned)

stol_bases_cleaned = stol_bases_dropped_dup.replace(team_names)
print('stol_bases_cleaned: \n', stol_bases_cleaned)


#check info for each df to make sure it has 25 columns and no na values and the correct dtypes
print('bat_avg_cleaned.info(): \n')
bat_avg_cleaned.info()

print('home_runs_cleaned.info(): \n')
home_runs_cleaned.info()

print('rbi_cleaned.info(): \n')
rbi_cleaned.info()

print('tot_bases_cleaned.info(): \n')
tot_bases_cleaned.info()

print('stol_bases_cleaned.info(): \n')
stol_bases_cleaned.info()


#convert dfs to csvs
try:
    bat_avg_cleaned.to_csv("csv/bat_avg_cleaned.csv", sep=',', header=True, index=False)
    home_runs_cleaned.to_csv("csv/home_runs_cleaned.csv", sep=',', header=True, index=False)
    rbi_cleaned.to_csv("csv/rbi_cleaned.csv", sep=',', header=True, index=False)
    tot_bases_cleaned.to_csv("csv/tot_bases_cleaned.csv", sep=',', header=True, index=False)
    stol_bases_cleaned.to_csv("csv/stol_bases_cleaned.csv", sep=',', header=True, index=False)
    print('All csv files have been created.')
except Exception as file_error:
    print(f'Error writing CSV files: {file_error}')
