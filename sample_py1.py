import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample car data (include price information)
data = pd.DataFrame({
   'CarID': [1, 2, 3, 4, 5],
   'Make': ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Tesla'],
   'Model': ['Camry', 'Civic', 'F-150', 'Malibu', 'Model 3'],
   'Year': [2020, 2021, 2019, 2022, 2023],
   'Description': [
       'A midsize sedan with excellent fuel efficiency.',
       'A popular compact car known for reliability.',
       'A full-size pickup truck with powerful engine options.',
       'A comfortable midsize sedan with good safety features.',
       'An electric sedan with advanced technology.'
   ],
   'Price': [25000, 22000, 35000, 24000, 40000]  # Add car prices here
})

# User preferences (replace with user input)
user_preferences = {
   'Budget': 25000,
   'BodyType': 'Sedan',
   'FuelEfficiency': 'Good'
}

# Function to get car recommendations based on user preferences
def get_recommendations(user_preferences, data=data):
   # Filter cars based on user preferences and budget
    filtered_cars = data[(data['Price'] <= user_preferences['Budget']) &
                        (data['Description'].str.contains(user_preferences['BodyType'], case=False))]

    if len(filtered_cars) == 0:
       print("No cars match the user's preferences within the budget.")
       return None

    # Preprocess the car data for filtered cars
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(filtered_cars['Description'])

    # Calculate the average TF-IDF score for filtered cars
    avg_tfidf = tfidf_matrix.mean(axis=0)

    # Calculate the cosine similarity between user preferences and filtered cars
    sim_scores = linear_kernel(avg_tfidf, tfidf_matrix)

    # Get indices of top recommended cars
    car_indices = sim_scores.argsort()[0][::-1]

    # Recommend the top N cars (adjust N as needed)
    recommended_cars = data.iloc[car_indices][:N]

    return recommended_cars

# Get car recommendations for the user
N = 5  # Number of recommendations
recommended_cars = get_recommendations(user_preferences)

if recommended_cars is not None:
    print(recommended_cars[['Make', 'Model', 'Year']])