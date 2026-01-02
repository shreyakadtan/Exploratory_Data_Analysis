# NETFLIX EXPLORATORY DATA ANALYSIS (EDA)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Initial exploration
print("Dataset Shape:", df.shape)
print("\nDataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# Data cleaning
df['director'].fillna('Not Available', inplace=True)
df['cast'].fillna('Not Available', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df.drop_duplicates(inplace=True)

# Movies vs TV Shows
plt.figure(figsize=(6,4))
df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# Content added over the years
df['year_added'] = df['date_added'].dt.year
plt.figure(figsize=(8,5))
df['year_added'].value_counts().sort_index().plot()
plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

# Top 10 content producing countries
country_count = df['country'].str.split(',').explode().value_counts().head(10)
plt.figure(figsize=(8,5))
country_count.plot(kind='bar')
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.show()

# Top 10 genres
genre_count = df['listed_in'].str.split(',').explode().value_counts().head(10)
plt.figure(figsize=(8,5))
genre_count.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

# Rating distribution
plt.figure(figsize=(8,5))
sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index)
plt.title("Rating Distribution on Netflix")
plt.show()

# Movie duration analysis
movies = df[df['type'] == 'Movie'].copy()
movies['duration'] = movies['duration'].str.replace(' min','', regex=False)
movies['duration'] = pd.to_numeric(movies['duration'], errors='coerce')

plt.figure(figsize=(8,5))
sns.histplot(movies['duration'], bins=30)
plt.title("Movie Duration Distribution")
plt.xlabel("Duration (minutes)")
plt.show()

# Final insights
print("\nKEY INSIGHTS:")
print("1. Movies dominate Netflix content compared to TV Shows.")
print("2. Netflix content growth increased significantly after 2015.")
print("3. USA and India are the top content-producing countries.")
print("4. Drama and Comedy are the most popular genres.")
print("5. Most content is rated TV-MA and TV-14.")
print("6. Most Netflix movies are between 80 and 120 minutes long.")
