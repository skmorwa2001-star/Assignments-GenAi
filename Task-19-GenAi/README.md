# --------------------------------- Assignment 19 : Word2Vec Text Embeddings ----------------------

## Problem
- in this assignment we will understand Word2Vec techniques , neural network intuition and train a Word2Vec model on your own text data

## Assignment covers:
- Word Embeddings
- Word2Vec overview
- CBOW & skip gram techniques
- Neural network intuition behind Word2Vec
- Training Word2Vec on custom data

## PART 1 - Introduction to Word Embeddings

### Task 1 : Understanding word embedding (Conceptual)
1. What are word embeddings ?
- Word embeddings are numerical representations of words in the form of dense vectors that capture their meanings and relationship.
- They help computers understand similarities between words in Natural Language Processing (NLP)

Example : 
       - king  --->  [0.8 , 0.3 , 0.4]
       - queen --->  [0.7 , 0.4 , 0.2]
       - apple  ---> [0.1 , 0.9 , 0.6]

- king , queen may have similar vector representations because their meanings are related       

2. Why one-hot and bow fail to capture semantics ?
- One-Hot Encoding and Bag of Words (BoW) fail to capture semantics because they represent words using binary values
or word counts without understanding their meanings or relationships

Example : 
         - I like a car
         - I like a automobile

- Although car and automobile have similar meanings, one-hot encoding and BoW treat them as separate words and do not
automatically recognize their semantic similarity         

3. How word embeddings solve these problems ?
- Word embeddings solve these problems by representing words as dense numerical vectors that capture semantic meaning and relationships between words
- Words with similar meanings have similar vector representations


## PART 2 - Word2Vec Overview & Techniques

### Task 2 : Word2Vec Overview
1. Explain what Word2Vec is ?
- Word2Vec is a popular NLP technique that converts words into dense numerical vectors called word embeddings.
- It learn semantic relationships between words by anaalyzing their surrounding context in a large text corpus

2. Explain the idea of predicting words from context ?
- word prediction fron context is the process of predicting a word based on the surrounding words in a sentence
- Word2vec uses this idea to learn word embeddings and capture relationships between words

Example : sent ---> The cat drinks ___ .
                  -> the model may predict "milk" because it frequently appear in a similar context

3. Define:
- Vocabulary : Vocabulary is the collection of all unique words present in a text corpus uses to train an NLP model

Example : I like AI and I like ML
Vocabulary : {I , like , AI , and , ML}

- Context Window : Context window is the number of surrounding words considered by a model to learn or predict a target word

Example : The cat drinks milk
If the target word is drinks and the window size is 1 the context words are cat and milk

- Embedding Dimensions : Embedding dimensions refers to the number of numerical values used to represent a word as a vector

Example : if the embedding dimension is 3:
   king --> [0.5 , 0.4 , 0.8]
   the word king is represent using 3 numerical values                  