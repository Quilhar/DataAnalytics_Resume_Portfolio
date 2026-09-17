import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main_stats(dataset):
    '''
    Function to calculate main statistics of a dataset:
    - dataset (list or array): A list or array of numerical values
    - Returns a dictionary with mean, median, variance, std_dev, max, min
    '''
    
    data = dataset
    
    # Finding the values of the statistics
    mean = np.mean(data)
    median = np.median(data)
    variance = np.var(data)
    std_dev = np.std(data)
    max = np.max(data)
    min = np.min(data)
    
    # Converting numpy types to python types
    mean = float(mean)
    median = float(median)
    variance = float(variance)
    std_dev = float(std_dev)
    max = float(max)
    min = float(min)
    
    # Rounding to 2 decimal places
    mean = round(mean, 2)
    median = round(median, 2)
    variance = round(variance, 2)
    std_dev = round(std_dev, 2)
    max = round(max, 2)
    min = round(min, 2)
    
    # Creating a dictionary to store the results
    data_summary = {"mean": mean, "median": median, "variance": variance, "std_dev": std_dev, "max": max, "min": min}

    return data_summary

def quartiles(dataset):
    '''
    Function to calculate quartiles of a dataset:
    - dataset (list or array): A list or array of numerical values
    - Returns a dictionary with Q1, Q2 (median), and Q3
    '''
    data = dataset
    
    # Finding the quartiles
    Q1 = np.percentile(data, 25)
    Q2 = np.percentile(data, 50)
    Q3 = np.percentile(data, 75)
    
    # Converting numpy types to python types
    Q1 = float(Q1)
    Q2 = float(Q2)
    Q3 = float(Q3)
    
    # Rounding to 2 decimal places
    Q1 = round(Q1, 2)
    Q2 = round(Q2, 2)
    Q3 = round(Q3, 2)
    
    # Creating a dictionary to store the results
    quartile_summary = {"Q1": Q1, "Q2": Q2, "Q3": Q3}
    
    return quartile_summary

def regular_plot(dataset, xaxis_label = '', yaxis_label = '', title = '', color = ''):
    '''
    Function to create a regular plot of a dataset:
    - dataset (list or array): A list or array of numerical values
    - xaxis_label (str): Label for the x-axis
    - yaxis_label (str): Label for the y-axis
    - title (str): Title of the plot
    - color (str): Color of the line
    '''
    
    data = dataset
    
    # Creating regular plot
    plt.plot(data, color, linestyle='-', marker='o')
    plt.xlabel(xaxis_label)
    plt.ylabel(yaxis_label)
    plt.title(title)
    
    plt.tight_layout()

def histogram(dataset, xaxis_label = 'x_axis', yaxis_label = 'y_axis', title = 'histogram', color = 'blue', edgecolor = 'black'):
    '''
    Function to create a histogram of a dataset:
    - dataset (list or array): A list or array of numerical values
    - xaxis_label (str): Label for the x-axis
    - yaxis_label (str): Label for the y-axis
    - title (str): Title of the histogram
    - color (str): Color of the bars
    - edgecolor (str): Color of the edges of the bars
    '''
    
    data = dataset
    
    # Creating histogram
    
    # Use numpy to calculate the edges of the bins, using the 'auto' method, which calculates the optimal number of bins based on using the Freedman-Diaconis, and Sturges methods
    bins_edges_auto = np.histogram_bin_edges(data, bins='auto')
    
    plt.hist(data, bins=bins_edges_auto, edgecolor = edgecolor, color = color)
    plt.xlabel(xaxis_label)
    plt.ylabel(yaxis_label)
    plt.title(title)
    
    plt.tight_layout()
    
def piechart(dataset, labels, title = '', colors = '', explode = '', startangle = '', autopct = 'autopct'):
    '''
    Function to create a pie chart of a dataset:
    - dataset (list or array): A list or array of numerical values
    - labels (list): A list of labels for each slice
    - title (str): Title of the pie chart
    - colors (list): A list of colors for each slice
    - explode (list): A list of values to offset each slice
    - startangle (int): Starting angle of the pie chart
    - autopct (str): Format string for the percentage labels
    '''
    data = dataset
    
    # Creating pie chart
    plt.pie(data, labels=labels, colors=colors, explode=explode, startangle=startangle, autopct=autopct)
    plt.title(title)
    
    plt.tight_layout()

