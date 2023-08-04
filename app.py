import csv
from flask import Flask, jsonify, request
from data.storage import articles, liked_articles, not_liked_articles
from data.demographic_filtering import output
from data.content_filtering import get_recommendation

app = Flask(__name__)

# Import articles.csv and read all the data
articles_file = "data/articles.csv"
with open(articles_file, "r") as file:
    reader = csv.DictReader(file)
    all_articles = list(reader)

# Add the header "id" before the first comma in the first line
with open(articles_file, "r") as file:
    lines = file.readlines()
    lines[0] = "id," + lines[0].split(",", 1)[1]
    with open(articles_file, "w") as updated_file:
        updated_file.writelines(lines)


# Create the first GET request to get the first article
@app.route("/get_article", methods=["GET"])
def get_article():
    if len(all_articles) > 0:
        return jsonify(all_articles[0])
    else:
        return jsonify({"message": "No articles remaining."})


# Create the second POST request to mark the article as liked
@app.route("/like_article", methods=["POST"])
def like_article():
    if len(all_articles) > 0:
        article = all_articles.pop(0)
        liked_articles.append(article)
        return jsonify({"message": "Article liked successfully."})
    else:
        return jsonify({"message": "No articles remaining."})


# Create the third POST request to mark the article as not liked
@app.route("/not_like_article", methods=["POST"])
def not_like_article():
    if len(all_articles) > 0:
        article = all_articles.pop(0)
        not_liked_articles.append(article)
        return jsonify({"message": "Article marked as not liked."})
    else:
        return jsonify({"message": "No articles remaining."})


# Create a GET API to return the list of popular articles
@app.route("/popular_articles", methods=["GET"])
def get_popular_articles():
    return jsonify(output.to_dict(orient="records"))


# Create another GET API to return the list of recommended articles
@app.route("/recommended_articles/<string:contentId>", methods=["GET"])
def get_recommended_articles(contentId):
    recommendations = get_recommendation(contentId)
    return jsonify(recommendations)


# Run the Flask app
if __name__ == "__main__":
    app.run()
