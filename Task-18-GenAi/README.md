# ------------------- Assignment 18 : Text Vectorization Techniques ----------------------------

## Assignment ---> After cleaning and preprocessing the text , the next cruical step is to convert text into numerical form so that machine learning models can understand it.

### This assignment covers -
- One-Hot encoding(Text)
- Bag of words (BoW)
- N-grams
- TF-IDF vectorization

## PART 1 - One-Hot Encoding (Text level)

### Task 1: Manual One-Hot Encoding
1. Select 5 short sentences
- sentences=data['final_clean_text'].dropna().iloc[:5].tolist()
    dropna() --> it is used to remove missing values
    iloc[:5] ---> it is used to select first 5 values
    tolist() ---> convert the pandas series into a normal python list
- used loop to print sequences of the sentences  
- enumerate gives us the 1 means numbering start from 1 instead of 0  
2. Build vocalubary of unique words
- vocalubary=sorted(set(word for sentence in sentences for word in sentence.split()))
    sentence.split() ---> it separates the sentence into individual words
    for word in sentence.split() ---> take each word from the sentence
    set() --> it is used to removes duplicates every words appears once
    sorted() ---> arranges the vocalubary alphabetically
3. Create a one-hot encoded matrix manually using python lists
- create a list one_hot_vectors=[]
- if word is present in words then assign it 1 or not present then 0
- and store in empty list --> one_hot_vectors.append(vector)
4. Display:
- vocabulary ---> print(vocalubary)
- One-hot ---> one_hot_dff

### Task 2: One-Hot Encoding Using Scikit-learn
1. Use countvectorizer(binary=true)
- cv=CountVectorizer(binary=True) ---> binary if True all non zero counts are set to 1. the default is False
2. cv.fit_tranform().toarray() ---> it fit the data and convert into encoded matrix form
  - toarray() ---> to convert the data into array form
3. Print:
- vocabulary ---> cv.vocabulary_  ---> gives the vocabulary words
- print the encoded_matrix


## PART 2 - Bag of Words (BoW)

### Task 3 : Bag of Words representation
- Takes all available cleared reviews data
1. Use CountVectorizer()
- bow=CountVectorizer()  ---> Creates the Bag of Words converter
2. Fit on the entire dataset
- fit ---> learns all unique words inn the dataset
3. Tranform text into BoW vectors
- transform ---> converts every review into numerical word count vectors
4. Display:
- Display the length of vocabulary size
- sample of feature vectors or matrix table

### Task 4 : Understanding word frequency
1. Calculate total frequency of each word
- bow.get_feature_names_out() ----> gets vocubulary words
- bow_matrix.sum() ---> sum of total frequency
2. Identify
- .sort_values() ---> arange the frequency in desending value
- also least frequent words of all the frequency_df
3. Explain how BoW captures frequency information?
- The Bag of Words (BoW) model captures frequency information by converting text into numerical vectors where each dimension represents a known word, and the value in that dimension represents how many times that word appears. It throws away all grammar , context ,and word order treating the document like a literal bag of disconnected words
- 1. Vocubulary building
- 2. Vector initialization
- 3. Frequency Counting

### Task 5 : Unigrams, Bigrams, & Trigrams
- from sklearn.feature_extraction.text import CountVectorizer
1. Create BoW using:
- unigram(ngram_range=(1,1)) , bigram(ngram_range=(2,2)) , trigram(ngram_range=(3,3))
- matrix=unigram.fit_tranform(texts)
- vocabulary=unigram.get_feature_names_out()

2. Compare
- vocabulary size ---> len(vocabulary)
- sample feature vectors ---> matrix[:5].toarray()

### Task 6 : Combined N-Grams
1. USe ngram_range=(1,2)
- CounterVectorizer(ngrma_range=(1,2))
2. Observe the unigrams and the output in this process comes
- Its shows the exact difference between them
