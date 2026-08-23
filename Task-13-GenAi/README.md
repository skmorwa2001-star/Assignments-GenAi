# ----------Assignment 13 : Data Gathering, Preprocessing & EDA----------

## Assignment
- Before building any ML model , your responsibility is to collect data from multiple sources , clean and preprocess it and perform Exploratory Data Analysis (EDA) to understand patterns , issues, and insights in the data.

## Assignment focuses on pre ML foundations
1. Data gathering from different sources
2. Data preprocessing & Cleaning
3. Exploratory Data Analysis (EDA)


## Part 1 -- Data Gathering 

#### Task 1: Load data from CSV
1. Download any dataset from kaggle link - ("https://www.kaggle.com/datasets/paramvir705/netflix-dataset")
2. Load data ---> pd.read_csv()
3. Print:
- Shape of dataset ---> .shape
- Columns names  ---> .columns
- first 5 rowa ---> .head()
- other techniques ----> .info(), .describe(), .dtypes  ....

#### Task 2: Load data from JSON
1. Download a small JSON file
- link of dataset --> ("https://www.kaggle.com/datasets/pratyushpuri/retail-fashion-boutique-data-sales-analytics-2025")
2. load using pandas ---> pd.read_json()
3. Convert into a Dataframe
4. Print the DataFrame 

#### Task 3: Load data from SQL Database
- Import sqlite3
1. Create a SQLite database named as sample.db
- Connect with the sample.db ---> sqlite.connect('sample.db')
2. Created an employees table ---> index ---> id , name, department, salary
3. Inserted 5 employes records
4. Loaded the table into a pandas DataFrame name using an SQL query ---> pd.read_sql_query()
5. Displayed the DataFrame
6. Closed the database connection

#### Task API Mini Project (TMDB API)
#### Mini Project: Movie Data Collector
- API Used ---> TMDB (The Movie Database) API
- Purpose ---> API is used to collect popular movie data
- Authentication ---> Bearer Token
- Endpoint ---> https://api.themoviedb.org/3/movie/popular

1. Create a free account on TMDB
2. Generate an API Key
- API Used ---> TMDB (The Movie Database) API
- Purpose ---> API is used to collect popular movie data
3. Using requests library ---> import requests
- use ---> requests.get() ---> send a request to the TMDB API and receives data
- Popular movies data
- Extacts field: Movie title, Release data, Rating, Popularity, Vote Count, Vote Average 
4. Convert the API response into Pandas DataFrame  ---> pd.DataFrame()
5. Save the collected data into tmdb_movies.csv


## Part 2 -- Data Preprocessing & Cleaning (Kaggle Dataset)

#### Task 5: Understanding the data
- check dataset shape ---> .shape
- display column data types ---> .info()
- Identify numerical and categorical columns
- Check missing values ---> .isnull()
- Rest techniques  ---> .dtypes , .describe() ....


#### Task 6: Data Cleaning 
1. Handle missing values ----> .isnull().sum()
- fill missing numerical values with median or mean
- fill missing categorical values with 'Unknown'
2. Remove duplicate rows ----> .duplicated()
3. Rename columns to lowercase - .columns(str.strip().str.lower().str.replace(" ","_"))
--> str.strip() ---> Remove extra spacing
--> str.lower() ---> Convert into lowercase
--> str.replace ---> Remove spacing between them and insert "_" in it
4. Fix incorrect data types --> .astype()
--> In given dataset only one incorrect datatype ---> date_added ---> pd.to_datetime() ---> to convert into datetime data type


#### Task 7: Feature Preparation
- Feature Selection ---> select the specific columns which is used
1. Convert categorical columns to numerical 
- Label Encoding converts each category into a unique integer value . It is useful for binary or ordinal categorical data but may introduce an artifical order between categories
  - import LabelEncoder
  - le=LabelEncoder()  
  - data['columns_name']=le.fit_transform(data['columns_name'])
- One hot Encoding creates a separate binary column for each category . It avoids introducing any order among categories and is preferred for nominal categorical features
  - pd.get_dummies() ---> It is used to perform one hot encoding by converting categorical variables into multiple binary columns so that machine learning model can use them without assuming any order between categories

2. Separate features and target column
- X as the input data (except type)
- Y aas the output data (type)


## Part 3 - Exploratory Data Analysis (EDA)

#### Task 8: Univariate Analysis
1. Plot distribution of numerical columns ---> sns.histplot(data=df,x='col_name',kde=True)
2. Count plot for categorical columns ---> sns.countplot(data=df,x='cat_col')
3. Identify outliers using boxplots ----> sns.boxplot(data=df,x='col_name')
4. Show Every Chart possible
- sns.stripplot()
- sns.violinplot()
- sns.rugplot()


#### Task 9: Bivariate Analysis
1. Numerical vs Numerical
- sns.scatterplot()
- sns.heatmap()
2. Categorical vs Categorical
- sns.barplot()
- sns.boxplot()
- sns.countplot()
- sns.violinplot()
- sns.pointplot()


#### Task 10: Insights & Observations

1. Most Netflix titles were released after 2015
2. Movies are most common than TV shows
3. The United States has the highest number of titles
4. Older release year appear as outliers in the box plot
5. Most content is concentrated between 2015 and 2021
6. Missing values were cleaned successfully
7. The final dataset is clean and ready for analysis



### Kaggle Dataset links
- Netflix dataset
   https://www.kaggle.com/datasets/paramvir705/netflix-dataset

- Product dataset
  https://www.kaggle.com/datasets/pratyushpuri/retail-fashion-boutique-data-sales-analytics-2025
