# ----------------------- Assignment 16 -------------------------

### Assignment
- You will implement advanced ML algorithms understand model validation stragires apply ensemble learning

### This assignment covers:
- Support Vector Machine (SVM)
- Decision Tree Algorithms 
- Train vs Validation vs Test & Cross Validation
- Ensemble learning (Bagging and Boosting)
- Random Forest (Bagging)


## PART 1 - Advanced Supervised Learning

### Task 1 : Support Vector Machine (SVM)
- SVM is an Supervised ML Algorithm used for both classification & Regression which aims to find the optimal hyperplane that best(separates) data  points of different classes.

- Clean the dataset and handling the missing value by using ---> isnull(), info(), fillna()

1. Select the classification dataset 
- select the features which are important for our task only numerical features is selects

2. Split into train and test sets
- Separate the data into train and test purpose using from sklearn.model_selection import split_train_test
- Standardization of data because SVM is sensitive to feature scale

3. Train the SVM classifier using SVC
- passing the data to the model for training purpose
- from sklearn.svm import SVC

4. Experiment with the 
- SVC(kernel='linear',random_state=42) --> In this case it can separate multiple classes via a straight line

- SVC(kernel='rbf',random_state=42) --> there is a complex relationship between data pts

5. Compare accuracy of both kernels
- accuracy_score(Y_test,y_predict)

### Task 2: Decision Tree Algorithm
- Decision Tree is an Supervised learning algorithm used for both classification and regression tasks which models Decision as consequences & can be associated with it.

1. Train a decision tree classifier
- from sklearn.tree import DecisionTreeClassifier
- dt_model=DecisionTreeClassifier(random_state=42)
- dt_model.fit(X_train,Y_train)

2. Visualize the tree structure (depth limited)
- from sklearn.tree import plot_tree
- plot_tree() ---> passing differents parameters
- (dt_model , feature_name, class_name , filled , max_depth , fontsize)

3. Train models with Low max_depth (underfitting)
- low_model=DecisionTreeClassifier(max_depth=2, random_state=42)
- dt_model.fit(X_train, Y_train)
- Calculate accuracy_score

3. Train model with High max_depth (overfitting)
- high_model=DecisionTreeClassifier(max_depth=30, random_state=42)
- high_model.fit(X_train, Y_train)
- Calculate accuracy_score
- max_depth is important for archeving a good balance between learning and generalization

## PART 2 - Model Validation & Cross Validation

### Task 3 : Train vs Validation vs Test Split
1. The dataset was divided into three subsets 60% ---> for training, 20% ---> validation and 20% ---> testing set
2. A Decision tree model classifier was trained using the training set
- The max_depth parameter was tuned using the validation accuracy was selected as the best parameter 
- Training the Decision Tree classifier model to prediction of the output
3. Tune one simple parameter using validation set
- give differents values of max_depth to checks the prdiction of model changes when we passes differents value of of max_depth and decides the best output model which gives the best performance
4. Evaluate final model on test set
- when we decide which model is validation prediction best accuracy 
- then we use this max_depth value to predicts the final model performance

### Task 4 : Cross Validation
1. Apply K-Fold Cross Validation
- 5-Fold Cross Validation was applied to the decision tree model 
- the dataset was divided into 5 folds and each fold was used for validation once
2. Compute average accuracy
- the average of the five accuracies was calculate
3. Compute single train test accuracy vs cross validation accuracy
- cross validation gives a more reliable estimate of model performance than a single train test split


## PART 3 - Ensemble Learning

### Task 5 : Bagging vs Boosting (Conceptual + Practical)
1. Brief explain:
Bagging ----> Bagging is a ensemble method designed to enhance the stability and accuracy of machine learning models.
It works by training multiple base models independently on random subsets of the training data created through bootstrap sampling where data points are selected  with replacement. This means somes samples may appear multiple times in a subset while others may be excluded.

- It averge the prediction from multiple models bagging reduces the variability of individual models making the ensemble more robust
- Each sub-dataset has its own machine learning model (usually same type) has trains in parallel independently
- Combine multiple models generally leads to better prediction performance than a single model

Boosting ----> Boosting is a ensemble learning method where multiple weak learners typically models with high bias but low variance are trained sequentially . Each new learner focuses on correcting the errors made by the previous learners giving more weight to misclassified or difficult instances. The final model is a weighted combination of all base learners resulting in a strong model with improved predictive performance

- Sequentially combine weak learners helps correct underfitting and improves predictions
- Misclassified or difficult instances recevies more attention enhancing overall model performance
- Boosting achieves higher prediction accuracy than single models or some other esemble methods

2. Train
- from sklearn.ensemble import BaggingClassifier , AdaBoostClassifier
- n_estimators --> it a hyperparameters that controls number of trees or estimators used in the ensemble
- feed the data into model and train the model 
- prediction the model outcome

3. Compare their performance
- Bagging Classifier gives the accuracy of 79.4%
- AdaBoost Classifier gives the accuracy of 81.05%

### Task 6 : Random Forest (Bagging)
1. Train the Random Forest Classifier
- from sklearn.ensemble import RandomForestClassifier
- Feed the data in to model to predict the output
- rdc.fit(X_train,Y_train)
- check the performaces of model by the help of accuracy score
- accuracy_score(Y_test,y_pred_rdc)

2. Compute performace with Single Decision Tree , Bagging Classifier
- In task 2 we have the decision tree we use here and give the accuracy score of this model
- In task 5 we have train the bagging classifier model this model used give its accuracy score
- Use print function to give the prediction of different model

3. Print feature importance
- Random Forest Classifier provides a feature_importances_ attributes that shows how important each feature is for making predictions
- the feature importance was represented graphically using horizontal bar chart
- the graph helps identify which features contribute to the most in Random Forest prediction's

### How to Run
- Open the files in Jupyter Notebook or VS Code
- Place the dataset in the correct folder
- Run the cells sequently
- Check the Decision Tree visualization and accuracy comparsion
- Record the actual train and test accuracy values generated by the notebook


- Used dataset link ---> https://www.kaggle.com/datasets/meharshanali/student-dropout-prediction-dataset