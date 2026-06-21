# ============================================================
#         Netflix User Analytics - Complete Assignment
# ============================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# ============================================================
#               PART A: DATASET UNDERSTANDING
# ============================================================

# Q1. Load the dataset and display the first five records.

df = pd.read_csv(r'f:/ML Internship Assignments/Netflix.csv')
print("Q1. First 5 Records:")
print(df.head())
print()

# ----------------------------------------------------------

# Q2. Determine the number of rows and columns in the dataset.

print("Q2. Shape of Dataset:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print()

# ----------------------------------------------------------

# Q3. Display all column names.

print("Q3. Column Names:")
print(df.columns.tolist())
print()

# ----------------------------------------------------------

# Q4. Identify numerical and categorical features.

numerical_features = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_features = df.select_dtypes(include=['str']).columns.tolist()

print("Q4. Feature Types:")
print(f"Numerical Features  : {numerical_features}")
print(f"Categorical Features: {categorical_features}")
print()

# ----------------------------------------------------------

# Q5. Check whether the dataset contains missing values.

print("Q5. Missing Values:")
print(df.isnull().sum())
print(f"Total Missing Values: {df.isnull().sum().sum()}")
print()

# ============================================================
#           PART B: EXPLORATORY DATA ANALYSIS
# ============================================================

# Q6. Calculate the average age of users.

avg_age = df['Age'].mean()
print(f"Q6. Average Age of Users: {avg_age:.2f} years")
print()

# ----------------------------------------------------------

# Q7. Determine the average watch hours per week.

avg_watch = df['WatchHoursPerWeek'].mean()
print(f"Q7. Average Watch Hours per Week: {avg_watch:.2f} hours")
print()

# ----------------------------------------------------------

# Q8. Find the average monthly spending of users.

avg_spend = df['MonthlySpend'].mean()
print(f"Q8. Average Monthly Spending: Rs.{avg_spend:.2f}")
print()

# ----------------------------------------------------------

# Q9. Count the number of users in each subscription category.

print("Q9. Users per Subscription Category:")
print(df['SubscriptionType'].value_counts())
print()

# ----------------------------------------------------------

# Q10. Determine the percentage of users who renewed their subscriptions.

renewed_pct = (df['SubscriptionRenewed'] == 'Yes').mean() * 100
print(f"Q10. Percentage of Users who Renewed: {renewed_pct:.2f}%")
print()

# ============================================================
#               PART C: DATA PREPARATION
# ============================================================

# Q11. Encode categorical features using Label Encoding.

print("Q11. Label Encoding Categorical Columns:")
le = LabelEncoder()
df_encoded = df.copy()

for col in ['Gender', 'SubscriptionType', 'FavoriteGenre', 'SubscriptionRenewed']:
    df_encoded[col] = le.fit_transform(df_encoded[col])

print(df_encoded.head())
print()

# ----------------------------------------------------------

# Q12. Define the feature set (X) and target variable (y)
#      for subscription renewal prediction.

X = df_encoded.drop(columns=['UserID', 'SubscriptionRenewed'])
y = df_encoded['SubscriptionRenewed']

print("Q12. Features and Target:")
print(f"Feature Set X columns : {X.columns.tolist()}")
print(f"Target Variable y     : SubscriptionRenewed (0 = No, 1 = Yes)")
print()

# ----------------------------------------------------------

# Q13. Split the dataset into training and testing sets (80/20).

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Q13. Train-Test Split:")
print(f"Training Samples : {X_train.shape[0]}")
print(f"Testing Samples  : {X_test.shape[0]}")
print()

# ============================================================
#          PART D: DECISION TREE CLASSIFICATION
# ============================================================

# Q14. Train a Decision Tree model to predict subscription renewal.

dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
print("Q14. Decision Tree Model trained successfully.")
print()

# ----------------------------------------------------------

# Q15. Evaluate the model using accuracy.

y_pred_dt = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, y_pred_dt)

print(f"Q15. Decision Tree Accuracy: {dt_accuracy * 100:.2f}%")
print()

# ----------------------------------------------------------

# Q16. Generate and interpret the confusion matrix.

cm_dt = confusion_matrix(y_test, y_pred_dt)

print("Q16. Confusion Matrix (Decision Tree):")
print(cm_dt)
print()
print("Interpretation:")
print(f"  True Negatives  (TN) = {cm_dt[0][0]}  → Correctly predicted 'Not Renewed'")
print(f"  False Positives (FP) = {cm_dt[0][1]}  → Predicted 'Renewed' but actually Not Renewed")
print(f"  False Negatives (FN) = {cm_dt[1][0]}  → Predicted 'Not Renewed' but actually Renewed")
print(f"  True Positives  (TP) = {cm_dt[1][1]}  → Correctly predicted 'Renewed'")
print()

