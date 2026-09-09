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

### Task 2 : Regression Evaluation Metrics
- Using predictions from Linear Regression 
1. Mean Absolute Error (MAE) ---> When all errors are equally important & we want a Robust metric againist outliers.
2. Mean Squared Error (MSE) ---> THe value is getting squared sso the error is huge mistake here . when we want to penalize large errors
3. Root Mean Squared Error (RMSE) --> Perfered when large errors are particularly undersierable. More sensitive to outliers.


## PART 3 - Classification Algorithms

### Task 3 : Logistic Regression
- Used LabelEncoder to convert categorical data into numerical data
- Logistic Regression is used for Binary output like 0, 1
- So that we can select is_returned columns as the target columns
- It give idea that customer return the product or not
1. Select the classification target variable
- We are select the target variable and nominal variable
2. Split data into training and testing sets
- import the libraries to separate into training and testing data as ---> from sklearn.model_selection import LogisticRegression
3. Train a Logistic Regression model
- import the logistic model from sklearn libraries
4. Make prediction
- Give the data to model to predict the output


### Task 4 : Naive Bayes Classifier
1. Train a Naive Bayes model (GaussianNB)
- import the GaussuanNB from sklearn library ---> from sklearn.naive_bayes import GaussianNB
2. Predict the output mean customer is returned the product 
3. Compare results with Logistic Regression
- Define the accuracy score 
- from sklearn.metrics import accuracy_score
- accuracy_score(Y_test,Y_predict)
- It helps us to explains the prediction score

### Task 5 : K-Nearest Neighbors (KNN)
- from sklearn.neighbors import KNeighborsClassifier
- KNN=KNeighborsClassifier(n_neighbors=17)
- pass the data to model using fit ---> KNN.fit(X_train,Y_train)
- Select the best performing k value for high accuracy score
- Based on the distance what are the nearest neighbors points we are having


## PART 4 - Classification Metrics

### Task 6: Evaluation Metrics for Classification
- For Logistic Regression, Naive Bayes, and KNN using different metrics
1. Accuracy = Measures the overall percentage of correctly classified samples
2. Precision = Measures how many predicted positive samples were actually positive
3. Recall = Measures how many actual positive samples were identified
4. F1- Score = The Harmonic mean of precision and recall
5. Confusion Matrix = Maintain a ratio between correct predict values & wrong predicted values & correct values & wrong actual values
6. Classification Report = It is summary of classification model which give performance of model for every class
- Precision
- Recall 
- F1-Score
- Support


## PART 5 - Model Behaviour & Learning Concepts

### Task 7: Overfitting & Underfitting
A situation where with the (training data) model is providing less accuracy or seen data along with that at the time of testing as model is not well able to provide good predict.
1. Underfitting ---> when my model provides great accuracy model could not enough on training data
- Taining Accuracy ---> Low / Relatively low
- Model is too simple
- High bias
- The test accuracy is slightly higher than training accuracy , so it isnot a testbook underfitting pattern. model was intentionally made simple but the result it self doesnot strongly demostrate underfitting
- Training Accuracy = 84.43%
- Testing Accuracy = 88.76%

2. Overfitting ---> when my model learns the training data too well , including noise and unnecessary details
- Training Accuracy ---> Very high
- Testing accuracy --> lower
- Model is too complex
- High variance

- Training Accuracy = 100%
- Testing Accuracy = 74.08%

- Explain the Observed behaviour


Underfitting :
The simple decision tree has relatively lower training accuracy but performs well on the test data . In this particular dataset the test accuracy
is even slightly higher than training accuracy which can happen due to the particular train test split.

Overfitting :
The complex decision achieves 100% training accuracy meaning it has learned the training data extremely well . However its testing accuracy drops
to 74.08% showing that it does not generalize well to unseen data . this is a clear indication of overfitting


### Task 8: Bias & Variance (Conceptual)
1. What is bias in ML models?
- Bias is the error caused when a machine learning model makes overly simple assumptions about the data.
- High Bias ---> model is too simple
- it cannot capture important patterns
- usually leads to underfitting

2. What is Variance?
- Variance is the error caused when a model is too sensitive to the training data
- High variance ---> model is too complex
- it learns noise and unnecessary details from training data
- usually to overfit

3. How do bias and variance relate to underfitting and overfitting?
- Situation of underfitting
 Bias ---> High
 Variance ---> Low
 Result ---> Model too simple
- Situation of Good fit
 Bias ---> Low
 Variance ---> low
 Result ---> Good generalization
- Situation of Overfittin
 Bias ---> Low
 Variance ---> High
 Result ---> Model too complex  

4. How can we reduce Overfitting?
- Reducing model complexity ---> limit, Decision Tree depth
- Using more training data
- Regularization ---> such as L1 or L2 regularization
- Cross validation to select a suitable model
- Feature selection
- Pruning Decision Trees
- Early stopping in models that support it
- Using ensemble models such as Random Forest  

# How to run

Requirements
- Python 
- VS code or other code editor

Steps:
1. Open the folder in VS code
2. Open the required file
3. Click the run button or open the terminal and run