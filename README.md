# Baseball Data Analysis and Visualization
The purpose of this project is to scrape the major league baseball history website, analyze data, build a program that allows a user to query the data, and create an interactive data visualization dashboard.

The project consists of five parts:
1. Web scraping program
2. Data cleaning program
3. Program that imports the data into a SQLite database
4. Bilingual Spanish/English program hat allows a user to query the data based on specific categories
5. Interactive Streamlit data visualization dashboard that allows the user to filter data based on specific categories

The code could be modified to scrape more data, integrate more user-based queries, or add further charts to the dashboard.


# Description
This project is written using Python and SQLite.

The project consists of five parts. Parts 1-3 need to be run in order before parts 4 and 5.
1_web-scraping.py: This program uses Selenium to scrape the Hitting Statistics Leaderboards tables from the Year in Review pages of the [Baseball Almanac](https://www.baseball-almanac.com/yearmenu.shtml) website. It pulls the American League data from 2000-2024. It selects five statistics (Batting Average, Home Runs, RBI, Stolen Bases, and Total Bases) and writes one table per statistic into a csv file.
2_data-cleaning.py: This program converts the csv files to dataframes and uses Pandas to perform data cleaning such as removing duplicates and null values, converting each column to the appropriate data type, and updating the team names so they are all consistent with each other. It then converts the data back into new csv files.
3_database-import.py: This program uses SQLite to create and connect to a database, create tables, and insert the data from the cleaned csv files into the tables.
4_database-query.py: This program is written with both Python and SQLite. It uses input from the terminal to prompt a user to choose a language (either Spanish or English), and then select certain queries to run on the database. The user can select top players by statistic and then choose a statistic, top teams by year and then choose a year, or players who earned top spots more than once.
5_dashboard.py: This program uses Streamlit to run an interactive data visualization dashboard. In the sidebar on the left, a user can choose a year range and the statistic(s) to view. The dashboard then displays three different visualizations based on those filters - a line graph plotting the statistics over the years, a bar chart showing the top 5 players for each statistic, and a map showing the location of the top teams. Altair is used to create each chart. Additionaly, the raw filtered data are shown in table form at the bottom of the page. This table can be sorted based on column by clicking on a column name.


# Getting Started
Dependencies: Code editing software is required to run this project on your local machine. GitHub also offers their own free software called [GitHub Desktop](https://github.com/apps/desktop) which can be downloaded if needed. Python, pip, and the virtualenv package are also required. 
- Python can be downloaded from [python.org](https://www.python.org/downloads/). 
- Pip can be installed by typing the following command into your terminal: ```bash python -m pip install```
- Virtualenv can be installed by typing the following command into your terminal: ```pip install virtualenv```

1. Create and/or open a folder where you want to save the repository. In your code editor, navigate to that folder. Clone the repository using an SSH key by typing the following command into your terminal: 
```bash
git clone git@github.com:vnewto/baseball-data-analysis.git
```
2. Change your directory to the correct repository by typing the command 

```bash
cd baseball-data-analysis 
```
3. Set up and activate a virtual environment.

For Windows users, type the following into your terminal:

```bash python -m venv .venv```
```bash source .venv/Scripts/activate```

For Mac and Linux users, type the following into your terminal:

```bash python -m venv .venv```
```bash source .venv/Scripts/activate```

4. Install the project requirements within the virtual environment by typing ```bash pip install -r requirements.txt``` into your terminal while the venv is active.

5. Now you can run the project, view, and edit the code. Run the programs in the following order:
1. 1_web-scraping.py
2. 2_data-cleaning.py
3. 3_database-import.py
4. 4_database-query.py
5. 5_dashboard.py


# Troubleshooting
If you are unable to clone the repository to your local machine, check your coding program for updates.

If 5_dashboard.py is not loading in the browser, check your internet connection. 

Please [submit an issue](https://github.com/vnewto/baseball-data-analysis/issues) if you have any other problems.


# Contribution
The idea of this project is that it can be used by anyone to scrape, analyze, and view data from the Baseball Almanac. This project could also be modified to have a bilingual dashboard, incorporate more languages, scrape additional data or additional years (as early as 1901), add additional database queries, add more charts to the interactive dashboard, or anything else you can think of. Pull requests are welcome if you would like to make any changes.


# Authors
Valerie Newton


# Acknowledgements
This project is part of my classwork in the Python class through [Code the Dream](https://codethedream.org/). Thank you to all the wonderful mentors and volunteers who put this program together and helped me through it. 
