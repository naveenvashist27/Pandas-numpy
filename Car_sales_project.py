# 🔁 Importing Required Libraries
from multiprocessing.reduction import duplicate  # Unused here; can be removed
import numpy as np                   # 🔵 NumPy
import pandas as pd                 # 🟡 Pandas
import matplotlib.pyplot as plt     # 🔴 Matplotlib

# 🟡 Step 1: Load the CSV file
data = pd.read_csv(r"C:\Users\visha\OneDrive\Desktop\Car Sell Dataset.csv")

# 🟡 Step 2: Create DataFrame
df = pd.DataFrame(data)

# 🟡 Step 3: Basic Inspection
# print(df.head(5))               # View top 5 rows
# print(df.columns)               # List of column names
# print(df.dtypes)                # Data types of each column
# print(df.isnull().sum())        # Count of missing/null values

# 🟡 Step 4: Drop rows with null values (not updating DataFrame unless assigned back)
df.dropna(inplace=True)

# # 🟡 Step 5: Check and Remove Duplicate Rows
# print("Number of duplicate rows:", df.duplicated().sum())  # How many duplicates?
# df.drop_duplicates(inplace=True)  # Remove duplicates


# 🟡 Step 6: Unique values in categorical columns
# print(df['Fuel Type'].unique())
# print(df['State'].unique())
# print(df['Owner'].unique())

# 🟡 Step 7: Fuel Type Analysis
# print(df['Fuel Type'].value_counts())  # How many of each fuel type?
# print(df['State'].value_counts())  # How many of each state type?
# print(df['Owner'].value_counts())  # How many of each owner type?

# most common fuel type
most_common_fuel = df['Fuel Type'].value_counts().idxmax()
print("Most used fuel type:", most_common_fuel)

# most fuel value
count = df['Fuel Type'].value_counts().max()
print("Used in", count, "cars")

# What is the most common car model or variant?
most_common_car = df['Model Name'].value_counts().idxmax()
most_common_model_number = df['Model Name'].value_counts().max()
print("Most used car modal numbers",most_common_car)
print("Most used car modal numbers",most_common_model_number)

# 🟡 Step 8: Mean Price of All and Diesel Cars Only
print("Overall Average Price:", df['Price'].mean())
print("Average Price of Diesel Cars:", df[df['Fuel Type'] == 'Diesel']['Price'].mean())
print("Average Price of CNG Cars:", df[df['Fuel Type'] == 'CNG']['Price'].mean())
print(df.groupby('Transmission')['Price'].mean())
 # What is the maximum price for each car brand?
print(df.groupby('Car Type')['Price'].mean())

 # Are there any rows with missing values in Price, Fuel Type, or Model Name
print('null values of price',df['Price'].isnull().sum())
print('null values of fuel type',df['Fuel Type'].isnull().sum())
print('null values of model name',df['Model Name'].isnull().sum())

#  Are there any cars with 0 Kilometers driven or price?
print('model variant where kilometer driven is zero',df[df['Kilometers']==0]['Model Variant'])
print(df[df['Kilometers'] == 0])


#   Remove rows where Price < 10,000 (likely invalid entries).
df = df[df['Price']>=10000]
print(df.head(5))

# to see invalid entries below 100000
# print(df[df['Price']<100000])

# as  Which car is the newest? Oldest?
import datetime
current_year = datetime.datetime.now().year
df['Car_Age'] = current_year - df['Year']  # New column based on current year
print('maximum age of car is ',df['Car_Age'].max())
print('minimum age of car is ',df['Car_Age'].min())

# qu Average price by Brand
print('group by cars & average of price ',df.groupby('Brand')['Price'].mean())
print('count of cars ,group by owner ',df['Owner'].value_counts())

# q How many cars are marked as Accidental = Yes?
print('cars accidental\n',df[df['Accidental'] == 'Yes']['Model Variant'])
print("Total accidental cars:\n", (df['Accidental'] == 'Yes').sum())


