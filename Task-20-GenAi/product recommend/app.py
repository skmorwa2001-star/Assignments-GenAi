import streamlit as st
import pandas as pd
import nltk
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Product Recommendation System")

data=pd.read_csv("clean_products.csv", encoding="utf-8")

# Handle missing text values
data["clean_text"] = data["clean_text"].fillna("").astype(str)

# Remove rows with empty text (optional but recommended)
data = data[data["clean_text"].str.strip() != ""].reset_index(drop=True)

tfidf=TfidfVectorizer(stop_words="english")
tf_matrix=tfidf.fit_transform(data["clean_text"])

# Similarity
similarity=cosine_similarity(tf_matrix)

# product list
product_names=data["Product Name"].values

# Function for recommendation
def recommend(product_name, top_n=5):
    matches=data.index[data['Product Name']==product_name]
    if len(matches)==0:
        return []
    
    product_index=matches[0]

    similarity_scores=similarity[product_index]

    product_list=sorted(enumerate(similarity_scores),reverse=True,key=lambda x:x[1])[1:6]

    recommendations=[]

    for index, score in product_list:
        if index!=product_index:
            recommendations.append(data.iloc[index]['Product Name'])

        if len(recommendations) == top_n:
            return recommendations 

# Select box to select product
product_name=st.selectbox("Enter the product name", product_names)        

if st.button("Recommend"):
    r=recommend(product_name)

    st.write("The Recommended Products are : ")

    for i in r:
        st.write(i)