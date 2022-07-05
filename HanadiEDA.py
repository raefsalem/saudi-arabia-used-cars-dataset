#%%
from enum import unique
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy import rotations
import scipy.stats as ss

#%%
cars = pd.read_csv('../saudi-arabia-used-cars-dataset/UsedCarsSA_Clean_EN.csv')

#%%
# Drop duplicate rows
cars.drop_duplicates(inplace=True)
#%%
# Dropping the rows having price equal to zero
cars = cars[cars['Price'] != 0]

#%%
#set a lower range for the price
cars = cars[cars['Price'] > 7000]

#%% 
####First plot (Color bar chart)
fig = plt.figure(figsize=(10,5))
cars.Color.value_counts().plot(kind='bar', rot=90, color='#FF96C5')
plt.title('Cars Color Distrobution')
plt.xlabel('Color')
plt.ylabel('Cars')
###Insight: White, black & silver are the most common colors whereas green, orange & yellow are the least frequent.
#%%
###Second plot (Price Histogram)
plt.figure(figsize=(10,5))
np.random.seed(6789)
x = cars['Price']
result = plt.hist(x, bins=150, color='c', edgecolor='k', alpha=0.65)
plt.axvline(x.median(), color='k', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(x.median()*1.1, max_ylim*0.9, 'Median: {:.2f}'.format(x.median()))
plt.title('Cars Price Distrobution')
plt.xlabel('Price (Million SAR)')
plt.ylabel('Cars')
#insight: price was positively skewed that's why we showed the median.
#%%
### Third plot (Company & Year Vs Price)
##cmap=plt.cm.get_cmap("cool_r", 12)
y = cars['Price']
x = cars['Make']
colors = cars['Year']
plt.figure(figsize=(18,5))
plt.scatter(x,y, s=10, c=colors, alpha=0.7)
plt.colorbar(orientation="vertical", label="Year")
plt.title('Price in each company & year')
plt.xlabel('Company Name')
plt.ylabel('Price (Million SAR)')
plt.xticks(rotation=90)
###Insight: 
##This plot shows the price according to each company & year, Marcedes has the heighest price followed by Bentley & Rolls-Royce.
##not surprisingly, most price increase as the car's year increase (The newer the car, the heigher the price).
#%%


# %%
