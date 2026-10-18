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
1. Use Tfidfvectorizer to convert text into vectors
2. set parameters as max_range ---> maximium features setect limit
- ngram_range=(1,2) --> unigram and bigram both considers
- fit_transform ---> vocabulary understands and text converts into numerical vectors
3. print
- matrix.shape

### Task 4: Similarity Computation
1. Compute cosine similarity between all items
- from sklearn.metrics.pairwise import cosine_similarity
2. Store similarity matrix
- similarity_matrix=cosine_similarity(data)

3. Explain brief why cosine similarity is used
- Cosine similarity measures the angle between the vectors
- it is useful in recommendation because it primarily used to give pattern/ direction comparision ratheer than length of documents


### Dataset Details
Dataset Name - amazon-product-data-2020
Dataset link - https://huggingface.co/datasets/calmgoose/amazon-product-data-2020/tree/main