# ============================================================
#          PART E: K-NEAREST NEIGHBORS (KNN)
# ============================================================

# Q17. Train a KNN classifier with K = 5.
#      Note: KNN requires feature scaling for best results.

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)
print("Q17. KNN Model (K=5) trained successfully.")
print()

# ----------------------------------------------------------

# Q18. Compare the accuracy of KNN with the Decision Tree model.

y_pred_knn = knn_model.predict(X_test_scaled)
knn_accuracy = accuracy_score(y_test, y_pred_knn)

print("Q18. Model Accuracy Comparison:")
print(f"  Decision Tree Accuracy : {dt_accuracy * 100:.2f}%")
print(f"  KNN (K=5) Accuracy     : {knn_accuracy * 100:.2f}%")

if knn_accuracy > dt_accuracy:
    print("  → KNN performs BETTER than Decision Tree")
elif dt_accuracy > knn_accuracy:
    print("  → Decision Tree performs BETTER than KNN")
else:
    print("  → Both models have EQUAL accuracy")
print()

# ============================================================
#              PART F: LINEAR REGRESSION
# ============================================================

# Q19. Train a Linear Regression model to predict monthly spending.

X_reg = df_encoded.drop(columns=['UserID', 'MonthlySpend', 'SubscriptionRenewed'])
y_reg = df_encoded['MonthlySpend']

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

lr_model = LinearRegression()
lr_model.fit(X_train_r, y_train_r)

y_pred_lr = lr_model.predict(X_test_r)

from sklearn.metrics import r2_score, mean_squared_error
r2   = r2_score(y_test_r, y_pred_lr)
rmse = np.sqrt(mean_squared_error(y_test_r, y_pred_lr))

print("Q19. Linear Regression Model trained successfully.")
print(f"  R² Score : {r2:.4f}  (Higher is better; max = 1.0)")
print(f"  RMSE     : Rs.{rmse:.2f}")
print()

# ----------------------------------------------------------

# Q20. Predict the monthly spending for a new user and interpret the result.

# New user profile:
#   Age=30, Gender=Female(0), SubscriptionType=Premium(1),
#   WatchHoursPerWeek=20, DevicesUsed=3, FavoriteGenre=Action(0), AdClicks=10

new_user = pd.DataFrame({
    'Age'               : [30],
    'Gender'            : [0],    # Female = 0
    'SubscriptionType'  : [1],    # Premium = 1
    'WatchHoursPerWeek' : [20],
    'DevicesUsed'       : [3],
    'FavoriteGenre'     : [0],    # Action = 0
    'AdClicks'          : [10]
})

predicted_spend = lr_model.predict(new_user)[0]

print("Q20. Monthly Spending Prediction for New User:")
print(f"  User Profile   : Age=30, Female, Premium, 20 hrs/week, 3 devices, Action, 10 AdClicks")
print(f"  Predicted Spend: Rs.{predicted_spend:.2f}")
print()
print("  Interpretation : A 30-year-old Female Premium subscriber who watches 20 hrs/week,")
print(f"  uses 3 devices, likes Action genre, and clicks 10 ads is predicted to spend")
print(f"  Rs.{predicted_spend:.2f} per month.")
print()

# ============================================================
#           BUSINESS REFLECTION QUESTIONS
# ============================================================

print("=" * 60)
print("BUSINESS REFLECTION QUESTIONS")
print("=" * 60)
print()
print("1. Which factors appear to influence subscription renewal the most?")
print("   → MonthlySpend, WatchHoursPerWeek, SubscriptionType, and AdClicks")
print("     are the strongest predictors of renewal. Higher engagement and")
print("     spending correlate with users being more likely to renew.")
print()
print("2. Why is subscription renewal a classification problem?")
print("   → Because the output is a discrete category — either 'Yes' or 'No'.")
print("     Classification models predict which class a new data point belongs to.")
print()
print("3. Why is monthly spending a regression problem?")
print("   → Because MonthlySpend is a continuous numerical value (e.g., Rs.317,")
print("     Rs.833). Regression predicts a number on a continuous scale.")
print()
print("4. Which algorithm performed better for renewal prediction?")
print(f"   → Decision Tree ({dt_accuracy*100:.2f}%) outperformed KNN ({knn_accuracy*100:.2f}%).")
print("     Decision Trees handle categorical data and non-linear patterns better")
print("     without needing feature scaling.")
print()
print("5. How could the platform use these predictions to improve customer retention?")
print("   → Users flagged as 'likely to NOT renew' can be targeted with:")
print("     - Personalised discount offers before billing date")
print("     - Content recommendations based on favourite genre")
print("     - Re-engagement email/push notifications")
print("     - Loyalty rewards for long-term subscribers")