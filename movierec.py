#importing dependencies 

import numpy as np
import pandas as pd 
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# loading the data from the csv file to pandas dataframe

movies_data = pd.read_csv('movies.csv')

# prints the first 5 rows if the dataframe
movies.data.head()

# total amount of rows and columns
movies_data.shape

#select specific features
selected_features = ['generes','keywords','tagline','cast','director']
print(selected_features)

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')