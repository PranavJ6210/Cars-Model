import pandas as pd

# Sample car data (include price information)
data = pd.DataFrame({
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
    'Price': [25000, 22000, 35000, 24000, 40000]
})

# User preferences (replace with user input)
user_preferences = {
    'Budget': 50000,
    'BodyType': 'truck'  # Lowercase for case-insensitive matching
}

# Function to get car recommendations based on user preferences
def get_recommendations(user_preferences, data=data):
    # Filter cars based on user preferences and budget
    filtered_cars = data[
        (data['Price'] <= user_preferences['Budget']) &
        (data['Description'].str.lower().str.contains(user_preferences['BodyType'], case=False))
    ]

    if len(filtered_cars) == 0:
        print("No cars match the user's preferences within the budget.")
        return None

    # Sort filtered cars by price in ascending order and select the top N
    N = 5  # Number of recommendations
    recommended_cars = filtered_cars.sort_values(by='Price').head(N)

    return recommended_cars

# Get car recommendations for the user
recommended_cars = get_recommendations(user_preferences)

if recommended_cars is not None:
    print(recommended_cars[['Make', 'Model', 'Year']])
