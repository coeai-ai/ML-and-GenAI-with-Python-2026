# Netflix User Analytics Assignment

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset

df = pd.read_csv("Dataset 2.csv")

print(df.head())

# Q2. Rows and columns

print(df.shape)

# Q3. Column names

print(df.columns)

# Q4. Numerical and categorical features

numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
categorical_features = df.select_dtypes(include=['object']).columns

print("Numerical Features:")
print(numerical_features)

print("Categorical Features:")
print(categorical_features)

# Q5. Missing values

print(df.isnull().sum())

# Q6-Q10. Basic analysis

print("Average Age:", df['Age'].mean())
print("Average Watch Hours Per Week:", df['WatchHoursPerWeek'].mean())
print("Average Monthly Spend:", df['MonthlySpend'].mean())

print("Subscription Category Count:")
print(df['SubscriptionType'].value_counts())

print("Subscription Renewal Percentage:")
print(df['SubscriptionRenewed'].value_counts(normalize=True) * 100)

# Q11. Convert categorical features into numerical form

df_encoded = df.copy()

label_encoder = LabelEncoder()

for column in df_encoded.select_dtypes(include=['object']).columns:
    df_encoded[column] = label_encoder.fit_transform(df_encoded[column])

print(df_encoded.head())

# Q12. Define X and y for subscription renewal prediction

X = df_encoded.drop(['UserID', 'SubscriptionRenewed'], axis=1)
y = df_encoded['SubscriptionRenewed']

print(X.head())
print(y.head())

# Q13. Split dataset into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Q14. Train Decision Tree model

dt_model = DecisionTreeClassifier(random_state=42, max_depth=4)
dt_model.fit(X_train, y_train)

print("Decision Tree model trained successfully.")

# Q15. Decision Tree accuracy

dt_predictions = dt_model.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_predictions)

print("Decision Tree Accuracy:", dt_accuracy)

# Q16. Confusion matrix

dt_cm = confusion_matrix(y_test, dt_predictions)

print("Decision Tree Confusion Matrix:")
print(dt_cm)

# Feature importance

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': dt_model.feature_importances_
})

feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

print("Feature Importance:")
print(feature_importance)

# Q17. Train KNN classifier with K = 5

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)

print("KNN model trained successfully.")

# Q18. Compare KNN with Decision Tree

knn_predictions = knn_model.predict(X_test_scaled)

knn_accuracy = accuracy_score(y_test, knn_predictions)

print("KNN Accuracy:", knn_accuracy)
print("Decision Tree Accuracy:", dt_accuracy)

if knn_accuracy > dt_accuracy:
    print("KNN performed better than Decision Tree.")
elif dt_accuracy > knn_accuracy:
    print("Decision Tree performed better than KNN.")
else:
    print("Both models performed equally.")

# Q19. Linear Regression to predict MonthlySpend

X_reg = df_encoded.drop(['UserID', 'MonthlySpend'], axis=1)
y_reg = df_encoded['MonthlySpend']

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

lr_model = LinearRegression()
lr_model.fit(X_train_reg, y_train_reg)

print("Linear Regression model trained successfully.")

# Evaluate Linear Regression

lr_predictions = lr_model.predict(X_test_reg)

mae = mean_absolute_error(y_test_reg, lr_predictions)
mse = mean_squared_error(y_test_reg, lr_predictions)
rmse = mse ** 0.5
r2 = r2_score(y_test_reg, lr_predictions)

print("Mean Absolute Error:", mae)
print("Root Mean Squared Error:", rmse)
print("R2 Score:", r2)

# Q20. Predict monthly spending for a new user

new_user = X_test_reg.iloc[[0]]

predicted_spend = lr_model.predict(new_user)

print("Predicted Monthly Spending:", predicted_spend[0])
print("Interpretation: The model predicts that this user may spend approximately ₹", round(predicted_spend[0], 2), "per month.")