def boxplot(dataset, xaxis_label = '', yaxis_label = '', title = '', vert = True, color = 'white'):
    '''
    Function to create a box plot of a dataset:
    - dataset (list or array): A list or array of numerical values
    - xaxis_label (str): Label for the x-axis
    - yaxis_label (str): Label for the y-axis
    - title (str): Title of the box plot
    - vert (bool): Orientation of the box plot (True for vertical, False for horizontal)
    - color (str): Color of the box
    '''
    data = dataset
    
    # Creating box plot
    plt.boxplot(data, vert = vert, patch_artist = True, boxprops = dict(facecolor = color))
    plt.ylabel(yaxis_label)
    plt.xlabel(xaxis_label)
    plt.title(title)
    
    plt.tight_layout()

def plot_weighted_moving_average_data(x_data, y_data, weight_list, x_label, y_label, title, color = 'blue', filtered_color = 'red'):
    
    x = x_data
    y = y_data
    
    filtered_x, filtered_y = weighted_moving_average_filter_for_graphs(x_data, y_data, weight_list)
    
    plt.plot(x, y, color = color, label = 'Raw Data')
    
    plt.plot(filtered_x, filtered_y, color = filtered_color, label = 'Weighted Moving Average Filtered Data')
    
    plt.xlabel(x_label)
    
    plt.ylabel(y_label)
    
    plt.title(title)
    
    plt.legend()
    
    plt.tight_layout()
    
def xy_plot(x_data, y_data, xaxis_label = '', yaxis_label = '', title = '', color = '', marker = 'o'):
    '''
    Function to create an XY plot of two datasets:
    - x_data (list or array): A list or array of numerical values for the x-axis
    - y_data (list or array): A list or array of numerical values for the y-axis
    - xaxis_label (str): Label for the x-axis
    - yaxis_label (str): Label for the y-axis
    - title (str): Title of the plot
    - color (str): Color of the points
    '''
    
    x = x_data
    y = y_data
    
    # Creating XY plot
    plt.plot(x, y, color=color, marker=marker)
    plt.xlabel(xaxis_label)
    plt.ylabel(yaxis_label)
    plt.title(title)
    
    plt.tight_layout()
############################################################################################## Lecture 3 Functions ###########################################################################################

def find_data_correlation(x_list, y_list):
    ''' Function to find correlation coefficient between two lists of data points
    Parameters
        x_list : list
            List of data points for X
        y_list : list
            List of data points for Y
    Returns
        corelation_coefficient : float'''
    
    n = len(x_list)
    x_array = np.array(x_list)
    y_array = np.array(y_list)
    
    sum_x = sum(x_list)
    sum_y = sum(y_list)
    sum_xy = np.sum(x_array * y_array)
    sum_x_squared = sum(x ** 2 for x in x_list)
    sum_y_squared = sum(y ** 2 for y in y_list)

    numerator = (n * sum_xy) - (sum_x * sum_y)
    denominator = ((np.sqrt((n * sum_x_squared) - sum_x ** 2)) * (np.sqrt((n * sum_y_squared) - sum_y ** 2)))
    
    corelation_coefficient = numerator / denominator
            
    return corelation_coefficient
    
def least_squares_matrixes(x_data, y_data, fit = 1):
    ''' Function to find the least squares matrix
        x_data : list
            List of data points for X
        y_data : list
            List of data points for Y
        Returns :
            least_squares_matrix_left : matrix
                Left hand side least squares matrix
            least_squares_matrix_right : matrix
                Right hand side least squares matrix '''
        
    # print(x_data)
    n = len(x_data)
    
    if fit == 1:
        x_array = np.array(x_data)
        y_array = np.array(y_data)
      
        a = sum(x_array ** 2)
        b = sum(x_array)
        c = b
        d = n
        e = sum(x_array * y_array)
        f = sum(y_array)
        
        least_squares_matrix_left = [[a, b], [c, d]]
        least_squares_matrix_right = [[e], [f]]
        
    if fit == 2:
        x_array = np.array(x_data)
        y_array = np.array(y_data)
        
        a = sum(x_array ** 4)
        b = sum(x_array ** 3)
        c = sum(x_array ** 2)
        d = sum(x_array)
        e = n
        
        f = sum((x_array ** 2) * y_array)
        g = sum(x_array * y_array)
        h = sum(y_array)
        
        least_squares_matrix_left = [[a, b, c], [b, c, d], [c, d, e]]
        least_squares_matrix_right = [[f], [g], [h]]
    
    return least_squares_matrix_left, least_squares_matrix_right

