# Part A: Dataset Understanding  

import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Q1. Load the dataset and display the first five records.
df = pd.read_csv('Dataset 2.csv')
df.head()

# Q2. Determine the number of rows and columns in the dataset. 
print('Shape:', df.shape)

# Q3. Display all column names. 
print('Columns:', df.columns)

# Q4. Identify numerical and categorical features.
print('Numerical Features:')
print(df.select_dtypes(include=['int64', 'float64']).columns)

print('\nCategorical Features:')
print(df.select_dtypes(include=['object']).columns)

# Q5. Check whether the dataset contains missing values. 
print(df.isnull().sum())


# Part B: Exploratory Data Analysis 
# Q6. Calculate the average age of users. 
print('Average age of users:',df["Age"].mean())

# Q7. Determine the average watch hours per week.
print('Average watch hours per week:',df["WatchHoursPerWeek"].mean())

# Q8. Find the average monthly spending of users.
print('Average monthly spending of users:',df["MonthlySpend"].mean())

# Q9. Count the number of users in each subscription category. 
print(df["SubscriptionType"].value_counts())

# Q10. Determine the percentage of users who renewed their subscriptions.
renewed = (df["SubscriptionRenewed"] == "Yes").mean() * 100
print('Percentage of renewal of subscription:', renewed)

# Part C: Data Preparation 
# Q11. Convert categorical features into numerical form. 
le = LabelEncoder()
for col in ['Gender',
            'SubscriptionType',
            'FavoriteGenre',
            'SubscriptionRenewed']:
    df[col] = le.fit_transform(df[col])
print(df.head())

# Q12. Define the feature set (X) and target variable (y) for subscription renewal prediction. 
X = df.drop(['UserID','SubscriptionRenewed','MonthlySpend'], axis=1)
y = df['SubscriptionRenewed']

# Q13. Split the dataset into training and testing sets. 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Part D: Decision Tree Classification 
# Q14. Train a Decision Tree model to predict whether a user will renew their subscription. 
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

# Q15. Evaluate the model using accuracy. 
y_pred = dt.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Decision Tree Accuracy:", accuracy)

# Q16. Generate and interpret the confusion matrix. 
cm = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:', cm)

# Part E: K-Nearest Neighbors (KNN) 
# Q17. Train a KNN classifier with K = 5.
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train) 

# Q18. Compare the accuracy of KNN with the Decision Tree model. 
knn_pred = knn.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_pred)
print("Decision Tree Accuracy:", accuracy)
print("KNN Accuracy:", knn_accuracy)

# Part F: Linear Regression 
# Q19. Train a Linear Regression model to predict monthly spending. 
X_reg = df.drop(['UserID','SubscriptionRenewed','MonthlySpend'], axis=1)
y_reg = df["MonthlySpend"]

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg,
    y_reg,
    test_size=0.2,
    random_state=42
)

lr = LinearRegression()
lr.fit(X_train_reg, y_train_reg)

# Q20. Predict the monthly spending for a new user and interpret the result. 
new_user = [[30, 1, 1, 15, 2, 1, 10]]
prediction = lr.predict(new_user)
print("Predicted Monthly Spend:", prediction[0])

# Business Reflection Questions  
# Q1. Which factors appear to influence subscription renewal the most?  
# Ans: From the dataset, features like WatchHoursPerWeek and MonthlySpend seem to have a strong influence on whether a user renews. Users who spend more time watching content or spend more money are more likely to continue. Other factors like SubscriptionType and AdClicks may also have some impact, but they are not as strong as user activity and spending.

# Q2. Why is subscription renewal a classification problem?  
# Ans: The SubscriptionRenewal column has only two possible outcomes (for example: Yes or No). Since the model is predicting one of these categories, it is a classification problem.

# Q3. Why is monthly spending a regression problem?  
# Ans: The MonthlySpend column contains numeric values that can vary continuously. Since we are predicting an exact number and not a category, this makes it a regression problem.

# Q4. Which algorithm performed better for renewal prediction? 
# Ans: The KNN model(0.6) performed better than the Decision Tree(0.5666666666666667), as it achieved a higher accuracy score. This means it was slightly better at predicting the SubscriptionRenewal outcome.

# Q5. How could the platform use these predictions to improve customer retention? 
# Ans: The platform can use SubscriptionRenewal predictions to identify users who may stop their subscription. For example, users with low WatchHoursPerWeek or lower MonthlySpend can be targeted with better content suggestions or special offers. This way, the platform can take action early and try to keep more users subscribed.