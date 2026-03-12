# Movie Recommendation System

This project implements two versions of a **content-based movie recommendation system** using machine learning techniques.  
The system recommends movies that are similar to a given movie based on their features.

The project demonstrates how recommendation systems can improve by incorporating richer information from datasets.

---

# Project Structure

```
movie-recommendation-system/
│
├── v1_genre_recommender/
│
├── v2_content_recommender/
│
├── requirements.txt
└── README.md
```

---

# Version 1: Genre-Based Recommender

Version 1 is a **simple content-based recommender** that suggests movies based only on their genres.

## Features Used

- Movie title
- Genres

## Method

1. Load movie dataset
2. Clean and preprocess genre data
3. Convert genres into numerical vectors using **CountVectorizer**
4. Compute similarity between movies using **cosine similarity**
5. Recommend movies with the highest similarity scores

## Example

Input:

```
recommend("Toy Story")
```

Output:

```
Toy Story 2
A Bug's Life
Monsters, Inc.
Finding Nemo
Cars
```

This version demonstrates the **basic concept of content-based filtering**.

---

# Version 2: Content-Based Recommender (Enhanced)

Version 2 improves the recommendation system by using **multiple movie features** instead of only genres.

## Dataset

This version uses the **TMDB 5000 Movie Dataset**, which contains rich movie metadata.

Files used:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

## Features Used

The recommender combines several attributes to represent each movie:

- Genres
- Keywords
- Movie overview (description)
- Cast (top 3 actors)
- Director

## Data Processing Pipeline

1. Load movie and credits datasets
2. Merge datasets using movie title
3. Extract useful information from JSON columns
4. Clean and normalize text features
5. Combine features into a single **tags** column

Example combined representation:

```
overview + genres + keywords + cast + director
```

## Vectorization

The text features are converted into numerical vectors using **CountVectorizer** from scikit-learn.

Each movie is represented as a vector in a high-dimensional space.

## Similarity Calculation

The system computes similarity between movies using **cosine similarity**.

Movies with the highest similarity scores are recommended.

## Example

Input:

```
recommend("Avatar")
```

Output:

```
Guardians of the Galaxy
John Carter
Star Trek
Aliens
The Fifth Element
```

Compared to Version 1, this version provides **more meaningful recommendations** because it considers the movie's story, cast, and themes.

---

# Technologies Used

- Python
- Pandas
- NumPy
- scikit-learn

---

# Future Improvements

Possible improvements for the project:

- Using **TF-IDF vectorization**
- Applying **stemming or lemmatization**
- Creating a **web interface using Streamlit**
- Adding **movie posters using the TMDB API**
- Deploying the recommender as a web application

---