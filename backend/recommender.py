import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

df = pd.read_csv("backend/data/movies.csv")

df["tags"] = df["overview"] + " " + df["genres"]

cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(df["tags"]).toarray()

similarity = cosine_similarity(vectors)

pickle.dump((df, similarity), open("backend/model/model.pkl", "wb"))

def recommend(movie):
    df, similarity = pickle.load(open("backend/model/model.pkl", "rb"))

    movie = movie.lower()
    if movie not in df["title"].str.lower().values:
        return ["Movie not found"]

    idx = df[df["title"].str.lower() == movie].index[0]
    distances = similarity[idx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movies_list:
        recommendations.append(df.iloc[i[0]].title)

    return recommendations

if __name__ == "__main__":
    print("Model created")
