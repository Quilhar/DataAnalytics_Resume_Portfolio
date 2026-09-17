"""
Climate Data Analysis & Time-Series Statistics

Portfolio version of a data-analysis project originally developed as coursework.

Research question:
How have long-term temperature and precipitation patterns changed, and what can smoothed time-series statistics reveal about those trends?

Note:
The code is preserved from the original analysis with project-local paths. Before
publishing publicly, verify dataset provenance, methodology, and course attribution.
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data_analytics_lib as dal

DATA_DIR = Path(__file__).resolve().parent

n = 20
weight_list = n * [1]


# STEP 1

def read_csv(filename):
    
    csvfile = filename
    
    df = pd.read_csv(csvfile)
    
    return df

def extract_monthly_temp_data(df):
    
    january_temps_df = df['January Temp(F)']
    february_temps_df = df['February Temp(F)']
    march_temps_df = df['March Temp(F)']
    april_temps_df = df['April Temp(F)']
    may_temps_df = df['May Temp(F)']    
    june_temps_df = df['June Temp(F)']
    july_temps_df = df['July Temp(F)']
    august_temps_df = df['August Temp(F)']
    september_temps_df = df['September Temp(F)']
    october_temps_df = df['October Temp(F)']
    november_temps_df = df['November Temp(F)']
    december_temps_df = df['December Temp(F)']
    
    all_months_temps = {
        'January': january_temps_df,
        'February': february_temps_df,
        'March': march_temps_df,
        'April': april_temps_df,
        'May': may_temps_df,
        'June': june_temps_df,
        'July': july_temps_df,
        'August': august_temps_df,
        'September': september_temps_df,
        'October': october_temps_df,
        'November': november_temps_df,
        'December': december_temps_df
    }
    
    return all_months_temps

def extract_monthly_pcp_data(df):
    
    january_pcp_df = df['January Inches']
    february_pcp_df = df['February Inches']
    march_pcp_df = df['March Inches']
    april_pcp_df = df['April Inches']
    may_pcp_df = df['May Inches']    
    june_pcp_df = df['June Inches']
    july_pcp_df = df['July Inches']
    august_pcp_df = df['August Inches']
    september_pcp_df = df['September Inches']
    october_pcp_df = df['October Inches']
    november_pcp_df = df['November Inches']
    december_pcp_df = df['December Inches']
    
    all_months_pcp = {
        'January': january_pcp_df,
        'February': february_pcp_df,
        'March': march_pcp_df,
        'April': april_pcp_df,
        'May': may_pcp_df,
        'June': june_pcp_df,
        'July': july_pcp_df,
        'August': august_pcp_df,
        'September': september_pcp_df,
        'October': october_pcp_df,
        'November': november_pcp_df,
        'December': december_pcp_df
    }
    
    return all_months_pcp

monthly_temps_df = read_csv(DATA_DIR / 'All_Months_Temp_1895_2022 (1).csv')
monthly_pcp_df = read_csv(DATA_DIR / 'All_Months_PCP_1895_2022_1.csv')

month_temps = extract_monthly_temp_data(monthly_temps_df)
month_pcp = extract_monthly_pcp_data(monthly_pcp_df)

temps_year = monthly_temps_df['Date']
pcp_year = monthly_pcp_df['Date']


# Plotting Monthly Temperatures vs Year

dal.plot_weighted_moving_average_data(temps_year, month_temps['January'], weight_list, 'January Temperatures with Weighted Moving Average', 'Temperature (F)', 'January Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, month_temps['February'], weight_list, 'February Temperatures with Weighted Moving Average', 'Temperature (F)', 'February Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, month_temps['March'], weight_list, 'March Temperatures with Weighted Moving Average', 'Temperature (F)', 'March Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, month_temps['April'], weight_list, 'April Temperatures with Weighted Moving Average', 'Temperature (F)', 'April Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, month_temps['May'], weight_list, 'May Temperatures with Weighted Moving Average', 'Temperature (F)', 'May Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, month_temps['June'], weight_list, 'June Temperatures with Weighted Moving Average', 'Temperature (F)', 'June Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, month_temps['July'], weight_list, 'July Temperatures with Weighted Moving Average', 'Temperature (F)', 'July Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, month_temps['August'], weight_list, 'August Temperatures with Weighted Moving Average', 'Temperature (F)', 'August Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, month_temps['September'], weight_list, 'September Temperatures with Weighted Moving Average', 'Temperature (F)', 'September Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, month_temps['October'], weight_list, 'October Temperatures with Weighted Moving Average', 'Temperature (F)', 'October Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, month_temps['November'], weight_list, 'November Temperatures with Weighted Moving Average', 'Temperature (F)', 'November Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, month_temps['December'], weight_list, 'December Temperatures with Weighted Moving Average', 'Temperature (F)', 'December Temperatures vs Year')


# Plotting Monthly PCP vs Year

dal.plot_weighted_moving_average_data(pcp_year, month_pcp['January'], weight_list, 'January Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'January Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, month_pcp['February'], weight_list, 'February Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'February Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, month_pcp['March'], weight_list, 'March Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'March Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, month_pcp['April'], weight_list, 'April Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'April Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, month_pcp['May'], weight_list, 'May Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'May Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, month_pcp['June'], weight_list, 'June Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'June Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, month_pcp['July'], weight_list, 'July Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'July Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, month_pcp['August'], weight_list, 'August Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'August Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, month_pcp['September'], weight_list, 'September Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'September Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, month_pcp['October'], weight_list, 'October Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'October Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, month_pcp['November'], weight_list, 'November Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'November Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, month_pcp['December'], weight_list, 'December Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'December Precipitation vs Year')


# STEP 2 - Analyzing the Raw Data

# A - Compute the mean, median, standard deviation, max and min for each year across all months

temp_year_stats = {'max': [], 'min': [], 'mean': [], 'median': [], 'standard_dev': []}


for i in range(len(temps_year)):
    year_data = monthly_temps_df.iloc[i, 1:13]
    
    temp_year_stats['max'].append(np.max(year_data))
    temp_year_stats['min'].append(np.min(year_data))
    temp_year_stats['mean'].append(np.mean(year_data))
    temp_year_stats['median'].append(np.median(year_data))
    temp_year_stats['standard_dev'].append(np.std(year_data))
    
pcp_year_stats = {'max': [], 'min': [], 'mean': [], 'median': [], 'standard_dev': []}

for i in range(len(pcp_year)):
    year_data = monthly_pcp_df.iloc[i, 1:13]
    
    pcp_year_stats['max'].append(np.max(year_data))
    pcp_year_stats['min'].append(np.min(year_data))
    pcp_year_stats['mean'].append(np.mean(year_data))
    pcp_year_stats['median'].append(np.median(year_data))
    pcp_year_stats['standard_dev'].append(np.std(year_data))


# B - Compute the mean, median, standard deviation, max and min for each month across all years. Determine the year where each max and min occurred for each month.

temp_month_stats = {'max': [], 'min': [], 'mean': [], 'median': [], 'standard_dev': [], 'max_year': [], 'min_year': []}
month_temp_keys = list(month_temps.keys())

for i in range(len(month_temps)):
    month_data = month_temps[month_temp_keys[i]]
    
    temp_month_stats['max'].append(np.max(month_data))
    temp_month_stats['min'].append(np.min(month_data))
    temp_month_stats['mean'].append(np.mean(month_data))
    temp_month_stats['median'].append(np.median(month_data))
    temp_month_stats['standard_dev'].append(np.std(month_data))
    
    max_value = temp_month_stats['max'][i]
    min_value = temp_month_stats['min'][i]
    
    max_index = month_data[month_data == max_value].index[0]
    min_index = month_data[month_data == min_value].index[0]
    
    temp_month_stats['max_year'].append(temps_year[max_index])
    temp_month_stats['min_year'].append(temps_year[min_index])
    
pcp_month_stats = {'max': [], 'min': [], 'mean': [], 'median': [], 'standard_dev': [], 'max_year': [], 'min_year': []}
month_pcp_keys = list(month_pcp.keys())

for i in range(len(month_pcp)):
    month_data = month_pcp[month_pcp_keys[i]]
    
    pcp_month_stats['max'].append(np.max(month_data))
    pcp_month_stats['min'].append(np.min(month_data))
    pcp_month_stats['mean'].append(np.mean(month_data))
    pcp_month_stats['median'].append(np.median(month_data))
    pcp_month_stats['standard_dev'].append(np.std(month_data))
    
    max_value = pcp_month_stats['max'][i]
    min_value = pcp_month_stats['min'][i]
    
    max_index = month_data[month_data == max_value].index[0]
    min_index = month_data[month_data == min_value].index[0]
    
    pcp_month_stats['max_year'].append(pcp_year[max_index])
    pcp_month_stats['min_year'].append(pcp_year[min_index])


# C - Plot the raw data and moving weighted average filtered data for the mean, median, min and max as a function of year one plot. Plot the yearly standard deviation and its moving weighted average filtered data on a second plot.

# Temperature Raw Data Graphs

dal.plot_weighted_moving_average_data(temps_year, temp_year_stats['mean'], weight_list, 'Yearly Mean Temperatures with Weighted Moving Average', 'Temperature (F)', 'Yearly Mean Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, temp_year_stats['median'], weight_list, 'Yearly Median Temperatures with Weighted Moving Average', 'Temperature (F)', 'Yearly Median Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, temp_year_stats['max'], weight_list, 'Yearly Max Temperatures with Weighted Moving Average', 'Temperature (F)', 'Yearly Max Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, temp_year_stats['min'], weight_list, 'Yearly Min Temperatures with Weighted Moving Average', 'Temperature (F)', 'Yearly Min Temperatures vs Year')


dal.plot_weighted_moving_average_data(temps_year, temp_year_stats['standard_dev'], weight_list, 'Yearly Standard Deviation of Temperatures with Weighted Moving Average', 'Temperature (F)', 'Yearly Standard Deviation of Temperatures vs Year')


# PCP Raw Data Graphs

dal.plot_weighted_moving_average_data(pcp_year, pcp_year_stats['mean'], weight_list, 'Yearly Mean Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'Yearly Mean Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, pcp_year_stats['median'], weight_list, 'Yearly Median Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'Yearly Median Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, pcp_year_stats['max'], weight_list, 'Yearly Max Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'Yearly Max Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, pcp_year_stats['min'], weight_list, 'Yearly Min Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'Yearly Min Precipitation vs Year')


dal.plot_weighted_moving_average_data(pcp_year, pcp_year_stats['standard_dev'], weight_list, 'Yearly Standard Deviation of Precipitation with Weighted Moving Average', 'Precipitation (Inches)', 'Yearly Standard Deviation of Precipitation vs Year')


# D - For each month, plot the year that maximum and minimum values were obtained.

# Year that maximum and minimum values were obtained for temp and pcp

plt.scatter(month_temp_keys, temp_month_stats['max_year'])
plt.tight_layout()
plt.xlabel('Months')
plt.ylabel('Year of Max Temperature')
plt.title('Year of Maximum Monthly Temperatures')
plt.xticks(month_temp_keys, rotation=45, ha='right') 
plt.show()


plt.scatter(month_temp_keys, temp_month_stats['min_year'])
plt.tight_layout()
plt.xlabel('Months')
plt.ylabel('Year of Min Temperature')
plt.title('Year of Minimum Monthly Temperatures')
plt.xticks(month_temp_keys, rotation=45, ha='right') 
plt.show()


plt.scatter(month_pcp_keys, pcp_month_stats['max_year'])
plt.tight_layout()
plt.xlabel('Months')
plt.ylabel('Year of Max Precipitation')
plt.title('Year of Maximum Monthly Precipitation')
plt.xticks(month_pcp_keys, rotation=45, ha='right') 
plt.show()


plt.scatter(month_pcp_keys, pcp_month_stats['min_year'])
plt.tight_layout()
plt.xlabel('Months')
plt.ylabel('Year of Min Precipitation')
plt.title('Year of Minimum Monthly Precipitation')
plt.xticks(month_pcp_keys, rotation=45, ha='right') 
plt.show()


# STEP 3 - Identifying Trends

# Make estimates for what the current rate of temperature and precipitation increase are.

weighted_temp_data = dal.weighted_moving_average_filter(temp_year_stats['mean'], weight_list)
weighted_temp_year = dal.weighted_moving_average_filter(temps_year, weight_list)

coefficients_temp = dal.least_squares_coefficient(weighted_temp_year[76:], weighted_temp_data[76:], ifit=1)

print(f'Linear Least Squares Coefficients for Temp (m, b): {coefficients_temp}')

weighted_pcp_data = dal.weighted_moving_average_filter(pcp_year_stats['mean'], weight_list)
weighted_pcp_year = dal.weighted_moving_average_filter(pcp_year, weight_list)

coefficients_pcp = dal.least_squares_coefficient(weighted_pcp_year[76:], weighted_pcp_data[76:], ifit=1)
print(f'Linear Least Squares Coefficients for PCP (m, b): {coefficients_pcp}')


# Estimated Mean Temperatures in 2025, 2030, 2035

def linear_eq(x, m, b):
    y = m * x + b
    
    return y

est_2025_temp = linear_eq(2025, coefficients_temp[0][0], coefficients_temp[0][1])
print(f'Estimated Mean Temperature for 2025: {est_2025_temp} F')

est_2030_temp = linear_eq(2030, coefficients_temp[0][0], coefficients_temp[0][1])
print(f'Estimated Mean Temperature for 2030: {est_2030_temp} F')

est_2035_temp = linear_eq(2035, coefficients_temp[0][0], coefficients_temp[0][1])
print(f'Estimated Mean Temperature for 2035: {est_2035_temp} F')


# Correlation coefficients for time and temperature

time_period_1 = weighted_temp_year[:39]
time_period_2 = weighted_temp_year[39:76]
time_period_3 = weighted_temp_year[76:]

cc_time_period_1 = dal.find_data_correlation(time_period_1, weighted_temp_data[:39])
cc_time_period_2 = dal.find_data_correlation(time_period_2, weighted_temp_data[39:76])
cc_time_period_3 = dal.find_data_correlation(time_period_3, weighted_temp_data[76:])

print(cc_time_period_1)
print(cc_time_period_2)
print(cc_time_period_3)


# Corelation coefficients for temperature and precipitation

weighted_pcp_data = dal.weighted_moving_average_filter(pcp_year_stats['mean'], weight_list)


cc_temperature_precipitation = dal.find_data_correlation(weighted_temp_data[89:], weighted_pcp_data[89:])

print(cc_temperature_precipitation)

