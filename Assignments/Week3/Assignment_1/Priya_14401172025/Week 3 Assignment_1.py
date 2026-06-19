import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
# Load Dataset
df = pd.read_csv("agriculture_yield_dataset.csv")
# Q1 Dataset Overview

print("Rows and Columns:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 10 Records:")
print(df.head(10))


# Q2 Data Types and Missing Values

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())


# Q3 Descriptive Statistics

print("\nSummary Statistics:")
print(df.describe())

numeric_cols = df.select_dtypes(include=np.number)

highest_mean = numeric_cols.mean().idxmax()
highest_std = numeric_cols.std().idxmax()

print("\nFeature with Highest Mean:", highest_mean)
print("Feature with Highest Standard Deviation:", highest_std)


# Q4 Distribution Analysis

cols = ['rainfall_mm', 'temperature_c',
        'fertilizer_kg', 'yield_ton_per_hectare']
for col in cols:
    plt.figure(figsize=(6,4))
    plt.hist(df[col], bins=20)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

# Q5 Crop Type Analysis

print("\nCrop Type Frequency:")
print(df['crop_type'].value_counts())

plt.figure(figsize=(6,4))
sns.countplot(x='crop_type', data=df)
plt.title("Crop Type Count")
plt.show()

print("\nMost Frequent Crop:")
print(df['crop_type'].value_counts().idxmax())


# Q6 Soil Type Analysis

print("\nSoil Type Frequency:")
print(df['soil_type'].value_counts())
plt.figure(figsize=(6,4))
sns.countplot(x='soil_type', data=df)
plt.title("Soil Type Count")
plt.show()
print("\nMost Common Soil Type:")
print(df['soil_type'].value_counts().idxmax())


# Q7 Yield Distribution

plt.figure(figsize=(6,4))
plt.hist(df['yield_ton_per_hectare'], bins=20)
plt.title("Yield Distribution")
plt.xlabel("Yield")
plt.ylabel("Frequency")
plt.show()


# Q8 Scatter Plot Analysis

plt.figure(figsize=(6,4))
plt.scatter(df['rainfall_mm'],
            df['yield_ton_per_hectare'])
plt.xlabel("Rainfall")
plt.ylabel("Yield")
plt.title("Rainfall vs Yield")
plt.show()
plt.figure(figsize=(6,4))
plt.scatter(df['fertilizer_kg'],
            df['yield_ton_per_hectare'])
plt.xlabel("Fertilizer")
plt.ylabel("Yield")
plt.title("Fertilizer vs Yield")
plt.show()

# Q9 Correlation Analysis

corr = numeric_cols.corr()
print("\nCorrelation Matrix:")
print(corr)
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
yield_corr = corr['yield_ton_per_hectare'].sort_values(
    ascending=False)
print("\nTop Features Correlated with Yield:")
print(yield_corr)


# Q10 Group-Based Analysis

crop_yield = df.groupby('crop_type')[
    'yield_ton_per_hectare'].mean()
soil_yield = df.groupby('soil_type')[
    'yield_ton_per_hectare'].mean()
print("\nAverage Yield by Crop:")
print(crop_yield)
print("\nAverage Yield by Soil:")
print(soil_yield)
print("\nHighest Yield Crop:",
      crop_yield.idxmax())
print("Highest Yield Soil:",
      soil_yield.idxmax())


# Q11 Feature Encoding

categorical_cols = ['crop_type', 'soil_type']
print("\nCategorical Columns:")
print(categorical_cols)
encoded_df = pd.get_dummies(
    df,
    columns=categorical_cols,
    drop_first=True
)
print("\nFirst 5 Rows After Encoding:")
print(encoded_df.head())

# Q12 Feature Selection

X = encoded_df.drop(
    'yield_ton_per_hectare',
    axis=1
)
y = encoded_df['yield_ton_per_hectare']
print("\nTarget Variable:")
print("yield_ton_per_hectare")


# Q13 Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42
)
print("\nX_train Shape:", X_train.shape)
print("X_test Shape:", X_test.shape)
print("y_train Shape:", y_train.shape)
print("y_test Shape:", y_test.shape)


# Q14 Linear Regression

model = LinearRegression()
model.fit(X_train, y_train)
print("\nIntercept:")
print(model.intercept_)
coef_df = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
})
print("\nCoefficients:")
print(coef_df)

highest_positive = coef_df.loc[
    coef_df['Coefficient'].idxmax()
]
print("\nFeature with Highest Positive Coefficient:")
print(highest_positive)