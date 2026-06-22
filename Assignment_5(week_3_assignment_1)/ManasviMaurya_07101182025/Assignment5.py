#Dataset= agriculture_yield_dataset.csv
#Q1. Dataset Overview 
# How many rows and columns are present?  
import pandas as pd
data = pd.read_csv('agriculture_yield_dataset.csv')
print("Number of rows and columns:", data.shape)

# What are the names of all columns?  
print("Column names:", data.columns.tolist())

# Display the first 10 records. 
print("First 10 records:")
print(data.head(10))

# Q2. Data Types and Missing Values 
'''Check the data type of each column.  
Identify whether any missing values are present.  
If missing values exist, mention the affected columns. '''

print(data.dtypes)
print(data.isnull().sum())

#Q3. Descriptive Statistics 
'''Which feature has the highest mean value?  
Which feature has the highest standard deviation? '''
print(data.describe())

#Q4. Distribution Analysis 
'''Create histograms for: 
rainfall_mm  
temperature_c  
fertilizer_kg  
yield_ton_per_hectare '''
import matplotlib.pyplot as plt
data[['rainfall_mm', 'temperature_c', 'fertilizer_kg', 'yield_ton_per_hectare']].hist(bins=15, figsize=(10, 8))
plt.show()

'''Q5. Crop Type Analysis 
Find the number of records for each crop type.  
Create a count plot (bar chart) for crop_type.  
Which crop appears most frequently? '''

import seaborn as sns
print(data['crop_type'].value_counts())
sns.countplot(data=data, x='crop_type')
plt.show()

#Q6. Soil Type Analysis
'''Find the frequency of each soil type.  
Create a count plot for soil_type.  
Which soil type is most common? '''
print(data['soil_type'].value_counts())
sns.countplot(data=data, x='soil_type')
plt.show()

#Q7. Yield Distribution 
#Create a histogram of yield_ton_per_hectare.
sns.histplot(data=data, x='yield_ton_per_hectare', kde=True)
plt.show()

#Q8. Scatter Plot Analysis 
'''Create scatter plots of: 
1. rainfall_mm vs yield_ton_per_hectare  
2. fertilizer_kg vs yield_ton_per_hectare'''
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.scatterplot(data=data, x='rainfall_mm', y='yield_ton_per_hectare', ax=axes[0])
sns.scatterplot(data=data, x='fertilizer_kg', y='yield_ton_per_hectare', ax=axes[1])
plt.show()

'''Q9. Correlation Analysis 
Generate a correlation matrix for numerical features.  
Create a heatmap.  
Identify the top three features most correlated with crop yield.'''
# Select only numerical columns for correlation
numerical_df = data.select_dtypes(include=['float64', 'int64'])
corr_matrix = numerical_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()
print(corr_matrix['yield_ton_per_hectare'].sort_values(ascending=False))

#Q10. Group-Based Analysis 
'''Calculate the average yield for: 
Each crop type  
Each soil type  '''
print("By Crop:\n", data.groupby('crop_type')['yield_ton_per_hectare'].mean().sort_values(ascending=False))
print("\nBy Soil:\n", data.groupby('soil_type')['yield_ton_per_hectare'].mean().sort_values(ascending=False))

'''Q11. Feature Encoding 
Identify the categorical columns.  
Convert them into numerical form using One-Hot Encoding.  
Display the first five rows of the transformed dataset. '''
df_encoded = pd.get_dummies(data, columns=['crop_type', 'soil_type'], drop_first=True)
print(df_encoded.head())

#Q12. Feature Selection 
'''Separate: 
Input features (X)  
Target variable (y)  
Specify which column is being used as the target variable. '''
X = df_encoded.drop('yield_ton_per_hectare', axis=1)
y = df_encoded['yield_ton_per_hectare']

'''Q13. Train-Test Split 
Split the dataset into: 
80% Training Data  
20% Testing Data  
-Display the shape of: 
X_train  
X_test  
y_train  
y_test '''
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")

'''Q14. Linear Regression Model 
Train a Linear Regression model.  
Display the model coefficients and intercept.  
Which feature has the highest positive coefficient?'''
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Intercept: {model.intercept_}")
coefficients = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_})
print(coefficients.sort_values(by='Coefficient', ascending=False))