def matrix_inverse(A, ifit = 1):
    ''' Function computes the inverse matrix for either the 2X2 linear least squares matrix
    or the 3X3 quadratic least square fit, depending on the value of ifit
    
    Inputs :
        A - The least squares matrix to be inverted input as a 2 dimensional Python list
        ifit - the degree of the polynomial to be fitted (either 1 or 2)
        
    Outputs :
        A_inv - The inverse of the least squares matrix output as a 2
        dimensional Python list'''
    
    if ifit == 1:
        a_matrix = A
        
        a1 = a_matrix[0][0]
        b1 = a_matrix[0][1]
        c1 = a_matrix[1][0]
        d1 = a_matrix[1][1]
        
        det = (a1 * d1) - (b1 * c1)
        
        a2 = a_matrix[1][1]/det
        b2= -a_matrix[0][1]/det
        c2 = -a_matrix[1][0]/det
        d2 = a_matrix[0][0]/det
        
        a_inverse = [[a2, b2],
                    [c2, d2]]
        
    if ifit == 2:
        a_matrix = A
        
        a1 = a_matrix[0][0]
        b1 = a_matrix[0][1]
        c1 = a_matrix[0][2]
        d1 = a_matrix[1][0]
        e1 = a_matrix[1][1]
        f1 = a_matrix[1][2]
        g1 = a_matrix[2][0]
        h1 = a_matrix[2][1]
        i1 = a_matrix[2][2]
        
        det = (a1 * (e1 * i1 - f1 * h1) - b1 * (d1 * i1 - f1 * g1) + c1 * (d1 * h1 - e1 * g1))
        
        a2 = (e1 * i1 - f1 * h1)/det
        b2 = (c1 * h1 - b1 * i1)/det
        c2 = (b1 * f1 - c1 * e1)/det
        d2 = (f1 * g1 - d1 * i1)/det
        e2 = (a1 * i1 - c1 * g1)/det
        f2 = (c1 * d1 - a1 * f1)/det
        g2 = (d1 * h1 - e1 * g1)/det
        h2 = (b1 * g1 - a1 * h1)/det
        i2 = (a1 * e1 - b1 * d1)/det
        
        a_inverse = [[a2, b2, c2],
                     [d2, e2, f2],
                     [g2, h2, i2]]
        
    return a_inverse

def least_squares_coefficient(x_list, y_list, ifit = 1):
    ''' Function to find least squares coefficients for linear fit
        A : matrix
            Left hand side least squares matrix
        B : matrix
            Right hand side least squares matrix '''

    ifit = ifit
    
    A, B = least_squares_matrixes(x_list, y_list, fit=ifit)
    
    A = matrix_inverse(A, ifit)
    

    if ifit == 1:
        a = A[0][0] * B[0][0] + A[0][1] * B[1][0] 
        b = A[1][0] * B[0][0] + A[1][1] * B[1][0] 
        
        least_squares_coefficients = [[a, b]]
        
    if ifit == 2 :
        a = A[0][0] * B[0][0] + A[0][1] * B[1][0] + A[0][2] * B[2][0]
        b = A[1][0] * B[0][0] + A[1][1] * B[1][0] + A[1][2] * B[2][0]
        c = A[2][0] * B[0][0] + A[2][1] * B[1][0] + A[2][2] * B[2][0]
        least_squares_coefficients = [[a, b, c]]
    
    return least_squares_coefficients

