#create interactive dashboard using either streamlit or dash

# Dashboard:
# sort by year (line graph) for each statistic
# sort by team for each statistic (bar graph)
# top 5 best players or teams for each statistic (bar graph)
# players with most records
# players - highest percentage of bases stolen (stacked bar graph or pie chart)


#Promedio de Bateo, Jonrones, Carreras Impulsadas, Bases Robadas, Total de Bases

import streamlit as st
import pandas as pd
import altair as alt
import sqlite3
from vega_datasets import data

##----------------------- Set up data frames ------------------------##
#connect to sqlite db
try:
    with sqlite3.connect('db/baseball.db') as conn:
            print('Database connected successfully')
            #turn on foreign key constraints
            conn.execute("PRAGMA foreign_keys = 1")
            #create cursor
            cursor = conn.cursor()
            # Read table into DataFrame
            baseball_df = pd.read_sql_query("SELECT * FROM baseball_data", conn)
except Exception as e:
      print(f'Error: {type(e).__name__} - {e}')

#generate list of all teams
teams_list = sorted(baseball_df['team'].unique())
print('teams_list data type: ', type(teams_list))
print('teams_list: ', teams_list)
#make lists of lat/long coordinates for teams
teams_lat = [39.29038, 42.35843, 41.85003, 41.505493, 42.33143, 29.76328, 39.099724, 34.05223, 44.986656, 40.837048, 37.804363, 47.608013, 27.964157, 32.705002, 43.651070,]
teams_lon = [-76.61219, -71.05977, -87.65005, -81.681290, -83.04575, -95.36327, -94.578331, -118.24368, -93.258133, -73.865433, -122.271111, -122.335167, -82.452606, -97.122780, -79.347015]
print(len(teams_list))
print(len(teams_lat))
print(len(teams_lon))
#turn teams, lat, and long into a new dataframe using a dictionary
lat_long_dict = {'team': teams_list, 'lat': teams_lat, 'long': teams_lon}
print('lat_long_dict: ', lat_long_dict)
lat_long_df = pd.DataFrame.from_dict(lat_long_dict)
#convert lat/long columns to float
lat_long_df['lat'] = pd.to_numeric(lat_long_df['lat'], errors='coerce')
lat_long_df['long'] = pd.to_numeric(lat_long_df['long'], errors='coerce')
print('lat_long_df: \n', lat_long_df.head())
#merge with filtered_df
baseball_lat_long = baseball_df.merge(lat_long_df, on='team')

# #add Spanish stat names to the df
# stats_sp = {'Batting Average': 'Promedio de Bateo', 'Home Runs': 'Jonrones', 'RBI': 'Carreras Impulsadas', 'Stolen Bases': 'Bases Robadas', 'Total Bases': 'Total de Bases'}

print('baseball_lat_long: \n', baseball_lat_long.head())
#check that data types are correct - if not, coerce numbers to floats or integers
print('baseball_lat_long data types: \n', baseball_lat_long.dtypes)


## --------------------------- Streamlit Dashboard Setup -------------------------------##
#Page Title
st.title('American League Baseball Data')

#Sidebar
#Language Toggle Button

#title
st.sidebar.title('Filter Options')
#year filter
min_year = int(baseball_lat_long['year'].min())
max_year = int(baseball_lat_long['year'].max())
print('min_year, max_year: ', min_year, max_year)
#year slider
yr_slider = st.sidebar.slider('Select Year Range', min_value=min_year, max_value=max_year, value=(min_year, max_year), label_visibility='visible')
#stat selector
stats=['Batting Average', 'Home Runs', 'RBI', 'Stolen Bases', 'Total Bases']
stats_en = st.sidebar.multiselect('Select Stat(s)', stats)


## -------------------Prepare data for charts-----------------------------

#set filters based on user's input
filtered_data = baseball_lat_long[
      (baseball_df['year'] >= yr_slider[0]) &
      (baseball_df['year'] <= yr_slider[1]) & 
      (baseball_df['stat'].isin(stats_en))
]

#group by team and stat to get all top teams
filtered_grouped = filtered_data.groupby(['team', 'stat']).max().reset_index()
#sort by stat and number, pull out top 5 for each stat
sorted_grouped = filtered_grouped.sort_values(['stat', 'number'], ascending=[True, False]).groupby('stat').head(5).reset_index(drop=True)
#add up all numbers to sort teams by total #
grouped_by_num = sorted_grouped.groupby('team').sum('number').reset_index().rename(columns={'number': 'total_num'})
#merge total_num column back in
resorted_grouped = sorted_grouped.merge(grouped_by_num, on='team')
#turn into a list that's sorted ascending
ordered_teams = resorted_grouped[['team', 'total_num']].sort_values('total_num', ascending=True)['team'].tolist()


## ----------------------------Create Charts ---------------------------------- ##
#line graph that plots stat vs year
st.subheader('Top Statistic(s) by Year')
stats_over_time = alt.Chart(filtered_data).mark_line().encode(
      x=alt.X('year', title='Year'),
      y=alt.Y('number', title='Number'),
      color=alt.Color('stat', title='Statistic')
)
st.altair_chart(stats_over_time, use_container_width=True)


## make grouped bar chart that plots top teams
st.subheader('Top Teams by Statistic(s)')
top_teams = alt.Chart(resorted_grouped).mark_bar().encode(
      x=alt.X('number:Q', title='Number'),
      y=alt.Y('team:N', title='Team', sort=ordered_teams),
      color=alt.Color('stat:N', title='Statistic'),
)
st.altair_chart(top_teams, use_container_width=True)


#make background map layer for teams map
states = alt.topo_feature(data.us_10m.url, 'states')
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project('albersUsa')

#plot locations of the top teams
top_teams_map = alt.Chart(filtered_data).mark_circle().encode(
    longitude='long:Q',
    latitude='lat:Q',
    size=alt.value(100),
    tooltip=['team', 'stat']
).project(
    'albersUsa'
)

#combine the base map and team locations
map_with_teams = background + top_teams_map
st.subheader('Top Teams by Location')
st.altair_chart(map_with_teams, use_container_width=True)

st.subheader('All Data')
st.dataframe(filtered_data)

#add team / player to tooltips (add year in map too?)
#fix commas in years