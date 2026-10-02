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

### Task 2: Basic Text Cleaning
Apply the following basic cleaning steps:

1. Convert text into lowercase
- use str.lower() -->  to convert uppercase to lowercase
2. Remove Punctuation
- use regular expression library
- re.sub(r"[^\w\s]","",text) its means...
     ^ --> not
     \w --> matches letters digits and underscore
     \s ---> matches whitespace characters as (spaces, tans, newlines)
3. Remove numbers
- re.sub(r"\d+","",text) its means 
     \d+ ---> finds one or more digits
     "" ---> replaces them with nothing
4. Remove extra whitspaces
- re.sub(r"\s+"," ",str(text)).strip()
     \s+ --> multiple spaces , tabs, newlines find
     " "  ---> replace single space
     .strip() --> for remove spaces of starting and ending of sentence
- Create a new columns as clean_text_basic
- Compare original text vs cleaned text              

## PART 2 - Advanced Text Cleaning

### Task 3: Removing Noise
Apply advanced cleaning techniques
1. Remove URLs
- URLs are removed by Regular expression
- use this (r'https?//\S+|www\.\S+',"",text) 
       https ----> matches with the url
       ?S ----> s is optional
       :// ---> matches the ://
       \S+ ----> matches characters inside the URL as the rest of the URL
       | --> or
       www\.\S+ ---> match URL starting with www.
2. Remove email addressess
- Use this pattern (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
           b[A-Za-z0-9._%+-] ---> word boundary for username
           @[A-Za-z0-9.-] ----> word boundary for domain
           \.[A-Za-z]{2,} ----> for extension minimium two words
3. Remove HTML tags
- Use the pattern (r'<.*?>',"",text)   
          <.*?> ---> only character is present
          "" ----> remove html tags replace unspace
4. Remove special characters and emojis
- Use the pattern --->
        "["
        u"\U0001F600-\U0001F64F" # EMOTICONS
        u"\U0001F300-\U0001F5FF" # SYMBOLS AND PICTOGRAPHS 
        u"\U0001F680-\U0001F6FF" # TRANSPORT AND MAP
        u"\U0001F1E0-\U0001F1FF" # FLASH 
        "]+",
        flags=re.UNICODE                   

- Store result in clean_text_advanced

### Task 4: Handling Stopwords
1. Load stopwords using NLTK
- from nltk.corpose import stopword
2. Remove stopwords from clean_text_advanced
- Use stopword.words('english) --> english stopwords
- apply if condition and remove stopwords present in text
- and store in a list without_stopword=[]
3. Save the output as text_no_stopwords

### Task 5: Handling Repeated Characters & Slang (Optional)
1. Normalize repeated characters
- Use '(.)\1{2,}',r'\1' its means
      . ---> character
      \1{2,} --> same character atleast 2 additional times
      r'\1' ---> only one character 
2. Create a dict of slang
- slang_dict={"u":"you","gr8":"great","btw":"by the way","pls":"please"}
3. Replace slang words
- sland_dict.get(word.lower(),word)
- Its replace dictionary if found else same as


## PART 3 - Basic Text Preprocessing in NLP

### Task 6: Tokenization
1. Perform word tokenization
- from nltk.tokenize import word_tokenize, sent_tokenize
- for word_tokenize --> divided into words tokens
2. Perform sentence tokenization
- for sent_tokenize --> divided into sentence tokens
3. Diplay tokens for atleast 3 text samples
- it shows the output

### Task 7: Stemming
1. Apply Porter Stemmer 
- from nltk.stem import PorterStemmer
- make list of some words with passing through the stem the give stemmed words
- for loop is used iterate over all list
2. Compare original words vs stemmed words
- compare the words list before and after of stem

### Task 8: Lemmatization
1. Apply wordnet lemmatization
- from nltk.stem import WordNetLemmatizer
- from nltk.corpus import wordnet
- Apply for all previous task words 
2. Compare stemming vs lemmization results
- print the results of both process

### Task 9: Final NLP Pipeline Creation
- Create a single function nlp_preprocess(text)
1. Lowercasing ---> text.lower() is convert all characters into lowercase
2. Noise Removal ---> re.sub(r'[^a-zA-Z\s]','',text) is used remove unnecssary charactersand spaces from dataset
3. Stopword removal ---> remove those with not any useful infomation for our NLP tasks
4. Tokenization --> individual words / sentences divides into tokens
5. Lemmatization ---> converts the words into base/dictionary words
- return ' '.join(tokens) ---> convert token list to sentence/string format


### Task 10: Observations & Insights
- Write short observations

1. Difference between basic and advanced cleaning
- Basic Cleaning ---> basic cleaning removes unwanted characters , lowercasing , punctuations , numbers , removes extra spaces , and formatting from text. It is simpler and faster .

- Advanced Cleaning ----> advanced cleaning goes further by processing the liguistic structure of text using techniques such as tokenization , stopwords removal , stemming , and lemmatization . Its produces text that is more suitable for NLP analysis and machine learning models

2. Why lemmatization is preferred over stemming.
- Lemmatization is preferred over stemming because it converts words into meaningful dictionary forms, while stemming may produce incomplete or meaningless words
- Why lemmatization preferred?
 i. Its preoduces meaningful words
 ii. We considers linguistic / Grammatical information
 iii. Its more accurate then stemming
iv. Its provides clearer and meaningful text for NLP model

3. Importance of preprocessing in NLP models
- NLP preprocessing means cleaning and transforming raw text into a suitable format before giving to a NLP or Machine learning model
- Why Important
- 1. Removes unnecessary data --> removes punctuations , special charcters , extra spaces , etc .
- 2. Reduces noise ---> makes the text cleaner by removing irrelevant information .
- 3. Standardize text ---> prevent the model from treating them a different words
- 4. Reduces vocubulary size ---> stopword removal and lemmatization can reduce the number of unique words
- 5. Improves model performance ---> clean and consistent input can help the model learn meaningful pattern more efficiently
- 6. Converts text into usable form ---> techniques like tokenization convert sentences into individual words / tokens that NLP algorithms can process
- 7. Improves computational efficiency ---> less unnecssary text means fewer features and potentially faster processing


link of dataset used in assignment is ---> https://www.kaggle.com/datasets/yasserh/amazon-product-reviews-dataset