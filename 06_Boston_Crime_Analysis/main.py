"""
Boston Crime Data Visualization

Code exported from the original course notebook.
Dataset paths were made local so the project can be run from this folder.
"""

# Exercise 0 - Organizing Data

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import numpy as np
import matplotlib.pyplot as plt
import data_analytics_lib as dal
import random
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

DATA_DIR = Path(__file__).resolve().parent


def read_data(filepath):

    df = pd.read_csv(filepath, low_memory=False)
    
    return df

main_crime_df = read_data(DATA_DIR / "crime.csv")
main_crime_data = main_crime_df.to_dict("list")
print(f"Loaded {len(main_crime_df)} Boston crime records.")


# Exercise 1

import matplotlib.pyplot as plt


def get_crime_data_by_year(data, year):


    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]


    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]


    crime_db = {year: {}}


    # create empty dictionary
    for month in months:


        crime_db[year][month] = {}


        for day in days:
            crime_db[year][month][day] = [0] * 24


    # fill dictionary
    year_value = int(year)
    for i in range(len(data["YEAR"])):

        if int(data['YEAR'][i]) == year_value:

            month_num = int(data["MONTH"][i])
            month_name = months[month_num - 1]

            day = data["DAY_OF_WEEK"][i]
            hour = int(data["HOUR"][i])

            crime_db[str(year_value)][month_name][day][hour] += 1


    return crime_db

# TOTAL CRIMES EACH MONTH

def plot_month_totals(crime_db, year):


    months = list(crime_db[year].keys())
    totals = []


    for month in months:


        total = 0


        for day in crime_db[year][month]:
            total += sum(crime_db[year][month][day])


        totals.append(total)


    plt.figure(figsize=(12,5))
    plt.bar(months, totals)
    plt.title("Total Crimes Each Month")
    plt.ylabel("Crimes")
    plt.show()

# CRIMES BY DAY OF WEEK FOR EACH MONTH

def plot_days_by_month(crime_db, year):


    months = list(crime_db[year].keys())


    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]


    plt.figure(figsize=(12,6))


    totals = []


    for day in days:
        total = 0
        for month in months:
            total += sum(crime_db[year][month][day])
        totals.append(total)


    plt.bar(days, totals)
    plt.title("Total Crimes by Day of Week (All Months)")
    plt.ylabel("Crimes")
    plt.show()


def plot_month_day_of_week(crime_db, year, month):


    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]
    totals = [sum(crime_db[year][month][day]) for day in days]


    plt.figure(figsize=(10,5))
    plt.bar(days, totals, color="tab:blue")
    plt.title(f"Data for Month of {month} Year {year} Total Crimes {sum(totals)}")
    plt.ylabel("Number of Crimes")
    plt.xlabel("Day of Week")
    plt.show()


# Temp Values - gonna change to inputs later
year = 2016
selected_month = "October"
selected_day = "Monday"

yearly_crime_db = get_crime_data_by_year(main_crime_data, str(year))

# plot_month_totals(crime_db, year)
plot_month_day_of_week(yearly_crime_db, str(year), selected_month)


# Exercise 2 - Pick a specific year, plot the location of all the crimes committed for each day of the week over the entire year on separate plots. There will be 7 separate plots, one for each day of the week. Are more crimes being committed in certain areas as a function of week day ?

title = f'All crimes committed on {selected_day} in Boston'

crime_results = main_crime_df[
    (main_crime_df['DAY_OF_WEEK'] == selected_day) &
    (main_crime_df['YEAR'] == year)
].copy()

fig = px.scatter_map(crime_results,
                    lon='Long', lat='Lat',
                    hover_data=['MONTH', 'STREET'],
                    title=title,
                    zoom=12,
                    height=800
                   )

fig.update_layout(map=dict(style="open-street-map"))
fig.update_traces(marker = dict(size=10, color='red'))

output_path = DATA_DIR / "boston_crime_map.html"
fig.write_html(output_path, auto_open=False)
print(f"Saved Boston crime map to {output_path}")

