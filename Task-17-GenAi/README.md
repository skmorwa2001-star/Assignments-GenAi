# ------------------------ Assignment 17 : Test Cleaning, Preprocessing & NLP Pipeline --------------------------

## Assignment
- Before building any NLP or GENAI model , raw text data must be cleaned and preprocessing properly. in this assignment we will build a complete NLP preprocessing pipeline starting from raw text to model ready text
 
## This assignment focuses on :
1. NLP Pipepline & Basic text cleaning
2. Advanced text cleaning
3. Basic text preprocessing techniques 

## PART 1 - NLP Pipeline & Text Cleaning

### Task 1: Understanding Raw Text Data
1. Load the text dataset using pandas ---> pd.read_csc()
- analysis the dataset and make a relevant for our assignment 
- from dataset we only create a reviews colunns in which we added the 'reviews.title+reviews.text+reviews.URLs' columns to make relevant columns for our assignment
2. Print:
- First 5 text samples ---> data.head(5)
- length of each text ---> data['reviews'].str.len()
3. Identify common issues in raw text suxh as:
- Analysis the dataset and check the dataset-
- punctuation marks
- Uppercase/ lowercase mismatch
- numbers
- extra spaces



link of dataset used in assignment is ---> https://www.kaggle.com/datasets/yasserh/amazon-product-reviews-dataset