def graph__least_squares(x_data, y_data, x_axis = '', y_axis = '', title = '', fit = 1):
    ''' Function to graph least squares fit along with data points
        x_data : list
            List of data points for X
        y_data : list
            List of data points for Y
        x_axis : str
            Label for x axis
        y_axis : str
            Label for y axis
        title : str
            Title for the graph
        fit : int
            Degree of polynomial fit (1 for linear, 2 for quadratic)'''
    
    coefficients = least_squares_coefficient(x_data, y_data, ifit = fit)
    
    plt.scatter(x_data, y_data, color='blue', label='Data Points')
    
    a = coefficients[0][0]
    b = coefficients[0][1]
    
    
    if fit == 1:

        x_fit = np.linspace(min(x_data), max(x_data), 100)
        y_fit = a * x_fit + b
        plt.plot(x_fit, y_fit, color='green', label='Least Squares Fit')
        
    if fit == 2:
        
        c = coefficients[0][2]
        
        x_fit = np.linspace(min(x_data), max(x_data), 100)
        
        y_fit = a * x_fit ** 2 + b * x_fit + c
        plt.plot(x_fit, y_fit, color='green', label='Least Squares Fit')

    
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(title)
    plt.legend()
    


def calculate_residuals(x_data, y_data, ifit = 1):
    
    x_array = np.array(x_data)
    y_array = np.array(y_data)
    
    least_square_line_y_values = []
    
    fit_residual = []
    
    if ifit == 1:
        least_squares_coefficients = least_squares_coefficient(x_array, y_array)
        
        for x in x_array:
            least_square_line_y_values.append((least_squares_coefficients[0][0] * x) + least_squares_coefficients[0][1])
        
        for y in y_array:
            fit_residual.append(y - least_square_line_y_values[len(fit_residual)])
    
        residual_mean = np.mean(fit_residual)
        residual_std = np.std(fit_residual)
        
    if ifit == 2:
        least_squares_coefficients = least_squares_coefficient(x_array, y_array, ifit = 2)
        
        for x in x_array:
            least_square_line_y_values.append((least_squares_coefficients[0][0] * (x ** 2)) + (least_squares_coefficients[0][1] * x) + least_squares_coefficients[0][2])
        
        for y in y_array:
            fit_residual.append(y - least_square_line_y_values[len(fit_residual)])
    
        residual_mean = np.mean(fit_residual)
        residual_std = np.std(fit_residual)
        
    return fit_residual, residual_mean, residual_std

def determine_outliers(residuals, mean, std_dev, n = 2):
    outlier_indices = []
    bound1 = mean + n * std_dev
    bound2 = mean - n * std_dev
    
    for i in range(len(residuals)):
        if residuals[i] > bound1 or residuals[i] < bound2:
            outlier_indices.append(i)
    
    return outlier_indices 

def remove_outliers(x_data, y_data, outlier_indices):
    x_cleaned = []
    y_cleaned = []
    
    for i in range(len(x_data)):
        if i not in outlier_indices:
            x_cleaned.append(x_data[i])
            y_cleaned.append(y_data[i])
        
    
    return x_cleaned, y_cleaned

def error_bar_bounds(x_data, y_data, fit = 1):
    x = x_data
    y = y_data
    
    residuals, residual_mean, residual_std_dev = calculate_residuals(x, y, ifit = fit)
    correlation_coefficients = least_squares_coefficient(x, y, ifit = fit)
    
    upper_boundx = []
    upper_boundy = []

    lower_boundx = []
    lower_boundy = []
    
    if fit == 1:
        
        upper_boundx.append(np.min(x))
        upper_boundx.append(np.max(x))

        lower_boundx.append(np.min(x))
        lower_boundx.append(np.max(x))

        y_upper_min = (correlation_coefficients[0][0]*np.min(x)) + (correlation_coefficients[0][1] - (residual_mean - 2 * residual_std_dev))
        y_upper_max = (correlation_coefficients[0][0]*np.max(x)) + (correlation_coefficients[0][1] + (residual_mean + 2 * residual_std_dev))

        upper_boundy.append(y_upper_min)
        upper_boundy.append(y_upper_max)

        y_lower_min = (correlation_coefficients[0][0]*np.min(x)) + (correlation_coefficients[0][1] - (residual_mean + 2 * residual_std_dev))
        y_lower_max = (correlation_coefficients[0][0]*np.max(x)) + (correlation_coefficients[0][1] + (residual_mean - 2 * residual_std_dev))

        lower_boundy.append(y_lower_min)
        lower_boundy.append(y_lower_max)
        
    if fit == 2:
        
        for i in range(len(x)):
            upper_boundx.append(x[i])
            lower_boundx.append(x[i])
            
            y_upper = (correlation_coefficients[0][0] * (x[i] ** 2)) + (correlation_coefficients[0][1] * x[i]) + correlation_coefficients[0][2] + (residual_mean + 2 * residual_std_dev)
            y_lower = (correlation_coefficients[0][0] * (x[i] ** 2)) + (correlation_coefficients[0][1] * x[i]) + correlation_coefficients[0][2] - (residual_mean + 2 * residual_std_dev)
            
            upper_boundy.append(y_upper)
            lower_boundy.append(y_lower)
            
    return upper_boundy, upper_boundx, lower_boundx, lower_boundy

