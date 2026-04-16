import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

movies = movies.merge(credits, on="title")
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.dropna(inplace=True)

movies['title_lower'] = movies['title'].str.lower()


def get_names(text):
    items = json.loads(text)
    return [item["name"] for item in items]


movies["genres"] = movies["genres"].apply(get_names)
movies["keywords"] = movies["keywords"].apply(get_names)


def get_cast(text):
    items = json.loads(text)
    return [actor["name"] for actor in items[:3]]


movies["cast"] = movies["cast"].apply(get_cast)


def get_director(text):
    items = json.loads(text)
    for person in items:
        if person["job"] == "Director":
            return [person["name"]]
    return []


movies["crew"] = movies["crew"].apply(get_director)
movies["overview"] = movies["overview"].apply(lambda x: x.split())


def collapse(words):
    return [word.replace(" ", "") for word in words]


movies["genres"] = movies["genres"].apply(collapse)
movies["keywords"] = movies["keywords"].apply(collapse)
movies["cast"] = movies["cast"].apply(collapse)
movies["crew"] = movies["crew"].apply(collapse)

movies["tags"] = (movies["overview"] + movies["genres"] + movies["keywords"] + movies["cast"] + movies["crew"])
movies["tags"] = movies["tags"].apply(lambda x: " ".join(x))

cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(movies["tags"]).toarray().astype('float32')
similarity = cosine_similarity(vectors)


def recommend(movie):
    movie_query = movie.lower().strip()

    if movie_query not in movies["title_lower"].values:
        return ["Sorry, that movie is not in the dataset."]

    index = movies[movies["title_lower"] == movie_query].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]


class MovieRequest(BaseModel):
    prompt: str


@app.post("/predict")
async def predict_api(request: MovieRequest):
    recommendations = recommend(request.prompt)
    return {"recommendations": recommendations}