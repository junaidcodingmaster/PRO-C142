import numpy as np
import pandas as pd

# Read articles.csv into DataFrame
articles_df = pd.read_csv("data/articles.csv")

# Sort the rows based on total_events column in ascending order
articles_df = articles_df.sort_values(by="total_events", ascending=True)

# Create output with top 20 rows
output = articles_df.head(20)
