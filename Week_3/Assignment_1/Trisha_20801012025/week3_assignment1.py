# Exploratory Data Analysis (EDA) and Machine Learning
# Agricultural Yield Dataset

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Part A: Understanding Dataset

# Q1. Dataset Overview
df = pd.read_csv("agriculture_yield_dataset.csv")

print("Q1. Dataset Overview")
print("Rows and Columns:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 10 Records:")
print(df.head(10))


# Q2. Data Types and Missing Values
print("\n\nQ2. Data Types and Missing Values")
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())


# Q3. Descriptive Statistics
print("\n\nQ3. Descriptive Statistics")
print(df.describe())

numeric_df = df.select_dtypes(include=["int64", "float64"])

highest_mean_feature = numeric_df.mean().idxmax()
highest_std_feature = numeric_df.std().idxmax()

print("\nFeature with highest mean value:", highest_mean_feature)
print("Feature with highest standard deviation:", highest_std_feature)


# Part B: Exploratory Data Analysis

# Q4. Distribution Analysis
print("\n\nQ4. Distribution Analysis")

distribution_columns = [
    "rainfall_mm",
    "temperature_c",
    "fertilizer_kg",
    "yield_ton_per_hectare"
]

for col in distribution_columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


# Q5. Crop Type Analysis
print("\n\nQ5. Crop Type Analysis")

crop_counts = df["crop_type"].value_counts()
print("\nCrop Type Counts:")
print(crop_counts)

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="crop_type")
plt.title("Count of Each Crop Type")
plt.xlabel("Crop Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

most_frequent_crop = crop_counts.idxmax()
print("Most frequent crop type:", most_frequent_crop)


# Q6. Soil Type Analysis
print("\n\nQ6. Soil Type Analysis")

soil_counts = df["soil_type"].value_counts()
print("\nSoil Type Counts:")
print(soil_counts)

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="soil_type")
plt.title("Count of Each Soil Type")
plt.xlabel("Soil Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

most_common_soil = soil_counts.idxmax()
print("Most common soil type:", most_common_soil)


# Q7. Yield Distribution
print("\n\nQ7. Yield Distribution")

plt.figure(figsize=(8, 5))
sns.histplot(df["yield_ton_per_hectare"], kde=True)
plt.title("Distribution of Yield per Hectare")
plt.xlabel("Yield Ton per Hectare")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# Q8. Scatter Plot Analysis
print("\n\nQ8. Scatter Plot Analysis")

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="rainfall_mm", y="yield_ton_per_hectare")
plt.title("Rainfall vs Yield")
plt.xlabel("Rainfall in mm")
plt.ylabel("Yield Ton per Hectare")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="fertilizer_kg", y="yield_ton_per_hectare")
plt.title("Fertilizer vs Yield")
plt.xlabel("Fertilizer in kg")
plt.ylabel("Yield Ton per Hectare")
plt.tight_layout()
plt.show()


# Q9. Correlation Analysis
print("\n\nQ9. Correlation Analysis")

corr_matrix = numeric_df.corr()
print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.show()

yield_correlation = corr_matrix["yield_ton_per_hectare"].sort_values(ascending=False)
print("\nCorrelation with Yield:")
print(yield_correlation)

top_three_features = yield_correlation.drop("yield_ton_per_hectare").head(3)
print("\nTop Three Features Most Correlated with Yield:")
print(top_three_features)


# Q10. Group-Based Analysis
print("\n\nQ10. Group-Based Analysis")

crop_avg_yield = df.groupby("crop_type")["yield_ton_per_hectare"].mean().sort_values(ascending=False)
print("\nAverage Yield by Crop Type:")
print(crop_avg_yield)

soil_avg_yield = df.groupby("soil_type")["yield_ton_per_hectare"].mean().sort_values(ascending=False)
print("\nAverage Yield by Soil Type:")
print(soil_avg_yield)

highest_yield_crop = crop_avg_yield.idxmax()
highest_yield_soil = soil_avg_yield.idxmax()

print("\nCrop type with highest average yield:", highest_yield_crop)
print("Soil type with highest average yield:", highest_yield_soil)


# Part C: Data Preparation

# Q11. Feature Encoding
print("\n\nQ11. Feature Encoding")

categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()
print("\nCategorical Columns:")
print(categorical_columns)

encoded_df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

print("\nFirst 5 Rows of Transformed Dataset:")
print(encoded_df.head())


# Q12. Feature Selection
print("\n\nQ12. Feature Selection")

X = encoded_df.drop("yield_ton_per_hectare", axis=1)
y = encoded_df["yield_ton_per_hectare"]

print("\nInput Features:")
print(X.columns.tolist())

print("\nTarget Variable: yield_ton_per_hectare")


# Part D: Machine Learning

# Q13. Train-Test Split
print("\n\nQ13. Train-Test Split")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)


# Q14. Linear Regression Model
print("\n\nQ14. Linear Regression Model")

model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Intercept:")
print(model.intercept_)

print("\nModel Coefficients:")
print(model.coef_)

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

coefficients_sorted = coefficients.sort_values(by="Coefficient", ascending=False)

print("\nModel Coefficients with Feature Names:")
print(coefficients_sorted)

highest_positive_feature = coefficients_sorted.iloc[0]

print("\nFeature with Highest Positive Coefficient:")
print(highest_positive_feature)


# Additional Model Evaluation
print("\n\nAdditional Model Evaluation")

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R2 Score:", r2)

comparison = pd.DataFrame({
    "Actual Yield": y_test,
    "Predicted Yield": y_pred
})

print("\nActual vs Predicted Values:")
print(comparison.head())

plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("Actual vs Predicted Yield")
plt.tight_layout()
plt.show()