##Q1. Dataset Overview 
#Load the dataset and answer the following:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("agriculture_yield_dataset.csv")

#How many rows and columns are present?  
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
# ouput-Rows: 1500, Columns: 8

#What are the names of all columns?  
print(df.columns)
# output- Index(['rainfall_mm', 'temperature_c', 'fertilizer_kg', 'irrigation_hours','soil_ph', 'crop_type', 'soil_type', 'yield_ton_per_hectare'],dtype='object')

#Display the first 10 records. 
print(df.head(10))


##Q2. Data Types and Missing Values 
#Check the data type of each column.  
print(df.dtypes)

#Identify whether any missing values are present.
print(df.isnull().sum()) #no missing values present

#If missing values exist, mention the affected columns. 
print(df.columns[df.isnull().any()])


##Q3. Descriptive Statistics 
#Generate summary statistics for all numerical features and answer:
print(df.describe())
 
#Which feature has the highest mean value?  
means = df.mean(numeric_only=True)
print(means.idxmax(), "=", means.max())
# output- rainfall_mm = 754.0546666666667

#Which feature has the highest standard deviation? 
stds = df.std(numeric_only=True)
print(stds.idxmax(), "=", stds.max())
# output-rainfall_mm = 255.0972161445094


##Q4. Distribution Analysis 
#Create histograms for(Write 2–3 observations from each histogram.): 
#rainfall_mm  
plt.hist(df['rainfall_mm'], bins=20)
plt.title("Rainfall Distribution")
plt.xlabel("Rainfall")
plt.ylabel("Frequency")
plt.show()
'''
Rainfall values are spread across a wide range approximately 300–1200 mm.
The distribution appears fairly uniform without strong skewness.
No significant outliers or extreme rainfall values are visible.
'''

#temperature_c 
plt.hist(df['temperature_c'], bins=20)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()
'''
Temperature values range approximately  from 18°C to 38°C.
The distribution is nearly symmetric with most observations concentrated around the middle.
There are no noticeable extreme temperature values.
'''

#fertilizer_kg 
plt.hist(df['fertilizer_kg'], bins=20)
plt.title("Fertilizer Distribution")
plt.xlabel("Fertilizer")
plt.ylabel("Frequency")
plt.show()
'''
Fertilizer usage ranges approximately from 50 kg to 250 kg.
The values are distributed fairly evenly across the range.
No major peaks or outliers are observed.
'''

#yield_ton_per_hectare  
plt.hist(df['yield_ton_per_hectare'], bins=20)
plt.title("Yield Distribution")
plt.xlabel("Yield")
plt.ylabel("Frequency")
plt.show()
'''
Most crop yields are concentrated between 4 and 6 tons per hectare.
The distribution is approximately bell-shaped.
'''

##Q5. Crop Type Analysis 
#Find the number of records for each crop type. 
print(df['crop_type'].value_counts())
 
#Create a count plot (bar chart) for crop_type.  
sns.countplot(x='crop_type', data=df)
plt.title("Crop Type Count")
plt.show()

#Which crop appears most frequently? 
print(df['crop_type'].value_counts().idxmax())
#output- cotton


##Q6. Soil Type Analysis 
#Find the frequency of each soil type. 
print(df['soil_type'].value_counts())
 
#Create a count plot for soil_type. 
sns.countplot(x='soil_type', data=df)
plt.title("Soil Type Count")
plt.show()
 
#Which soil type is most common? 
print(df['soil_type'].value_counts().idxmax())
#output-clay


##Q7. Yield Distribution 
#Create a histogram of yield_ton_per_hectare. 
plt.hist(df['yield_ton_per_hectare'], bins=20)
plt.title("Yield Distribution")
plt.xlabel("Yield")
plt.ylabel("Frequency")
plt.show()

#Is the distribution approximately normal?
#Yes, the distribution is normal (bell-shaped) as most yield values are concentrated around the center of the graph and then it gradually decrease towards both ends.

#Are there any noticeable outliers? 
#No major outliers are visible in the histogram that deviate from the graph.


##Q8. Scatter Plot Analysis 
#Create scatter plots of: 
#1. rainfall_mm vs yield_ton_per_hectare 
plt.scatter(df['rainfall_mm'],
            df['yield_ton_per_hectare'])

plt.xlabel("Rainfall")
plt.ylabel("Yield")
plt.title("Rainfall vs Yield")
plt.show()
 
#2. fertilizer_kg vs yield_ton_per_hectare 
plt.scatter(df['fertilizer_kg'],
            df['yield_ton_per_hectare'])

plt.xlabel("Fertilizer")
plt.ylabel("Yield")
plt.title("Fertilizer vs Yield")
plt.show()

#Which feature appears to have a stronger relationship with yield? 
rainfall_mm appears to have a stronger relationship with yield as the scatter plot shows a clear upward trend and a tighter cluster of points compared to fertilizer_kg with yield plot.


##Q9. Correlation Analysis 
#Generate a correlation matrix for numerical features. 
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)
 
#Create a heatmap.  
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix,
            annot=True,
            cmap='coolwarm')

plt.title("Correlation Heatmap")
plt.show()

#Identify the top three features most correlated with crop yield. 
print(corr_matrix['yield_ton_per_hectare'].sort_values(ascending=False))
# The top three features are rainfall_mm, irrigation_hours and fertilizer_kg 


##Q10. Group-Based Analysis 
#Calculate the average yield for: 
#Each crop type  
crop_avg = df.groupby('crop_type')['yield_ton_per_hectare'].mean()
print(crop_avg)

#Each soil type
soil_avg = df.groupby('soil_type')['yield_ton_per_hectare'].mean()
print(soil_avg) 

#Which crop and soil type have the highest average yield? 
print(crop_avg.idxmax())
print(soil_avg.idxmax())
# output is Rice and Loamy respectively.


##Q11. Feature Encoding 
#The dataset contains categorical variables. 
#Identify the categorical columns.  
print(df.select_dtypes(include='object').columns)

#Convert them into numerical form using One-Hot Encoding. 
df_encoded = pd.get_dummies(
    df,
    columns=['crop_type', 'soil_type']
)
 
#Display the first five rows of the transformed dataset. 
print(df_encoded.head())


##Q12. Feature Selection 
#Separate: Input features (X) and Target variable (y)  
#Specify which column is being used as the target variable. 
X = df_encoded.drop(
    'yield_ton_per_hectare',
    axis=1
)
y = df_encoded['yield_ton_per_hectare']
print("X Shape:", X.shape)
print("y Shape:", y.shape)


##Q13. Train-Test Split 
#Split the dataset into: 80% Training Data and 20% Testing Data  
#Display the shape of: X_train, X_test ,y_train and y_test  
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("X_train:", X_train.shape)
print("X_test :", X_test.shape)
print("y_train:", y_train.shape)
print("y_test :", y_test.shape)


##Q14. Linear Regression Model 
#Train a Linear Regression model.  
model = LinearRegression()
model.fit(X_train, y_train)

#Display the model coefficients and intercept. 
coef_df = pd.DataFrame({
    'Feature': X_train.columns,
    'Coefficient': model.coef_
})
print(coef_df) 
print("Intercept:", model.intercept_)

#Which feature has the highest positive coefficient?
highest = coef_df.loc[
    coef_df['Coefficient'].idxmax()
]
print(highest)
#crop_type_Rice has highest positive coefficient