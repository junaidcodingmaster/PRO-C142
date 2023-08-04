import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read articles.csv into DataFrame and drop NA values in the title column
articles_df = pd.read_csv("data/articles.csv").dropna(subset=["title"])

# Create count_matrix using CountVectorizer
count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform(articles_df["title"])

# Create cosine_sim classifier
cosine_sim = cosine_similarity(count_matrix, count_matrix)

# Reset indexes of DataFrame to the article's title
articles_df = articles_df.set_index("title")


# Function to get a recommendation based on the contentId of the article
def get_recommendation(contentId):
    if contentId not in articles_df.index:
        return []  # Return an empty list if the contentId is not found in the DataFrame
    idx = articles_df.index.get_loc(contentId)
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Get top 10 similar articles (excluding itself)
    recommended_articles = [articles_df.index[i] for i, _ in sim_scores]
    return recommended_articles
