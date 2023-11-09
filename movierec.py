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

# replacing the null values with null string
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# combining all the 5 selected features

combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

print(combined_features)

# converting the text data to feature vectors

vectorizer = TfidfVectorizer()