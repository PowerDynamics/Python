from matplotlib import ticker
import pandas as pd
import matplotlib.pyplot as plt


'''
Interest rate data
https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp

'''

#Load the interest data
df_rateHistory = pd.read_csv('\\Python\\pandas\\data\\Bank Rate history and data Bank of England Database.csv')

#Add a new Year column
df_rateHistory['Year'] = pd.to_datetime(df_rateHistory['Date Changed']).dt.year.astype(str)

#Get average year rate changes
df_yearRate = df_rateHistory.groupby(['Year'])['Rate'].mean().reset_index(name='Interest_Rate')

print(df_yearRate)



'''
House pricing data
http://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/Annual-price-change-by-country-2021-05.csv

'''


#Load the house price data
df_housePrice = pd.read_csv('\\Python\\pandas\\data\\ukhpi-property-type-pac-united-kingdom-from-2000-06-01-to-2021-06-01.csv')

#Add a new Year column
df_housePrice['Year'] = pd.to_datetime(df_housePrice['Period']).dt.year.astype(str)

#Get annual price changes
df_yearPrice = df_housePrice.groupby(['Year'])['Percentage change (yearly) All property types'].mean().reset_index(name='Price_Change')

print(df_yearPrice)




'''
Data merge/lookup

'''

#Merge two dataframes by Year
merged_df = pd.merge(df_yearRate, df_yearPrice, 
                     left_on = 'Year', 
                     right_on = 'Year', 
                     how='right')

print(merged_df)

#Fill the NaN interest rate with previous Year rate
filled_df = merged_df.fillna(method='ffill')
print(filled_df)
#filled_df.plot(x ='Year', y='Rate', kind = 'line')	

ax = plt.gca()
filled_df.plot(kind='line',x='Year',y='Price_Change',ax=ax)
filled_df.plot(kind='bar',x='Year',y='Interest_Rate', color='red', ax=ax)

#add axis labels and a title
plt.ylabel('Interest Rate vs House Price Changes', fontsize=10)
plt.xlabel('Year', fontsize=10)
plt.title('Interest Rate vs House Price Changes - 2000 to 2021', fontsize=12)

plt.show()