"""
Driver Behavior Clustering

Portfolio version of a data-analysis project originally developed as coursework.

Research question:
Can unsupervised learning reveal distinct groups of driving behavior from measured driving features?

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


# Exercise 1

# Write a Python function to read in the data. The data file is named drivingclusteringdata.txt. Plot the raw data for the distance feature and speeding features. Make the distance feature the independent value and the speeding feature the dependent value for the plot. Write a Python function that will take as inputs the raw feature data (distance and speed) and return the normalized data for each feature. Plot the normalized data for the distance feature and speeding features. Makethe normalized distance feature the independent value and the normalized speeding feature the dependent value for the plot.

def read_data(file):
    
    driver_id = []
    driving_feature = []
    speeding_feature = []
    
    with open(file, 'r') as f:
        
        data = f.readlines()
        
        for line in data[1:]:  # Skip the header line
            line = line.strip().split()
            driver_id.append(float(line[0]))
            driving_feature.append(float(line[1]))
            speeding_feature.append(float(line[2]))

    return driver_id, driving_feature, speeding_feature

driver_id, driving_feature, speeding_feature = read_data(DATA_DIR / 'driving_clustering_data.txt')


plt.figure(figsize=(25, 20))
plt.scatter(driving_feature, speeding_feature)
plt.xlabel('Driving Feature')
plt.ylabel('Speeding Feature')
plt.title('Driver Clustering - Raw Data')
plt.tight_layout()
plt.show()


def k_means_normalize_data(feature1, feature2):
    feature1 = np.array(feature1)
    feature2 = np.array(feature2)

    normalized_feature1 = []
    normalized_feature2 = []  

    for i in range(len(feature1)):
        normalized_feature1.append((feature1[i] - np.mean(feature1)) / np.std(feature1))
    for i in range(len(feature2)):
        normalized_feature2.append((feature2[i] - np.mean(feature2)) / np.std(feature2))

    return normalized_feature1, normalized_feature2

normalized_driving_feature, normalized_speeding_feature = k_means_normalize_data(driving_feature, speeding_feature)

plt.figure(figsize=(25, 20))
plt.scatter(normalized_driving_feature, normalized_speeding_feature)
plt.xlabel('Normalized Driving Feature')
plt.ylabel('Normalized Speeding Feature')
plt.title('Driver Clustering - Normalized Data')
plt.tight_layout()
plt.show()


# Exercise 2

import numpy as np
import matplotlib.pyplot as plt


def k_means_clustering_algorithm(feature1, feature2, x_label="Feature 1", y_label="Feature 2", title="K-Means Clustering", k=3, max_iterations=20, initial_centroids=None):
    colors = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 'orange', 'purple', 'brown']

    if initial_centroids is None:
        if len(feature1) < k:
            raise ValueError("k cannot exceed the number of observations available.")
        initial_idx = np.linspace(0, len(feature1) - 1, k, dtype=int)
        centroids = [[feature1[i], feature2[i]] for i in initial_idx]
    else:
        centroids = [list(centroid) for centroid in initial_centroids]

    print(f"Running {title} with {k} clusters for up to {max_iterations} iterations.")
    print(f"Initial centroids: {centroids}")


    for iteration in range(max_iterations):
        clusters = {}

        # Assign points using INDEXES
        for j in range(len(feature1)):
            point = np.array([feature1[j], feature2[j]])

            distances = []
            for centroid in centroids:
                dist = np.linalg.norm(point - np.array(centroid))
                distances.append(dist)

            closest_idx = distances.index(min(distances))

            if closest_idx not in clusters:
                clusters[closest_idx] = []

            clusters[closest_idx].append(j)


       # Plot
        plt.figure()
        for cluster_idx in clusters:
            x_vals = [feature1[i] for i in clusters[cluster_idx]]
            y_vals = [feature2[i] for i in clusters[cluster_idx]]

            plt.scatter(x_vals, y_vals, color=colors[cluster_idx % len(colors)], label=f'Cluster {cluster_idx + 1}')

            plt.scatter(centroids[cluster_idx][0], centroids[cluster_idx][1], color='black', marker='X', s=200)

        plt.title(f"{title} - Iteration {iteration + 1}")
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()


        # Update centroids using NumPy
        for idx in clusters:
            points = np.array([[feature1[i], feature2[i]] for i in clusters[idx]])
            centroids[idx] = np.mean(points, axis=0).tolist()


        print(f"Updated centroids: {centroids}")


    return clusters


def cluster_stats(cluster_indices, cluster_num, feature1, feature2):
    points = np.array([[feature1[i], feature2[i]] for i in cluster_indices])

    stats = {
    "cluster": cluster_num,
    "size": len(cluster_indices),
    "mean": np.mean(points, axis=0),
    "median": np.median(points, axis=0),
    "std": np.std(points, axis=0),
    "min": np.min(points, axis=0),
    "max": np.max(points, axis=0)
    }

    return stats

clusters = k_means_clustering_algorithm(normalized_driving_feature, normalized_speeding_feature, "Normalized Driving Feature", "Normalized Speeding Feature")

for cluster_num in clusters:
    stats = cluster_stats(clusters[cluster_num], cluster_num, driving_feature, speeding_feature)
    print(stats)


# Project Code



def load_data(filename):

    male_income = []
    male_spending = []
    male_age = []

    female_income = []
    female_spending = []
    female_age = []

    with open(filename, 'r') as file:
        next(file) # skip header

        for line in file:
            lines = line.strip().split(',')

            gender = lines[1]
            age = int(lines[2])
            income = int(lines[3])
            spending = int(lines[4])

            if gender == "Male":
                male_income.append(income)
                male_spending.append(spending)
                male_age.append(age)
            else:
                female_income.append(income)
                female_spending.append(spending)
                female_age.append(age)

    return male_income, male_spending, male_age, female_income, female_spending, female_age

customer_data_path = DATA_DIR / 'customer_data.txt'
if customer_data_path.exists():
    male_income, male_spending, male_age, female_income, female_spending, female_age = load_data(customer_data_path)
else:
    male_income = male_spending = male_age = female_income = female_spending = female_age = []
    print("Skipping customer profile clustering because customer_data.txt is not included in this workspace.")


# Income vs Spending

if male_income and female_income:
    male_clusters_income__spending = k_means_clustering_algorithm(male_income, male_spending, "Male Income", "Male Spending", "Male Income vs Spending Score")

    for cluster_num in male_clusters_income__spending:
        stats = cluster_stats(male_clusters_income__spending[cluster_num], cluster_num, male_income, male_spending)

        print(stats)


    female_clusters_income__spending = k_means_clustering_algorithm(female_income, female_spending, "Female Income", "Female Spending", "Female Income vs Spending Score")

    for cluster_num in female_clusters_income__spending:
        stats = cluster_stats(female_clusters_income__spending[cluster_num], cluster_num, female_income, female_spending)
        print(stats)


# Age vs income

if male_income and female_income:
    male_clusters_age__income = k_means_clustering_algorithm(male_age, male_income, "Male Age", "Male Income", "Male Age vs Income")

    for cluster_num in male_clusters_age__income:
        stats = cluster_stats(male_clusters_age__income[cluster_num], cluster_num, male_age, male_income)

        print(stats)


    female_clusters_age__income = k_means_clustering_algorithm(female_age, female_income, "Female Age", "Female Income", "Female Age vs Income")

    for cluster_num in female_clusters_age__income:
        stats = cluster_stats(female_clusters_age__income[cluster_num], cluster_num, female_age, female_income)

        print(stats)


# Age Vs Spending Score

if male_income and female_income:
    male_clusters_age__spending = k_means_clustering_algorithm(male_age, male_spending, "Male Age", "Male Spending", "Male Age vs Spending Score")

    for cluster_num in male_clusters_age__spending:
        stats = cluster_stats(male_clusters_age__spending[cluster_num], cluster_num, male_age, male_spending)

        print(stats)


    female_clusters_age__spending = k_means_clustering_algorithm(female_age, female_spending, "Female Age", "Female Spending", "Female Age vs Spending Score")

    for cluster_num in female_clusters_age__spending:
        stats = cluster_stats(female_clusters_age__spending[cluster_num], cluster_num, female_age, female_spending)
        print(stats)


# Income vs Spending



    print(stats)


# Corelation Coefficients

# Male Correlations
m_age_income_cc = dal.find_data_correlation(male_age, male_income)
m_age_score_cc = dal.find_data_correlation(male_age, male_spending)
m_spending_income_cc = dal.find_data_correlation(male_income, male_spending)

# Female Correlations
f_age_income_cc = dal.find_data_correlation(female_age, female_income)
f_age_score_cc = dal.find_data_correlation(female_age, female_spending)
f_spending_income_cc = dal.find_data_correlation(female_income, female_spending)

print(f"Male Age vs Income Correlation Coefficient: {m_age_income_cc}")
print(f"Male Age vs Spending Score Correlation Coefficient: {m_age_score_cc}")
print(f"Male Income vs Spending Score Correlation Coefficient: {m_spending_income_cc}") 

print(f"Female Age vs Income Correlation Coefficient: {f_age_income_cc}")
print(f"Female Age vs Spending Score Correlation Coefficient: {f_age_score_cc}")
print(f"Female Income vs Spending Score Correlation Coefficient: {f_spending_income_cc}")

