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


## PART 4 - TF-IDF Vectorization

### Task 7: TF-IDF Implementation
- from sklearn.feature_extraction.text import TfidfVectorizer
1. USe TfidfVectorizer
- tf=TfidfVectorizer()
2. Fit and transform the dataset
- tf.fit_transform(texts)
3. Display:
- Vocabulary ---> tf.get_feature_names_out()
- TF-IDF matrix shape ----> tf.idf_

### Task 8: BoW vs IF-IDF comparsion
- from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer
1. Compare word weights for common words
- bow_matrix=bow.fit_transform(texts)
- tf_matrix=tf.fit_transform(texts)
2. Identify:
- Words with high TF-IDF ---> its means the words which less repeat in files/Documents and give a meaningful
in the document

- Word with low TF-IDF ---> its means the words which more repeats in the files and documents 
3. Explain why TF-IDF down-weights common words
- TF-IDF are two components:
       
         TF(t,d) = frequency of term t in document d

         IDF(t) = log(N/df(t))

         where,
         - N = total number of documents
         - df(t) = number of documents containing the word

- If any words repeated in each document its not helpful to create any difference identify
so its IDF is low
- If any not repeated in each document then its IDF is higher 

## PART 5 - Practical Insights

### Task 9 : Vectorizer Parameter Exploration
- Experiment with:
1. Max_features --> set the vocabulary max limit
2. min_df ---> remove those words which are less in documents
3. max_df ---> remove those words which more repeats in documents

- Observe how vocabulary size changes
   - max_features=5 ---> keeps at most 5 features --> limits vocabulary size to 5
   - min_df=2 ---> keeps words appearing in at least 2 documents ---> Removes very rare words
   - max_df=0.6 ---> removes words appearing in more than 60% of documents ---> Removes overly common words

### Task 10 : Practical Questions
1. Difference between one-hot encoding and BoW?
- One-hot Encoding ---> it is a type of text vectorization where we convert the text into vectors such that every unique 
word while have their corresponding vector

- BoW ---> Bag of words as the name states , here we are looking for words counts 
 we check the given word in the given document if that how many times it is getting repeated

Example - sent --> AI is useful and AI is powerful
               -> one-hot encoding : Each word has its different vector
               -> BoW : AI=2, is=2, useful=1, and=1, powerful=1 

2. Why do N-gram increase dimensionality?
- In N-gram rather than taking a unique word in the vocabulary we take the sequence of words in the vocabulary

Example: machine learning is useful
     -> unigrams : machine , learning, is , useful
     -> bigrams : machine learning , learning is , is useful 
     -> trigram : machine learning is , learning is useful

As the n-gram size increases as vocabulary word combinations adds and its helps in increase features and vector dimensions     

3. When should we prefer TF-IDF over BoW?
- TF-IDF is prefer when we give higher weight of important and distinctive words

Example: Document search , information retrieval and text classification its use TF-IDF because common words has less influence

- BoW is useful when we need simple word counts

4. Limitations of count-based vectorization?
- No semantic understanding : not related the similar words meaning
- High dimensionality : as large vocabulary as vectors size increase
- Spare representation : most vectors value is zero
- word order loss : basic word sequence has preserve
- Synonym problem : happy and joyful has not automatically similar understandin