def graphing_error_bars(x_data, y_data, fit = 1, xlabel = 'X values', ylabel = 'Y values', title = 'Error Bounds for Least Squares Fit'):
    upper_boundy, upper_boundx, lower_boundx, lower_boundy = error_bar_bounds(x_data, y_data, fit)
        
    plt.plot(upper_boundx, upper_boundy, color='red', linestyle='--', label='Upper Bound')
    plt.plot(lower_boundx, lower_boundy, color='red', linestyle='--', label='Lower Bound')
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()

def RMSE(x_data, y_data):
    n = len(x_data)
    
    fit_residual, residual_mean, residual_std = calculate_residuals(x_data, y_data)
    
    sum_squared_errors = 0.0
    for residual in fit_residual:
        sum_squared_errors += residual ** 2
        
    rmse = np.sqrt(sum_squared_errors / n)
    
    return rmse

def gaussian_prob(x, mean, std_dev):
    '''x : value to evaluate the probability at
       mean : mean of the distribution
       std_dev : standard deviation of the distribution
    '''
    
    coeff = 1 / (std_dev * np.sqrt(2 * np.pi))
    exponent = np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
    
    gaussian_probability = coeff * exponent
    
    return gaussian_probability


#########################################################################

def weighted_moving_average_filter(data_set, weight_list):
    x = data_set
    n = len(weight_list)
    filter_length = n
    
    filtered_data = []
    
    weight_sum = sum(weight_list)
    
    for i in range(len(data_set) - filter_length + 1):
        
        numerator = 0
        
        for a in range(filter_length):
            
            numerator += data_set[i + a] * weight_list[a]
            
        filtered_value = numerator / weight_sum
        filtered_data.append(filtered_value)
            
    return filtered_data

def weighted_moving_average_filter_for_graphs(x_data, y_data, weight_list):
    x = x_data
    y = y_data
    n = len(weight_list)
    filter_length = n
    
    filtered_data_x = []
    filtered_data_y = []
    
    weight_sum = sum(weight_list)
    
    for i in range(len(x) - filter_length + 1):
        
        numerator_x = 0
        
        for a in range(filter_length):
            
            numerator_x += x_data[i + a] * weight_list[a]
            
        filtered_value_x = numerator_x / weight_sum
        filtered_data_x.append(filtered_value_x)
        
    for i in range(len(y) - filter_length + 1):
        
        numerator_y = 0
        
        for b in range(filter_length):
            
            numerator_y += y_data[i + b] * weight_list[b]
            
        filtered_value_y = numerator_y / weight_sum
        filtered_data_y.append(filtered_value_y)
            
    return filtered_data_x, filtered_data_y

def fading_moving_average_filter(data_set, weight_list):
    x = data_set
    n = len(weight_list)
    
    filtered_data = []
    
    for i in range(len(data_set) - n + 1):
        
        if i == 0:
            filtered_data.append(x[i])
        
        filtered_data.append((weight_list[0] * x[i + n - 1] + (weight_list[1] * filtered_data[i])))
        
    return filtered_data

#########################################################################

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

def normalize(data):
    data = np.array(data)
    normalized_data = []
    
    for i in range(len(data)):
        normalized_value = (data[i] - np.mean(data)) / np.std(data)
        normalized_data.append(normalized_value)
        
    return normalized_data