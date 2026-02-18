from flask import Flask, request, jsonify, render_template
from recommender import recommend

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def get_recommendation():
    movie = request.json.get("movie")
    result = recommend(movie)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
