# ---------- Assignment 14 -----------

## Assignment 
- After cleaning and exploring the data, the next critical step to prepare features correctly so that machine learning models can learn effectively

## In this assignment 
- Feature Engineering
- Feature Encoding 
- Feature Scaling
- Building an end to end Scikit learn Pipeline

## PART A - Feature Engineering

#### Task 1: Creating New Features
1. Identify at least 2 existing columns from dataset
2. Create new meaningful features
- column of price per unit is already in given dataset as 'original_price'
- Total Value is create of ('original_price'+'stock_quantity')
- The dataset does not contain an age column so the Age Group feature cannot be created . Therefore this feature is skipped
- Create a def which define the category of revenue as (0-999) as low, (1000-4999) as median, (5000-9999) as high, (more than 10000) as very high
- Create a new column of Revenue Category


#### Task 2: Handling Date & Text Features 
1. Date column - Extract yeat, month, dat
- from dataset has a purchase_date column which in object type then convert it into datetime type ---> pd.to_datetime() - if in data any error then apply (errors='coerce)
- Extract year , month , day information and create new columns of it
- By data['Month Year']=data['purchase_date'].dt.year
- data['Month Month']=data['purchase_date'].dt.month_name() --> month_name() used for name of month instead of number of month
- data['Month Day']=data['purchase_date'].dt.day

2. Text column - Extract length of text or word count
- Brand column used
- brand text length calculated by using str.len() method
- brand word count calculated by using str.split() 

- fillna('') is used to missing brand value dont show cause error while calculating text features



## PART 2 - Feature Encoding

#### Task 3: One-Hot Encoding
- For the given dataset we have identify categorical columns so that it understandable for machine to proced it
- It create a separate binary columns
1. Identify categorical columns - columns in which no pattern oberserved
2. Apply one hot encoding using --> pd.get_dummies() --> pass parameter(data,columns)
3. Display the transformed dataframe

#### Task 4: ColumnTransformer
- Check missing value
- If any missing value then handling missing value first
1. Separate: 
- Numerical features ---> all numerical columns
- Categorical features ---> all categorical columns
2. Use Columns Transformer
- Import all important encoders ---> OneHotEncoder, OrdinalEncoder, LabelEncoder, ColumnTransformer
- OneHotEncoder ---> apply to categorical columns
- OrdinalEncoder ---> apply to column in patten forms
- Pass numerical columns unchanged
3. Fit and transform the dataset
- Divide the data input and output data
- then fit_transform() apply to change data into machine easily understandable form

## PART 3 - Feature Scaling

#### Task 5: Standardization (StandardScaler)
- Select the numerical columns
- import StandardScaler as ss
1. Apply StandardScaler to numerical columns
- ss.fit_transform(numerical_cols)
2. Standardization ---> It is a type of feature scaling is done to keep all value in a Standard Scale Range.
StandardScaler transforms numerical features so that their mean becomes approximate 0 and standard deviation becomes approximate 1
it uses the formula:
      
      z= (x-mean)/standard deviation

      the value of z called as scaled value


#### Task 6: Normalization (MinMaxScaler)
- Select numerical columns
- import MinMaxScaler as mm
1. Apply 
- value.scaled=mm.fit_transformer(numerical_cols)
2. Display   value_scaled
3. StandardScaler:
- Mean approxmate to 0 & Standard deviation is approxmate 1
- It also contains negative values
- Uses mean & standard deviation 

MinMaxScaler:
- Minimum is 0 & Maximum is 1
- It contains values between 0 to 1
- Uses Minimum & Maximum    


## PART 4 - Building ML Pipeline

#### Task 7: Create a Preprocessing Pipeline
- Separate Data into multiple cateegories ---> Numerical_Data, Nominal_Data, Ordinal_Data
- import libraries --> Pipeline, OneHotEncoder, SimpleImputer, OrdinalEncoder, StandardScaler
1. Create Separate pipelines:
- Numerical_Pipeline=Pipeline(steps[(imputer),(scaling)])
- Ordinal_Pipeline=Pipeline(steps[(imputer),(encoding),(scaling)])
- Nominal_Pipeline=Pipeline(steps[(imputer),(scaling)])
2. Combine them using ColumnTransformer
- Import ColumnTransformer
- features=ColumnTransformer(transformer[(Numerical Transformation),(Ordinal Transformation),(Nominal Transformation)])

#### Task 8: Full Scikit learn Pipeline
1. Create a complete pipeline using scikit learn library
- import features from previous task
2. Raw Data ---> Encoding ---> Scaling ---> Model
3. Use simple model: LinearRegression or LogisticRegression
- Import LogisticRegression
- model=Pipeline(steps=[(features),(classifier)])
4. Split data into train test split
- import train_test_split library
- Divide data into Input Or Output data ---> X , Y
- train_test_split(X,Y,test_size=0.2)
5. Fit the pipeline on training data
- model.fit(X_train,Y_train)
6. Make prediction on test data
- Y_predict=model_predict(X_test)
- Check accuracy_score
- accuracy_score(Y_test,Y_predict)


#### Task 9: Pipeline Benefits
1. Why pipelines are important in ML?
- Pipelines combine preprocessing and model training into a single workflow . They make ML processes organized , consistent, and easier to reproduce.

2. What problems do pipelines solve?
- Pipelines help solve: -> Repeated preprocessing steps
                       -> Data Leakage
                       -> Inconsistent transformations between training and testing data
                       -> Manual errors
                       -> Difficult to maintain ML workflows
3. Difference between manual preprocessing vs pipeline based preprocessing?
- Manual Preprocessing:
-> Steps are preformed separately
-> More chances of errors
-> Data leakage can happen easily
-> Difficult to reproduce
-> More code and maintenance

- Pipeline Based Preprocessing
-> Steps are combined into one workflow
-> Fewer manual errors
-> helps prevent data leakage
-> easy to preproduce
-> Cleaner and easier to maintain


## How to Run

#### 1. Clone the Repository
- get clone <https://github.com/skmorwa2001-star/Task-14-GenAi>

#### 2. Install Dependencies
- pip install pandas numpy sckit learn matplotlib seaborn

#### 3. Open the notebook
- Open ass_14.ipynb in jupyter Notebook or VS Code

#### 4. Run the notebook
- Run the cells from top bottom


## Dataset Links
- Product data --->   https://www.kaggle.com/datasets/pratyushpuri/retail-fashion-boutique-data-sales-analytics-2025 