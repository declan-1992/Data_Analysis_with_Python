import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('AAPL_data.csv')  ## import apple stock imformation
print(df.head())   ## check the table information

df['Daily Log Rate of Return'] = np.log(df['Adj Close']/df['Adj Close'].shift(1))   ##calculate the daily lograte of retunr

print(df['Daily Log Rate of Return'])

stdev = np.std(df['Daily Log Rate of Return'])    ##calculate the standard deviation
print(stdev)

plt.hist(df['Daily Log Rate of Return'].dropna())   ##analyse the data using a histogram
plt.title('Histogram of AAPL Daily Log Rates of Return')
plt.xlabel('Log Rate of Return')
plt.ylabel('Number of Days')
plt.show()
