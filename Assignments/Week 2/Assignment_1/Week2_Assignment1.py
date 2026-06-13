import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix
#Part A
#Q1Load dataset and display first five records
df = pd.read_csv("/Users/priya/Downloads/Dataset 2.csv")
print(df.head())

# Q2. Number of rows and columns
print(df.shape)

# Q3. Display all column names
print(df.columns)

# Q4. Identify numerical and categorical features
print("Numerical Features:")
print(df.select_dtypes(include=['int64', 'float64']).columns)

print("\nCategorical Features:")
print(df.select_dtypes(include=['object']).columns)

# Q5. Check for missing values
print(df.isnull().sum())

# Q6. Average age of users
print(df['Age'].mean())

# Q7. Average watch hours per week
print(df['WatchHoursPerWeek'].mean())

# Q8. Average monthly spending
print(df['MonthlySpend'].mean())

# Q9. Number of users in each subscription category
print(df['SubscriptionType'].value_counts())

# Q10. Percentage of users who renewed subscriptions
renewed = (df['SubscriptionRenewed'] == 'Yes').mean() * 100
print(renewed)

# Q11. Convert categorical features into numerical form
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
categorical_columns = ['Gender', 'SubscriptionType',
                       'FavoriteGenre', 'SubscriptionRenewed']

for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

print(df.head())

# Q12. Define X and y
X = df.drop(['UserID', 'SubscriptionRenewed'], axis=1)
y = df['SubscriptionRenewed']

# Q13. Split the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Q14. Train Decision Tree model
from sklearn.tree import DecisionTreeClassifier
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

# Q15. Accuracy of Decision Tree
from sklearn.metrics import accuracy_score
y_pred_dt = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, y_pred_dt)

print("Decision Tree Accuracy:", dt_accuracy)

# Q16. Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred_dt)
print(cm)

# Q17. Train KNN classifier (K=5)
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# Q18. Compare accuracy
knn_accuracy = accuracy_score(y_test, y_pred_knn)
print("Decision Tree Accuracy:", dt_accuracy)
print("KNN Accuracy:", knn_accuracy)

#Q19. Train a Linear Regression model to predict monthly spending.
from sklearn.linear_model import LinearRegression
# Features and target variable
X = df.drop(['UserID', 'MonthlySpend'], axis=1)
y = df['MonthlySpend']
# Split the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
# Train the model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
print("Linear Regression model trained successfully.")

#Q20. Predict the monthly spending for a new user and interpret the result.
new_user = [[25, 1, 2, 15, 2, 0, 5, 1]]
# Age, Gender, SubscriptionType, WatchHoursPerWeek,
# DevicesUsed, FavoriteGenre, AdClicks, SubscriptionRenewed
predicted_spend = lr_model.predict(new_user)
print("Predicted Monthly Spending: ₹", predicted_spend[0])