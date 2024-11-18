#list of movies with their genre, year, and age rating
movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama", "year": 90, "age_rating": "R"},
    {"title": "The Godfather", "genre": "Crime", "year": 70, "age_rating": "R"},
    {"title": "The Dark Knight", "genre": "Action", "year": 00, "age_rating": "PG-13"},
    {"title": "12 Angry Men", "genre": "Drama", "year": 50, "age_rating": "Not Rated"},
    {"title": "Schindler's List", "genre": "History", "year": 90, "age_rating": "R"},
    {"title": "Pulp Fiction", "genre": "Crime", "year": 90, "age_rating": "R"},
    {"title": "The Lord of the Rings: The Return of the King", "genre": "Fantasy", "year": 00, "age_rating": "PG-13"},
    {"title": "The Avengers", "genre": "Action", "year": 10, "age_rating": "PG-13"},
    {"title": "Inception", "genre": "Sci-Fi", "year": 10, "age_rating": "PG-13"},
    {"title": "Forrest Gump", "genre": "Drama", "year": 90, "age_rating": "PG-13"},
    {"title": "Frozen", "genre": "Animation", "year": 10, "age_rating": "PG"},
    {"title": "Finding Nemo", "genre": "Animation", "year": 00, "age_rating": "G"},
    {"title": "Spirited Away", "genre": "Animation", "year": 00, "age_rating": "PG"},
    {"title": "Parasite", "genre": "Thriller", "year": 10, "age_rating": "R"},
    {"title": "Amélie", "genre": "Romance", "year": 00, "age_rating": "R"},
    {"title": "La La Land", "genre": "Musical", "year": 10, "age_rating": "PG-13"},
    {"title": "Coco", "genre": "Animation", "year": 10, "age_rating": "PG"},
    {"title": "Whiplash", "genre": "Drama", "year": 10, "age_rating": "R"},
    {"title": "Get Out", "genre": "Horror", "year": 10, "age_rating": "R"},
    {"title": "The Lion King", "genre": "Animation", "year": 90, "age_rating": "G"},
    {"title": "The Incredibles 2", "genre": "Animation", "year": 10, "age_rating": "PG"},
    {"title": "Kiki's Delivery Service", "genre": "Animation", "year": 90, "age_rating": "G"},
]
#asks the user questions
def get_user_preferences():
    
    print("Welcome to the Mood Movie Recommendation System!")
    preferred_genres = input("What type of movie are you in the mood for? (Separate by comma, e.g., Drama, Action): ")
    
    preferred_genres = [genre.strip().capitalize() for genre in preferred_genres.split(',')]
    
    min_year = int(input("What age generation are you looking for? (e.g., 80, 90, 00, 10, 20): "))
    
    age_ratings = input("What age ratings do you prefer? (Separate by comma, e.g., G, PG, PG-13, R): ")
    
    age_ratings = [rating.strip().upper() for rating in age_ratings.split(',')]
    
    return preferred_genres, min_year, max_year, age_ratings

#filters the database based on the answers
def recommend_movies(preferred_genres, min_year, max_year, age_ratings):
    recommended = []
    for movie in movies:
        if (movie['genre'] in preferred_genres and
            min_year <= movie['year'] <= max_year and
            movie['age_rating'] in age_ratings):
            recommended.append(movie['title'])
    return recommended

#Returns the filtered movies to the user
def main():
    genre, min_year, max_year, rating = get_user_preferences()
    recommended = recommend_movies(genre, min_year, max_year, rating)
    if recommended:
        print("\nWe recommend watching these movies!:")
        for title in recommended:
            print(title)
    else:
        print("\nNo movies found that match your criteria.")

if __name__ == "__main__":
    main()
