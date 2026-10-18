# Assignment 20 : Building & Deploying a Recommendation System

## Problem
- Task is to build a content based recommendation system starting from raw data preprocessing, performing text vectorization , generating recommendations and finally deploying the application on render by connecting it to github using git

## PART 1 - Data Preprocessing

### Task 1: Load & Understand Dataset
1. import pandas as pd
- pd.read_csv()
2. print:
- dataset shape ---> data.shape
- columns names ---> data.columns
- first 5 rows ---> data.head(5)
- data info ---> data.info()
- data.describe()
3. identify text columns used for recommendations
- select important columns of text for NLP preprocessing


### Task 2: Text Preprocessing for Recommendation
- Apply the following steps on the text column
1. convert text to lowercase
- data.str.lower() ---> it is used for to convert into lowercase the text
2. Remove punctuation and special characters
- create a def for to remove punctuation and special characters
- re.sub(r"[^\w\s]",'',text) 
3. remove stopwords
- create a def to remove stopwords
- and apply conditions which remove the stopwords from the data
4. Remove missing values 
- remove missing values from the data

- store cleaned text into clean_text column


## PART 2 - Text Vectorization

### Task 3: Vectorization using TF-IDF



### Dataset Details
Dataset Name - amazon-product-data-2020
Dataset link - https://huggingface.co/datasets/calmgoose/amazon-product-data-2020/tree/main