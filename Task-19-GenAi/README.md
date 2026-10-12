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