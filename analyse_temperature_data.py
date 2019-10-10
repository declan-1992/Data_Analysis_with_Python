import numpy as np

temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')   # use number to import data from CSV file

temperatures_fixed = temperatures + 3     # adjust all temperatures in numpy array by 3

monday_temperatures = temperatures_fixed[0,:]    #obtain temperatures for monday

thursday_friday_morning = temperatures_fixed[3:5,1]    #obtain temperatures for Thursday and Friday morning

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]   #Select all temperatures that are below 50 OR above 60 
