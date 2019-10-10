import numpy as np

rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11])

rain_mean = np.mean(rainfall)   #mean

rain_median = np.median(rainfall)   #median

first_quarter = np.percentile(rainfall, 25)    #lower quartile

third_quarter = np.percentile(rainfall, 75)    #upper quartile

interquartile_range = third_quarter - first_quarter     #interquartile range

rain_std = np.std(rainfall)    #standard deviation 
