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
