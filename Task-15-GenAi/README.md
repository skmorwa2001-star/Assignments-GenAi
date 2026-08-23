# ------------------------- Assignment 15 : Core Algorithmns, Metrics & Model Behavior ------------------------

## Assignment
- After prepraring features and Pipelines , your task is to build core ML models, evaluate them using appropriate metrics, and understand model behaviour such as overfitting and underfitting.

### Assignment Focuses on ML Algorithms and evaluation concepts:
- Linear Regression
- Logistic Regression 
- Naive Bayes
- K-Nearest Neighbours (KNN)
- Regression Metrics
- Classification Metrics
- Bias- Variance, Overfitting & Underfitting


## PART 1 - Regression Algorithms

### Task 1: Linear Regression
- Uses the previous dataset used in previous assignments
- Clean format used in which no missing values in it
1. Select the Numerical target variables
- Select only numerical columns and make a target column as 'original_price'
- We have predict the output for original_price for the product
2. Split the data into Training and testing sets
- We have to import train_test_split from sklearn.model_selection
- Split the data into 80% in training and 20% in testing
3. Train a Linear Regression model using scikit learn
- import LinearRegression model from sklearn.linear_model
- feed the data into model 
4. Make Prediction on test data
- X_test values pass into the model to make prediction 
5. Plot Actual vs Predicted Values
- with the help of matplotlib plot a scatterplot which shows different of actual and predicted values


## PART 2 - Regression Metrics

### Task 2: Regression Evaluation Metrics
