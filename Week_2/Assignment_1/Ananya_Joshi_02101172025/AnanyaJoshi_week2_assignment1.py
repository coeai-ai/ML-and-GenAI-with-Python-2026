import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import os

# ==========================================
# 0. DATA LOADING
# ==========================================
file_name = 'netflix_dataset.csv'

if not os.path.exists(file_name):
    print(f"Error: '{file_name}' not found. Please ensure the dataset is in the same folder as this script.")
    exit()

# Load the dataset
df = pd.read_csv(file_name)

print("="*50)
print("PART A: DATASET UNDERSTANDING")
print("="*50)

# Q1. Load the dataset and display the first five records.
print("\nQ1: First five records:")
print(df.head())

# Q2. Determine the number of rows and columns in the dataset.
print(f"\nQ2: The dataset has {df.shape[0]} rows and {df.shape[1]} columns.")

# Q3. Display all column names.
print("\nQ3: Column names in the dataset:")
print(df.columns.tolist())

# Q4. Identify numerical and categorical features.
numerical_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = df.select_dtypes(include=['object']).columns.tolist()
print(f"\nQ4: \nNumerical Features: {numerical_features}\nCategorical Features: {categorical_features}")

# Q5. Check whether the dataset contains missing values.
print("\nQ5: Missing values in each column:")
print(df.isnull().sum())
print("Total missing values:", df.isnull().sum().sum())


print("\n" + "="*50)
print("PART B: EXPLORATORY DATA ANALYSIS")
print("="*50)

# Q6. Calculate the average age of users.
avg_age = df['Age'].mean()
print(f"\nQ6: Average age of users: {avg_age:.2f} years")

# Q7. Determine the average watch hours per week.
avg_watch_hours = df['WatchHoursPerWeek'].mean()
print(f"\nQ7: Average watch hours per week: {avg_watch_hours:.2f} hours")

# Q8. Find the average monthly spending of users.
avg_spend = df['MonthlySpend'].mean()
print(f"\nQ8: Average monthly spending: ${avg_spend:.2f}")

# Q9. Count the number of users in each subscription category.
print("\nQ9: Number of users per subscription category:")
print(df['SubscriptionType'].value_counts())

# Q10. Determine the percentage of users who renewed their subscriptions.
renewal_pct = (df['SubscriptionRenewed'] == 'Yes').mean() * 100
print(f"\nQ10: Percentage of users who renewed: {renewal_pct:.2f}%")


print("\n" + "="*50)
print("PART C: DATA PREPARATION")
print("="*50)

# Q11. Convert categorical features into numerical form.
# We use Label Encoding for binary categories and One-Hot Encoding (get_dummies) for others
df_processed = df.copy()

# Drop UserID as it is just an identifier and has no predictive power
df_processed = df_processed.drop('UserID', axis=1)

# Encode target variable manually for clarity
df_processed['SubscriptionRenewed'] = df_processed['SubscriptionRenewed'].map({'Yes': 1, 'No': 0})
df_processed['Gender'] = df_processed['Gender'].map({'Male': 1, 'Female': 0})

# One-hot encode the remaining categorical columns (SubscriptionType, FavoriteGenre)
df_processed = pd.get_dummies(df_processed, columns=['SubscriptionType', 'FavoriteGenre'], drop_first=True)

print("\nQ11: Categorical features converted to numerical. (First 3 rows shown)")
print(df_processed.head(3))

# Q12. Define the feature set (X) and target variable (y) for subscription renewal prediction.
X_clf = df_processed.drop('SubscriptionRenewed', axis=1)
y_clf = df_processed['SubscriptionRenewed']
print(f"\nQ12: Feature set X shape: {X_clf.shape}, Target y shape: {y_clf.shape}")

# Q13. Split the dataset into training and testing sets. (Standard 80-20 split)
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)
print(f"\nQ13: Split completed. Training set: {X_train_clf.shape[0]} rows. Testing set: {X_test_clf.shape[0]} rows.")


print("\n" + "="*50)
print("PART D: DECISION TREE CLASSIFICATION")
print("="*50)

# Q14. Train a Decision Tree model to predict whether a user will renew their subscription.
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train_clf, y_train_clf)
print("\nQ14: Decision Tree model trained successfully.")

# Q15. Evaluate the model using accuracy.
dt_predictions = dt_model.predict(X_test_clf)
dt_accuracy = accuracy_score(y_test_clf, dt_predictions)
print(f"\nQ15: Decision Tree Accuracy: {dt_accuracy * 100:.2f}%")

# Q16. Generate and interpret the confusion matrix.
dt_cm = confusion_matrix(y_test_clf, dt_predictions)
print("\nQ16: Confusion Matrix:")
print(dt_cm)
print("Interpretation:")
print(f"True Positives (Correctly predicted Renewals): {dt_cm[1][1]}")
print(f"True Negatives (Correctly predicted Non-renewals): {dt_cm[0][0]}")
print(f"False Positives (Predicted Renewal, but actually didn't): {dt_cm[0][1]}")
print(f"False Negatives (Predicted Non-renewal, but actually did): {dt_cm[1][0]}")


print("\n" + "="*50)
print("PART E: K-NEAREST NEIGHBORS (KNN)")
print("="*50)

# Q17. Train a KNN classifier with K=5.
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_clf, y_train_clf)
print("\nQ17: KNN Classifier (K=5) trained successfully.")

# Q18. Compare the accuracy of KNN with the Decision Tree model.
knn_predictions = knn_model.predict(X_test_clf)
knn_accuracy = accuracy_score(y_test_clf, knn_predictions)
print(f"\nQ18: KNN Accuracy: {knn_accuracy * 100:.2f}%")
print(f"Comparison: Decision Tree ({dt_accuracy * 100:.2f}%) vs KNN ({knn_accuracy * 100:.2f}%)")
if dt_accuracy > knn_accuracy:
    print("Conclusion: Decision Tree performed better on this dataset.")
else:
    print("Conclusion: KNN performed better on this dataset.")


print("\n" + "="*50)
print("PART F: LINEAR REGRESSION")
print("="*50)

# Q19. Train a Linear Regression model to predict monthly spending.
# Redefine X and y for Regression (Target = MonthlySpend)
X_reg = df_processed.drop('MonthlySpend', axis=1)
y_reg = df_processed['MonthlySpend']

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

lr_model = LinearRegression()
lr_model.fit(X_train_reg, y_train_reg)
print("\nQ19: Linear Regression model trained to predict Monthly Spend.")

# Q20. Predict the monthly spending for a new user and interpret the result.
# Creating a dummy new user using the median/mode of our dataset columns
new_user_data = {col: [X_reg[col].median() if X_reg[col].nunique() > 2 else X_reg[col].mode()[0]] for col in X_reg.columns}
new_user_df = pd.DataFrame(new_user_data)

predicted_spend = lr_model.predict(new_user_df)[0]
print(f"\nQ20: Predicted Monthly Spending for a new 'average' user: ${predicted_spend:.2f}")
print("Interpretation: Based on the historical data of average watch hours, ad clicks, and demographics, "
      "the model estimates this new user will generate this amount of monthly revenue.")
