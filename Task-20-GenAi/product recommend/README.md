# 🛍️ Product Recommendation System

A content-based Product Recommendation System built using Python, NLP, TF-IDF Vectorization, Cosine Similarity, and Streamlit. The application recommends similar products based on their cleaned textual descriptions.

## 📌 Project Overview

The Product Recommendation System helps users discover products similar to a selected product. It analyzes product text, converts it into numerical vectors using TF-IDF, and calculates similarity scores using Cosine Similarity.

The project provides a simple interactive web interface built with Streamlit.

## ✨ Features

- **Product Selection:** Select a product from the available dataset.
- **Text Processing:** Uses cleaned product text for analysis.
- **TF-IDF Vectorization:** Converts textual descriptions into numerical features.
- **Cosine Similarity:** Measures similarity between products.
- **Top Recommendations:** Displays up to five similar products.
- **Interactive Interface:** Provides a simple interface using Streamlit.
- **Missing Value Handling:** Replaces missing text values and removes rows with empty text.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorizer
- Cosine Similarity
- Streamlit

## 📂 Project Structure

```text
product-recommendation/
│
├── app.py
├── clean_products.csv
├── requirements.txt
└── README.md
```

**Dataset:** `clean_products.csv` contains the cleaned product information required by the application.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd product-recommendation
```

Replace `<your-repository-url>` with your GitHub repository URL.

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Ensure the requirements file includes the necessary libraries, such as:

```text
streamlit
pandas
scikit-learn
nltk
joblib
```

The current application imports these libraries, although NLTK and Joblib are not directly used in the recommendation logic.

### 4. Prepare the dataset

Place `clean_products.csv` in the same directory as `app.py`.

The CSV must contain these columns:

| Column | Description |
|---|---|
| `Product Name` | Name of each product |
| `clean_text` | Cleaned textual information used for similarity calculation |

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser to use the application.

## 🔍 How It Works

1. **Load Dataset:** Reads the cleaned product data from the CSV file.
2. **Handle Missing Values:** Replaces missing text with empty strings and removes rows with empty cleaned text.
3. **TF-IDF Vectorization:** Converts the cleaned text into numerical vectors.
4. **Similarity Calculation:** Calculates cosine similarity between product vectors.
5. **Product Selection:** Allows the user to select a product from a dropdown menu.
6. **Recommendation Generation:** Finds products with the highest similarity scores and displays the recommendations.

### Recommendation Workflow

```text
Cleaned Product Dataset
          ↓
Data Loading and Cleaning
          ↓
TF-IDF Vectorization
          ↓
Cosine Similarity
          ↓
User Selects a Product
          ↓
Find Similar Products
          ↓
Display Recommendations
```

## 🧠 Concepts Learned

- Text preprocessing for NLP
- Feature extraction using TF-IDF
- Vector similarity using Cosine Similarity
- Data manipulation with Pandas
- Building interactive applications with Streamlit
- Implementing a content-based recommendation system

## ⚠️ Limitations

- Recommendations depend on the quality and content of product descriptions.
- Products with similar textual descriptions are more likely to be recommended.
- The current implementation calculates a complete similarity matrix, which can consume substantial memory for large datasets.
- The system does not currently use customer ratings, purchase history, or collaborative filtering.
- The dataset must contain the required columns and be available when the application starts.

## 🚀 Future Improvements

- Add product images and descriptions to the interface.
- Display similarity scores alongside recommendations.
- Improve performance for large datasets.
- Add product category and price filters.
- Deploy the application online.
- Optimize model loading and text processing.

## 👨‍💻 Author

**Sunil Kumar**

AI & Machine Learning Student | Python Developer

GitHub: [skmorwa2001-star](https://github.com/skmorwa2001-star)

---

⭐ If you find this project useful, consider giving the repository a star!

