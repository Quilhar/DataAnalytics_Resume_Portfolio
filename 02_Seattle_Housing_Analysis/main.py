"""
Seattle Housing Data Analysis

Portfolio version of a data-analysis project originally developed as coursework.

Research question:
What patterns appear in Seattle home prices and property characteristics, and which variables are most useful for explaining differences in price?

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
import random

DATA_DIR = Path(__file__).resolve().parent


# Exercise 1 - Write a python function that reads in the Seattle housing data and puts it into an appropriate data structure(s). Note, there some entries in the database where price, sqftliving and sqftlot are equal to 0. There may be explanations for these entries or they might be input errors. Exclude these records from your analyses.

def read_data(file_path):

    data_by_statezip = {}

    with open(file_path, "r") as file:
        next(file)  # Skip the header line
        
        for line in file:

            lines = line.strip().split(",")

            zip_code = lines[-2]
            
            if zip_code not in data_by_statezip:
                data_by_statezip[zip_code] = {
                    'date': [],
                    'price': [],
                    'bedrooms': [],
                    'bathrooms': [],
                    'sqft_living': [],
                    'sqft_lot': [],
                    'floors': [],
                    'waterfront': [],
                    'view': [],
                    'condition': [],
                    'sqft_above': [],
                    'sqft_basement': [],
                    'yr_built': [],
                    'yr_renovated': [],
                    'street': [],
                    'city': [],
                    'country': []
                }
            # if lines[1] == '0' or lines[4] == '0' or lines[5] == '0':
            #     continue
            
            # else:
            data_by_statezip[zip_code]['date'].append(lines[0])
            data_by_statezip[zip_code]['price'].append(float(lines[1]))
            data_by_statezip[zip_code]['bedrooms'].append(float(lines[2]))
            data_by_statezip[zip_code]['bathrooms'].append(float(lines[3]))
            data_by_statezip[zip_code]['sqft_living'].append(float(lines[4]))
            data_by_statezip[zip_code]['sqft_lot'].append(float(lines[5]))
            data_by_statezip[zip_code]['floors'].append(float(lines[6]))
            data_by_statezip[zip_code]['waterfront'].append(float(lines[7]))
            data_by_statezip[zip_code]['view'].append(float(lines[8]))
            data_by_statezip[zip_code]['condition'].append(float(lines[9]))
            data_by_statezip[zip_code]['sqft_above'].append(float(lines[10]))
            data_by_statezip[zip_code]['sqft_basement'].append(float(lines[11]))
            data_by_statezip[zip_code]['yr_built'].append(float(lines[12]))
            data_by_statezip[zip_code]['yr_renovated'].append(float(lines[13]))
            data_by_statezip[zip_code]['street'].append(lines[14])
            data_by_statezip[zip_code]['city'].append(lines[15])
            data_by_statezip[zip_code]['country'].append(lines[17])
            
            

    return data_by_statezip

state_zip_data = read_data(DATA_DIR / "housing_data.csv")

print(state_zip_data)


# Exercise 2

# A. Investigate the correlation between the size of the house (sqftliving) and price and the lot size (sqftlot) and price by computing the correlation coefficient. Note, there some entries in the database where price is equal to 0. When doing computations that involve the price exclude these entries from your computation.

price_list = []
sqft_living_list = []
sqft_lot_list = []
condition_list = []



for zip in state_zip_data.keys():
    for i in range(len(state_zip_data[zip]['price'])):
        if (state_zip_data[zip]['price'][i] > 0 and state_zip_data[zip]['price'][i] <= 5000000) and (state_zip_data[zip]['sqft_lot'][i] > 0 and state_zip_data[zip]['sqft_lot'][i] <= 200000):
            price_list.append(state_zip_data[zip]['price'][i])
            sqft_living_list.append(state_zip_data[zip]['sqft_living'][i])
            sqft_lot_list.append(state_zip_data[zip]['sqft_lot'][i])
            condition_list.append(state_zip_data[zip]['condition'][i])


print(len(price_list))
correlation_price_sqft_lot = dal.find_data_correlation(price_list, sqft_lot_list)
correlation_price_sqft_living = dal.find_data_correlation(price_list, sqft_living_list)


print(f'Corelation Coefficient of Price to Square Foot Living: {correlation_price_sqft_living}')
print(f'Corelation Coefficient of Price to Square Foot Lot: {correlation_price_sqft_lot}')


# B. Develop a linear regression model for cost for each of the two independent variables sqftliving and sqftlot with price. Plot the graphs for each model. On the plots show the raw data , the regression line and the two sigma error bars. Which one is a better predictor?

plt.figure(figsize=(20, 10))
dal.graph__least_squares(sqft_lot_list, price_list)
dal.graphing_error_bars(sqft_lot_list, price_list, fit = 1, xlabel='Square Foot Lot', ylabel='Price', title='Price vs Square Foot Lot')


plt.figure(figsize=(20, 10))
dal.graph__least_squares(sqft_living_list, price_list)
dal.graphing_error_bars(sqft_living_list, price_list, fit = 1, xlabel='Square Foot Living', ylabel='Price', title='Price vs Square Foot Living')


# Square Foot Living is a much better predictor as the fit of the line is much better, and the data stays in the error bars much more.

# C. Choose one idea from those discussed in class other than those in parts a and b. Provide your analysis and the reasons why you choose the analytical techniques you did.

# Sorting the conditions with prices. Each condition will have a list of prices associated with it. I'm doing this because the scale between prices and conditions vary significantly, both with number of varying data available and the price ranges themselves. Then I'm going to get the regular statistics of each to get a read on how condition affects things like average price.

matched_conditions_with_price = {condition: [] for condition in condition_list}

print(matched_conditions_with_price)
for i in range(len(condition_list)):
    condition = condition_list[i]
    price = price_list[i]
    matched_conditions_with_price[condition].append(price)

condition_stats1 = dal.main_stats(matched_conditions_with_price[1.0])
condition_stats2 = dal.main_stats(matched_conditions_with_price[2.0])
condition_stats3 = dal.main_stats(matched_conditions_with_price[3.0])
condition_stats4 = dal.main_stats(matched_conditions_with_price[4.0])
condition_stats5 = dal.main_stats(matched_conditions_with_price[5.0])

print(f'Stats for a condition of 1: {condition_stats1}')
print(f'Stats for a condition of 2: {condition_stats2}')
print(f'Stats for a condition of 3: {condition_stats3}')
print(f'Stats for a condition of 4: {condition_stats4}')
print(f'Stats for a condition of 5: {condition_stats5}')


# Project Code

# Getting the Statistics for each Zipcode

# Cleaning the state_zip_data

cleaned_state_zip_data = {}

for zip in state_zip_data.keys():
    if zip not in cleaned_state_zip_data:
        cleaned_state_zip_data[zip] = {
                'price': [],
                'bathrooms': [],
                'bedrooms': [],
                'sqft_living': [],
                'sqft_lot': [],
                'yr_built': []
            }
            
        for i in range(len(state_zip_data[zip]['price'])):
            
            if (state_zip_data[zip]['price'][i] > 0 and state_zip_data[zip]['price'][i] <= 5000000) and (state_zip_data[zip]['sqft_lot'][i] > 0 and state_zip_data[zip]['sqft_lot'][i] <= 200000):

                cleaned_state_zip_data[zip]['price'].append(state_zip_data[zip]['price'][i])
                cleaned_state_zip_data[zip]['bathrooms'].append(state_zip_data[zip]['bathrooms'][i])
                cleaned_state_zip_data[zip]['bedrooms'].append(state_zip_data[zip]['bedrooms'][i])
                cleaned_state_zip_data[zip]['sqft_living'].append(state_zip_data[zip]['sqft_living'][i])
                cleaned_state_zip_data[zip]['sqft_lot'].append(state_zip_data[zip]['sqft_lot'][i])
                cleaned_state_zip_data[zip]['yr_built'].append(state_zip_data[zip]['yr_built'][i])




# Getting statistics for the specific zip code

def zip_code_stats(state_zip_data, zipcode):
    specific_zip = zipcode
    zip_code_stats = {}

    for zip_code in cleaned_state_zip_data.keys():

        if zip_code == f'WA {specific_zip}':
            price_stats = dal.main_stats(cleaned_state_zip_data[zip_code]['price'])
            bathroom_stats = dal.main_stats(cleaned_state_zip_data[zip_code]['bathrooms'])
            bedroom_stats = dal.main_stats(cleaned_state_zip_data[zip_code]['bedrooms'])
            sqft_living_stats = dal.main_stats(cleaned_state_zip_data[zip_code]['sqft_living'])
            sqft_lot_stats = dal.main_stats(cleaned_state_zip_data[zip_code]['sqft_lot'])
            year_stats = dal.main_stats(cleaned_state_zip_data[zip_code]['yr_built'])

            zip_code_stats = {
                'Price': {'min': price_stats['min'], 'max': price_stats['max'], 'mean': price_stats['mean'], 'median': price_stats['median'], 'stdev': price_stats['std_dev']},
                'bathrooms': {'min': bathroom_stats['min'], 'max': bathroom_stats['max'], 'mean': bathroom_stats['mean'], 'median': bathroom_stats['median'], 'stdev': bathroom_stats['std_dev']},
                'bedrooms': {'min': bedroom_stats['min'], 'max': bedroom_stats['max'], 'mean': bedroom_stats['mean'], 'median': bedroom_stats['median'], 'stdev': bedroom_stats['std_dev']},
                'SqFt_Living': {'min': sqft_living_stats['min'], 'max': sqft_living_stats['max'], 'mean': sqft_living_stats['mean'], 'median': sqft_living_stats['median'], 'stdev': sqft_living_stats['std_dev']},
                'SqFt_Lot': {'min': sqft_lot_stats['min'], 'max': sqft_lot_stats['max'], 'mean': sqft_lot_stats['mean'], 'median': sqft_lot_stats['median'], 'stdev': sqft_lot_stats['std_dev']},
                'Year': {'min': year_stats['min'], 'max': year_stats['max'], 'mean': year_stats['mean'], 'median': year_stats['median'], 'stdev': year_stats['std_dev']}
            }

    return zip_code_stats


zip_code_statistics_98042 = zip_code_stats(cleaned_state_zip_data, '98042')
zip_code_statistics_98006 = zip_code_stats(cleaned_state_zip_data, '98006')
zip_code_statistics_98103 = zip_code_stats(cleaned_state_zip_data, '98103')

zip_df_98042 = pd.DataFrame(zip_code_statistics_98042)
zip_df_98006 = pd.DataFrame(zip_code_statistics_98006)
zip_df_98103 = pd.DataFrame(zip_code_statistics_98103)

zip_df_98042


# Histograms for the Zipcodes

plt.figure(figsize=(20, 10))

dal.histogram(cleaned_state_zip_data['WA 98042']['price'], color = 'blue', xaxis_label='Price', yaxis_label='Frequency', title='Price Distribution for Zip Code 98042')
plt.axvline(x=dal.main_stats(cleaned_state_zip_data['WA 98042']['price'])['median'], color='purple', linestyle='-', label='Median Price')
plt.title('Zip Code 98042')

plt.legend()
plt.show()


plt.figure(figsize=(20, 10))

dal.histogram(cleaned_state_zip_data['WA 98006']['price'], color = 'green', xaxis_label='Price', yaxis_label='Frequency', title='Price Distribution for Zip Code 98006')
plt.axvline(x=dal.main_stats(cleaned_state_zip_data['WA 98006']['price'])['median'], color='purple', linestyle='-', label='Median Price')
plt.title('Zip Code 98006')

plt.legend()
plt.show()


plt.figure(figsize=(20, 10))

dal.histogram(cleaned_state_zip_data['WA 98103']['price'], color = 'red', xaxis_label='Price', yaxis_label='Frequency', title='Price Distribution for Zip Code 98103')
plt.axvline(x=dal.main_stats(cleaned_state_zip_data['WA 98103']['price'])['median'], color='purple', linestyle='-', label='Median Price')
plt.title('Zip Code 98103')

plt.legend()    
plt.show()


# Least Squares Fit of the Price as a Function of Sqftliving along with CC

plt.Figure(figsize=(20, 10))
dal.graph__least_squares(cleaned_state_zip_data['WA 98042']['sqft_living'], cleaned_state_zip_data['WA 98042']['price'])
dal.graphing_error_bars(cleaned_state_zip_data['WA 98042']['sqft_living'], cleaned_state_zip_data['WA 98042']['price'], fit = 1, xlabel='Square Foot Living', ylabel='Price', title='Price vs Square Foot Living for Zip Code 98042')
dal.find_data_correlation(cleaned_state_zip_data['WA 98042']['sqft_living'], cleaned_state_zip_data['WA 98042']['price'])


plt.Figure(figsize=(20, 10))
dal.graph__least_squares(cleaned_state_zip_data['WA 98006']['sqft_living'], cleaned_state_zip_data['WA 98006']['price'])
dal.graphing_error_bars(cleaned_state_zip_data['WA 98006']['sqft_living'], cleaned_state_zip_data['WA 98006']['price'], fit = 1, xlabel='Square Foot Living', ylabel='Price', title='Price vs Square Foot Living for Zip Code 98006')
dal.find_data_correlation(cleaned_state_zip_data['WA 98006']['sqft_living'], cleaned_state_zip_data['WA 98006']['price'])


plt.Figure(figsize=(20, 10))
dal.graph__least_squares(cleaned_state_zip_data['WA 98103']['sqft_living'], cleaned_state_zip_data['WA 98103']['price'])
dal.graphing_error_bars(cleaned_state_zip_data['WA 98103']['sqft_living'], cleaned_state_zip_data['WA 98103']['price'], fit = 1, xlabel='Square Foot Living', ylabel='Price', title='Price vs Square Foot Living for Zip Code 98103')
dal.find_data_correlation(cleaned_state_zip_data['WA 98103']['sqft_living'], cleaned_state_zip_data['WA 98103']['price'])


# Project Code 4A: A Real Estate

def get_user_input(data):
    state_zip_data = data
    requested_data = {}  
    matching_listings = []
    matching_listing_data = {
       
    }
    top_5_listings = {}

    default_values = {
        'zip': '98042',
        'bed_min': 2.0,
        'bed_max': 4.0,
        'bath_min': 1.5,
        'bath_max': 3.0,
        'sqft_min': 1200.0,
        'sqft_max': 2500.0,
        'price_min': 200000.0,
        'price_max': 800000.0,
    }

    interactive_mode = '--interactive' in sys.argv

    if interactive_mode:
        zip = input("Please enter your ZIP code: ")
        bed_min = float(input("Please enter the minimum number of bedrooms: "))
        bed_max = float(input("Please enter the maximum number of bedrooms: "))
        bath_min = float(input("Please enter the minimum number of bathrooms: "))
        bath_max = float(input("Please enter the maximum number of bathrooms: "))
        sqft_min = float(input("Please enter the minimum square footage: "))
        sqft_max = float(input("Please enter the maximum square footage: "))
        price_min = float(input("Please enter the minimum desired price: "))
        price_max = float(input("Please enter the maximum desired price: "))
    else:
        zip = default_values['zip']
        bed_min = default_values['bed_min']
        bed_max = default_values['bed_max']
        bath_min = default_values['bath_min']
        bath_max = default_values['bath_max']
        sqft_min = default_values['sqft_min']
        sqft_max = default_values['sqft_max']
        price_min = default_values['price_min']
        price_max = default_values['price_max']


    requested_data["zip"] = f'WA {zip}'
    requested_data["bedrooms"] = [bed_min, bed_max]
    requested_data["bathrooms"] = [bath_min, bath_max]
    requested_data["sqft"] = [sqft_min, sqft_max]
    requested_data["price"] = [price_min, price_max]


    ### Finding all listings that satisfy the requirements
    for zipcode in state_zip_data:
        for i in range(len(state_zip_data[zipcode]['price'])):
            if (zipcode == requested_data['zip'] and
                state_zip_data[zipcode]["bedrooms"][i] >= requested_data["bedrooms"][0] and
                state_zip_data[zipcode]["bedrooms"][i] <= requested_data["bedrooms"][1] and
                state_zip_data[zipcode]["bathrooms"][i] >= requested_data["bathrooms"][0] and
                state_zip_data[zipcode]["bathrooms"][i] <= requested_data["bathrooms"][1] and
                state_zip_data[zipcode]["sqft_living"][i] >= requested_data["sqft"][0] and
                state_zip_data[zipcode]["sqft_living"][i] <= requested_data["sqft"][1] and
                state_zip_data[zipcode]["price"][i] >= requested_data["price"][0] and
                state_zip_data[zipcode]["price"][i] <= requested_data["price"][1]):


                    matching_listings.append(i)


                    if state_zip_data[zipcode]["street"][i] not in matching_listing_data:
                        matching_listing_data[state_zip_data[zipcode]["street"][i]] = {
                            "bedrooms": state_zip_data[zipcode]["bedrooms"][i],
                            "bathrooms": state_zip_data[zipcode]["bathrooms"][i],
                            "sqft_living": state_zip_data[zipcode]["sqft_living"][i],
                            "price": state_zip_data[zipcode]["price"][i]
                        }

    # Printing the requested data
    print(f""""Requested Data:
    ZIP Code: {requested_data["zip"]}
    Bedrooms Minimum: {requested_data["bedrooms"][0]}
    Bedrooms Maximum: {requested_data["bedrooms"][1]}
    Bathrooms Minimum: {requested_data["bathrooms"][0]}
    Bathrooms Maximum: {requested_data["bathrooms"][1]}
    Square Footage Minimum: {requested_data["sqft"][0]}
    Square Footage Maximum: {requested_data["sqft"][1]}
    Price Minimum: {requested_data["price"][0]}
    Price Maximum: {requested_data["price"][1]}
    """)

    ### Getting the 5 best matching listings
   
    ## Normalizing the data for the distance test
    normalized_data = {}
    normalized_target = {}


    beds_list = []
    baths_list = []
    sqfts_list = []
    prices_list = []


    for street in matching_listing_data:
        beds_list.append(matching_listing_data[street]["bedrooms"])
        baths_list.append(matching_listing_data[street]["bathrooms"])
        sqfts_list.append(matching_listing_data[street]["sqft_living"])
        prices_list.append(matching_listing_data[street]["price"])


    bed_mean, bed_std = np.mean(beds_list), np.std(beds_list)
    bath_mean, bath_std = np.mean(baths_list), np.std(baths_list)
    sqft_mean, sqft_std = np.mean(sqfts_list), np.std(sqfts_list)
    price_mean, price_std = np.mean(prices_list), np.std(prices_list)


    for street in matching_listing_data:
        normalized_bed = (matching_listing_data[street]["bedrooms"] - bed_mean) / bed_std
        normalized_bath = (matching_listing_data[street]["bathrooms"] - bath_mean) / bath_std
        normalized_sqft = (matching_listing_data[street]["sqft_living"] - sqft_mean) / sqft_std
        normalized_price = (matching_listing_data[street]["price"] - price_mean) / price_std


        normalized_data[street] = {
            "bedrooms": normalized_bed,
            "bathrooms": normalized_bath,
            "sqft_living": normalized_sqft,
            "price": normalized_price
        }


    normalized_target = {
        "bedrooms": (requested_data["bedrooms"][1] - bed_mean) / bed_std,
        "bathrooms": (requested_data["bathrooms"][1] - bath_mean) / bath_std,
        "sqft_living": (requested_data["sqft"][1] - sqft_mean) / sqft_std ,
        "price": (requested_data["price"][1] - price_mean) / price_std
    }


    distances = []


    for street in normalized_data:


        distance = (
            abs(normalized_data[street]["bedrooms"] - normalized_target["bedrooms"]) +
            abs(normalized_data[street]["bathrooms"] - normalized_target["bathrooms"]) +
            abs(normalized_data[street]["sqft_living"] - normalized_target["sqft_living"]) +
            abs(normalized_data[street]["price"] - normalized_target["price"])
        )


        distances.append((street, distance))


    distances.sort(key=lambda x: x[1])
    top_5 = distances[:5]


    for street, dist in top_5:
        top_5_listings[street] = matching_listing_data[street]

    if top_5_listings == {}:
        print("No listings found that match your criteria.")
        
    
    return top_5_listings


user_data = get_user_input(state_zip_data)


print(user_data)