# que 6.2 What is the average price of accidental vs non-accidental cars?
print("Total accidental cars price average:\n", df[df['Accidental'] == 'Yes']['Price'].mean())
print("Total non accidental cars price average:\n", df[df['Accidental'] == 'No']['Price'].mean())
# other way
print("Average price of accidental vs non-accidental cars:\n")
print(df.groupby('Accidental')['Price'].mean())


print(df.groupby('Owner')['Kilometers'].mean())


print('diesel cars cost more than 5 lakh \n',df[(df['Fuel Type'] == 'Diesel') & (df['Price'] > 500000)])

# qu 7.2 Show all Automatic cars from year 2020 and above
print('automatic car year >2020\n',df[(df['Transmission'] == 'Automatic') & (df['Year']>2020 )])


# print(df[df['State'] == 'Delhi'].sort_values(by='Price' , ascending=False).head(10))
delhi_top10 = df[df['State'] == 'Delhi'].sort_values(by='Price' , ascending=False).head(10)
print(delhi_top10[['Brand', 'Model Name', 'Price', 'Fuel Type', 'Year']])


# If you want just the count of accidental cars:
# print("Total accidental cars:", (df['Accidental'] == 'Yes').sum())



# 🔵 NumPy Section: Car Age Calculation
# import datetime
# current_year = datetime.datetime.now().year
# df['Car_Age'] = current_year - df['Year']  # New column based on current year
# print(df['Car_Age'])
# print(df.head(5))  #car age column is clearly visible now

# argmax() → NumPy → gives positional index (can be risky if DataFrame is filtered or has non-default indexing).
# idxmax() → Pandas → gives actual index label where max occurs (recommended).

# But this approach works only if DataFrame index is default (0,1,2,...), which might not always be the case.
# df.iloc[df['Price'].values.argmax()]

# print("Row with highest price:\n", df.loc[df['Price'].idxmax()])
# max_index = df['Price'].idxmax()         # Returns the index label of max price
# print("Row with highest price:\n", df.loc[max_index])
# print("Maximum price is:", df['Price'].max())
# max_index = df['Price'].idxmax()
# print("Brand of the most expensive car:", df.loc[max_index, 'Brand'])
# print("Price of the most expensive car:", df.loc[max_index, 'Price'])


# Optional: Remove duplicates based on Car_Age and Year (now possible as we made car age column)
# df.drop_duplicates(subset=['Car_Age', 'Year'], inplace=True)

# 🔴 Matplotlib Section: Bar Chart – Cars Sold by Fuel Type
# df['Fuel Type'] = df['Fuel Type'].astype(str).str.strip().str.title()
# fuel_counts = df['Fuel Type'].value_counts()
# fuel_counts.plot(kind='bar', color='green', figsize=(8, 5))
# plt.xlabel('Fuel Type')
# plt.ylabel('Number of Cars Sold')
# plt.title('Number of Cars Sold by Fuel Type')
# plt.xticks(rotation=45)
# plt.show()


# 🔴 Optional: Horizontal bar example (commented)
# plt.barh(product, sales, color='orange', label='sales 2025')

# 🔴 Matplotlib Line Plot: Year vs Price (All data)
# plt.plot(df['Year'], df['Price'])
# plt.xlabel('Year')
# plt.ylabel('Price')
# plt.title('Price vs Year')
# plt.show()

# 🔴 Matplotlib Scatter Plot (Filtered for years 2020–2023)
# filtered_df = df[(df['Year'] >= 2020) & (df['Year'] <= 2023)]
#
# plt.figure(figsize=(10,6))
# plt.xlim(540000, 640000)    # X-axis range for price
# plt.ylim(2020, 2023)        # Y-axis range for year
# plt.scatter(filtered_df['Price'], filtered_df['Year'], color='blue')
# plt.xlabel('Price')
# plt.ylabel('Year')
# plt.title('Car Prices (2020–2023)')
# plt.grid(True)
# plt.show()
