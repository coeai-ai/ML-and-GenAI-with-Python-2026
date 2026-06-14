import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression

from sklearn.metrics import accuracy_score, confusion_matrix
# load the dataset
df = pd.read_csv("Dataset 2.csv")
# part(A) Dataset Understanding
#Q1. Load the dataset and display the first five records
print(df.head())

#Q2. Determine the number of rows and columns
print("Rows and Columns:", df.shape)

#Q3. Display all column names
print(df.columns)

#Q4. Identify numerical and categorical features
print("Numerical Features:")
print(df.select_dtypes(include=['int64','float64']).columns)

#print("\nCategorical Features:")
print(df.select_dtypes(include=['object']).columns)

#Q5. Check whether the dataset contains missing values
print(df.isnull().sum())

#Part B: Exploratory Data Analysis
#Q6. Calculate the average age of users
print("Average Age =", df['Age'].mean())

#Q7. Determine the average watch hours per week
print("Average Watch Hours =", df['WatchHoursPerWeek'].mean())

#Q8. Find the average monthly spending of users
print("Average Monthly Spend =", df['MonthlySpend'].mean())

#Q9. Count the number of users in each subscription category
print(df['SubscriptionType'].value_counts())

#Q10. Determine the percentage of users who renewed their subscriptions
renewed_percentage = (
    df['SubscriptionRenewed'].value_counts(normalize=True)['Yes']
) * 100

print("Renewed Percentage =", renewed_percentage)

#Part C: Data Preparation
#Q11. Convert categorical features into numerical form
le = LabelEncoder()

for col in ['Gender',
            'SubscriptionType',
            'FavoriteGenre',
            'SubscriptionRenewed']:
    df[col] = le.fit_transform(df[col])

print(df.head())

#Q12. Define the feature set (X) and target variable (y)


X = df.drop(['UserID', 'SubscriptionRenewed'], axis=1)
y = df['SubscriptionRenewed']

print("Features (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

#Q13. Split the dataset into training and testing sets

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

print("Training Labels Shape:", y_train.shape)
print("Testing Labels Shape:", y_test.shape)

#Part D: Decision Tree Classification
#Q14. Train a Decision Tree model

dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

#Q15. Evaluate the model using accuracy

y_pred_dt = dt.predict(X_test)
dt_accuracy = accuracy_score(y_test, y_pred_dt)

print("Decision Tree Accuracy =", dt_accuracy)

#Q16. Generate and interpret the confusion matrix

cm = confusion_matrix(y_test, y_pred_dt)

print("Confusion Matrix:")
print(cm)

#Part E: K-Nearest Neighbors (KNN)

#Q17. Train a KNN classifier with K = 5

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

#Q18. Compare the accuracy of KNN with the Decision Tree model

y_pred_knn = knn.predict(X_test)

knn_accuracy = accuracy_score(y_test, y_pred_knn)

print("Decision Tree Accuracy =", dt_accuracy)
print("KNN Accuracy =", knn_accuracy)

#Part F: Linear Regression

#Q19. Train a Linear Regression model to predict monthly spending

X_reg = df.drop(['UserID', 'MonthlySpend'], axis=1)
y_reg = df['MonthlySpend']

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg,
    y_reg,
    test_size=0.20,
    random_state=42
)

lr = LinearRegression()

lr.fit(X_train_reg, y_train_reg)

#Q20. Predict the monthly spending for a new user

new_user = [[25, 1, 2, 15, 3, 1, 10, 1]]

prediction = lr.predict(new_user)

print("Predicted Monthly Spend =", prediction[0])



