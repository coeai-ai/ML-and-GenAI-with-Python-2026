##Part A: Dataset Understanding 
#Q1-Load the dataset and display the first five records. 
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('Netflix_User_Analytics.csv')
df.head()

#Q2-Determine the number of rows and columns in the dataset. 
print('No of rows and columns respectively=',df.shape)

#Q3-Display all column names. 
print('Column names',df.columns)

#Q4-Identify numerical and categorical features. 
print("Numerical Features:")
print(df.select_dtypes(include=['int64', 'float64']).columns)

print("Categorical Features:")
print(df.select_dtypes(include=['object']).columns)

#Q5-Check whether the dataset contains missing value
print(df.isnull().sum())

##Part B: Exploratory Data Analysis 
#Q6-Calculate the average age of users. 
print('Average age of users=',df["Age"].mean())

#Q7-Determine the average watch hours per week.
print('Average watch hours per week=',df["WatchHoursPerWeek"].mean())

#Q8-Find the average monthly spending of users.
print('Average monthly spending of users=',df["MonthlySpend"].mean())
 
#Q9-Count the number of users in each subscription category. 
print(df["SubscriptionType"].value_counts())

#Q10-Determine the percentage of users who renewed their subscriptions.
renewed = (df["SubscriptionRenewed"] == "Yes").mean() * 100
print(renewed) 

##Part C: Data Preparation 
#Q11-Convert categorical features into numerical form. 
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])
print(df.head())

#Q12-Define the feature set (X) and target variable (y) for subscription renewal prediction. 
X = df.drop("SubscriptionRenewed", axis=1)
y = df["SubscriptionRenewed"]

#Q13-Split the dataset into training and testing sets. 
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
##Part D: Decision Tree Classification 
#Q14-Train a Decision Tree model to predict whether a user will renew their subscription. 
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

#Q15-Evaluate the model using accuracy. 
y_pred = dt.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

#Q16-Generate and interpret the confusion matrix. 
cm = confusion_matrix(y_test, y_pred)
print(cm)

##Part E: K-Nearest Neighbors (KNN) 
#Q17-Train a KNN classifier with K = 5.
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train) 

#Q18-Compare the accuracy of KNN with the Decision Tree model. 
knn_pred = knn.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_pred)
print("Decision Tree Accuracy:", accuracy)
print("KNN Accuracy:", knn_accuracy)

##Part F: Linear Regression 
#Q19-Train a Linear Regression model to predict monthly spending. 
X_reg = df.drop("MonthlySpend", axis=1)
y_reg = df["MonthlySpend"]
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg,
    y_reg,
    test_size=0.2,
    random_state=42
)
lr = LinearRegression()
lr.fit(X_train_reg, y_train_reg)

#Q20-Predict the monthly spending for a new user and interpret the result. 
prediction = lr.predict([[
    101,  # UserID
    25,   # Age
    1,    # Gender
    2,    # SubscriptionType
    15,   # WatchHoursPerWeek
    3,    # DevicesUsed
    0,    # FavoriteGenre
    5,    # AdClicks
    1     # SubscriptionRenewed
]])
print("Predicted Monthly Spend:", prediction[0])

##Business Reflection Questions  
##1. Which factors appear to influence subscription renewal the most?  
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': dt.feature_importances_
})
print(feature_importance.sort_values(by='Importance', ascending=False))
#By this code we get to know 'MonthlySpend' appears to influence subscription renewal the most followed by 'Age' and 'WatchHoursPerWeek'. 

##2. Why is subscription renewal a classification problem?  
#Ans- Subscription renewal is a classification problem as the answer is in the form of categories either 'yes' or 'no'.

##3. Why is monthly spending a regression problem?  
#Ans- Monthly Spending is a regression problem as the answer is in the form of continuous numerical value.

##4. Which algorithm performed better for renewal prediction? 
#Ans-Decision Tree Accuracy was 0.5666666666666667 and KNN Accuracy was 0.6, so KNN performed better for renewal prediction.

##5. How could the platform use these predictions to improve customer retention? 
#Ans-Netflix can identify users who are likely or not likely to renew their subscriptions and can offer them personalized discounts, or special offers based on this. They can also provide personalized recommendations based on all the factors like gender,age,watch hours, favorite genre etc.This can help improve customer satisfaction and increase retention.