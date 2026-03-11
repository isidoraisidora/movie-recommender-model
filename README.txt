Movie Recommendation System

Overview

This project implements a **content-based movie recommendation system** using Natural Language Processing (NLP). The system recommends movies that are similar to a movie selected by the user based on their content features.

Instead of relying on ratings from other users, the model analyzes movie metadata (in this case mainly **genres**) and finds movies that share similar characteristics.

---

How the Model Works

1. Data Preprocessing

The movie dataset is cleaned and prepared by:

* Removing unnecessary columns
* Cleaning movie titles
* Removing the year from movie titles
* Preparing genre information for analysis

2. Text Vectorization

The genre information is converted into numerical vectors using **TF-IDF (Term Frequency–Inverse Document Frequency)**. This method transforms text data into numbers so that it can be processed by machine learning algorithms.

3. Similarity Calculation

To determine how similar two movies are, the system computes **cosine similarity** between their TF-IDF vectors. Movies with higher similarity scores are considered more related.

4. Generating Recommendations

When a user enters a movie title:

1. The system finds that movie in the dataset.
2. It calculates similarity between that movie and all others.
3. It returns the most similar movies as recommendations.

---

Example

Input:

recommend("Toy story")

Example Output:

Toy story 2
Monsters, inc.
A bug's life
Finding nemo

These movies are recommended because they share similar **genres and themes**.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook

---

## Project Structure

MovieRecommendationSystem/

data/
movies.csv

notebook.ipynb
recommender.py
requirements.txt
README.md

---

How to Run

1. Clone the repository

git clone https://github.com/isidoraisidora/movie-recommender-model.git

2. Install dependencies

pip install -r requirements.txt

3. Run the recommender system in Python

recommend("Toy story")

---
Future Improvements

Possible improvements include:

* Adding movie descriptions and keywords
* Implementing collaborative filtering
* Building a hybrid recommendation system
* Creating a web interface using Streamlit
* Integrating movie posters using external APIs

---

Learning Goals

This project demonstrates important machine learning and data science concepts:

* Natural Language Processing
* Feature engineering
* Vector similarity
* Content-based recommendation systems
