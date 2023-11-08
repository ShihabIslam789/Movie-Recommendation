#importing dependencies 

import numpy as np
import pandas as pd 
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# loading the data from the csv file to pandas dataframe

movies_data = pd.read_csv('movies.csv')

movies.data.head()

movies_data.shape


selected_features = ['generes','keywords','tagline','cast','director']
print(selected_features)

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')