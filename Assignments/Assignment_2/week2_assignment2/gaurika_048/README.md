STUDENT NAME: Gaurika Yadav
ENROLLMENT NUMBER: 04801182025
COLLEGE NAME: igdtuw

### Q1. Loan Application Approval Prediction

This is a classification problem because the final outcome we want to predict is a clear, discrete category with only two choices: whether the bank will approve the loan or reject it.
The most suitable algorithm for this task would be a Decision Tree. Banks prefer Decision Trees because they mimic a straightforward, rule-based human logic process that is very easy to explain to auditors or customers. For instance, the model can look at data and say, "If this applicant's monthly income is above ₹50,000, move to the next check; if their credit score is above 750, then approve the loan." Linear Regression wouldn't work here at all since it is built to predict continuous numbers like stock prices or temperatures, rather than making a clear yes-or-no choice.


### Q2. Features vs. Labels

To understand the difference, think of a feature as the input piece of information we feed into a machine learning model, while the label is the final output or answer we want the model to guess.
A simple everyday example is predicting whether a student will pass or fail an upcoming exam. The features would be the measurable facts we collect beforehand, such as the total hours the student spent studying, their school attendance percentage, and how many mock tests they practiced. The label, on the other hand, is the final result on report card day, which is simply whether they "Passed" or "Failed."


### Q3. How a Decision Tree Reaches a Prediction

A Decision Tree arrives at a prediction by passing a customer's data down a flowchart-like structure that splits into branches based on specific questions. It starts at the very top with a main question and filters the data downward based on the answers.
If the tree is trying to predict whether someone will buy a laptop, it might first ask, "Is the user looking at the checkout page?" If yes, it follows that branch to the next question: "Did they apply a coupon code?" If the answer is yes again, the data hits a final leaf node at the bottom of the path, which outputs the definitive prediction: "The customer will purchase the product."


### Q4. KNN as a Supervised Algorithm

K-Nearest Neighbors is classified as a supervised learning algorithm because it can only make predictions if it has a pre-existing, labeled training dataset to learn from. It works by mapping new, unknown data points directly onto historical data where the correct answers are already known.
Because of this, KNN absolutely cannot perform classification if labels are missing. Without those pre-existing labels, the algorithm can still calculate distances and figure out which data points sit closest to each other, but it won't have any categories to read from to give you a final answer. It is like looking at a group of unfamiliar objects; you can tell which ones look alike, but you can't name what they are if nobody ever taught you the names.


### Q5. KNN Prediction Example with K=5

The final prediction for this model will be "Yes."
KNN runs on a simple majority voting system among the closest data points. In this scenario, we set our neighborhood boundary to look at the five closest neighbors. When we check their identities, the label "Yes" appears three times, while the label "No" only appears two times. Since three is greater than two, "Yes" holds the majority vote, and the model assigns it as the final prediction.


### Q6. The Linear Regression Equation ($y = mx + b$)

This formula represents the equation of a straight line that a model draws through data points to predict numerical trends. Each letter represents a specific part of that relationship:

* **$y$** is the dependent variable or the final label we want to predict.
* **$x$** is the independent variable or the feature input we are using to make the guess.
* **$m$** represents the slope or the coefficient. It tells us the direction of the line and exactly how much $y$ will change whenever $x$ goes up by one unit.
* **$b$** represents the y-intercept or the bias. This is the baseline starting value of $y$ when our input feature $x$ is completely zero.


### Q7. Understanding Correlation

Correlation measures the strength and direction of a straight-line relationship between two different variables.
A value of **+1** means a perfect positive correlation, where both variables move in the exact same direction; if one goes up, the other goes up proportionally. A value of **0** indicates absolutely no correlation, meaning the variables have zero linear connection and changes in one tell you nothing about the other. A value of **-1** represents a perfect negative correlation, which is an inverse relationship where one variable goes up and the other drops down by the exact same proportion.


### Q8. False Negatives in Disease Detection

This specific error is called a False Negative, which happens when a model mistakenly outputs a healthy or negative result even though the real-world condition is present.
This is an incredibly dangerous error in healthcare because a patient who is actually carrying a serious disease will be told they are completely fine and sent home. Because they believe the model's incorrect prediction, they will miss out on critical, early medical care. This gives the underlying illness more time to worsen without any treatment, which can quickly become life-threatening.


### Q9. Confusion Matrix vs. Correlation Matrix

A Confusion Matrix is an evaluation table used to judge the performance of a classification model after it finishes training. It maps out a grid showing exactly how many times the model guessed right or wrong by breaking things down into True Positives, True Negatives, False Positives, and False Negatives.
A Correlation Matrix is completely different because it doesn't evaluate model predictions. Instead, it is used during initial data analysis to look at the raw features and show how tightly coupled different columns are to one another before any machine learning even takes place.


### Q10. Summary of Machine Learning Algorithms

* A Decision Tree breaks data down by running it through a sequence of step-by-step, flowchart-like questions to sort data into categories or values.
* KNN classifies an unknown data point by measuring physical distance, finding its closest geographical neighbors, and taking a majority vote.
* An SVM works by drawing an optimal boundary line or hyperplane that creates the widest possible physical gap to separate different classes of data.
* Linear Regression draws a single straight line of best fit directly through continuous data points to predict numeric values based on visible trends.
* A Neural Network models data by passing inputs through layers of interconnected processing nodes that mimic human brain cells to catch highly complex, non-linear patterns.
