# Movie Reccomendation System for Two Users

# Step 1: Welcome the users
print("Welcome to the Movie Reccomndation System!")
print("User 1 will input their favorite movies, and User 2 will choose a genre to get a suggestion.\n")

# Step 2: Initialize an empty dictionary to store movies and their genres
favorite_movies = {}

# Step 3: Ask User 1 to input 5 movies in varying genres
print("User 1, please enter 5 of your favorite movies and their genres (e.g., 'Inception' as Sci-Fi).")
for i in range(5): # Using the range function for iteration
    movie = input("Enter Movie " + str(i + 1) + ": ")
    genre = input("Enter the genre for '" + movie + "': ")
    favorite_movies[movie] = genre # Add the movie and its genre to the dictionary

# Step 4: Display the genres entered for clarity
print("\nUser 1, here are the movies and genres you entered:")
for movie, genre in favorite_movies.items():
    print("- " + movie + " (" + genre + ")")

# Step 5: Allow User 2 to choose a genre
print("\nUser 2, it's your turn!")
chosen_genre = input("Enter a genre you're interested in (e.g., Sci-Fi, Action, Comedy): ")

#Step 6: Define a function to find a movie recommendation
def recommend_movie(favorite_movies, chosen_genre):

    #Recommends a movie based on the chosen genre

    recommendations = [] # Accumulator pattern to collect recommendations

    # Search for movies in the chosen genre
    for movie, genre in favorite_movies.items():
        if genre.lower() == chosen_genre.lower(): # Case-insensitive comparison
            recommendations.append(movie)
    
    return recommendations # Return the list of matching movies

# Step 7: Get recommendations based on User 2's input
suggestions = recommend_movie(favorite_movies, chosen_genre)

# Drippy Step
numRecs = int(input("How many reccomendations would you like to see?"))


# Step 8: Display the recommendations
print("\nMovie Recommendations for User 2: ")
if suggestions:
    for i in range(1, numRecs + 1):
        for i in suggestions:
            print("- " + i)
else:
    print("Sorry, no movies were found in the genre '" + chosen_genre + "'.")

# Step 9: Thank the users
print("\nThank you for using the Movie Recommendation System!")
