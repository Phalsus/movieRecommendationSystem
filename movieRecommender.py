import random

movies = {
 "action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
 "comedy": ["Superbad", "Step Brothers", "The Hangover", "Dumb and Dumber"],
 "drama": ["Forrest Gump", "The Shawshank Redemption", "Fight Club", "The Godfather"],
 "sci-fi": ["Inception", "The Matrix", "Interstellar", "Blade Runner 2049"]
}

class breakOut(Exception):
    pass


def getGenre():
    return list(movies.keys())

def getMoviesbyGenre(genre):
    return random.sample(movies.get(genre), 3)

def userChoice():
    print(f"What genre would you like to watch?, we have: {getGenre()} ")
    return input("Enter a movie genre or 'quit' to exit: ")

def recommendMovies():
    print("welcome to my Movie Recommendation System")
    try:
        genre = userChoice()

        if genre.lower() == "quit":
            print("Have a great day")
            raise breakOut
        elif genre.lower() in movies:
            print(f"You have chosen {genre} movies")
            recommendations = getMoviesbyGenre(genre)
            print(f"for {genre}, we recommend the following movies: {recommendations}")
            repeat = input("do you want to continue? (Y/N)")
            if repeat.lower() == "n":
                raise breakOut
            recommendMovies()
        

        else:
            print(f"sorry we dont have recommendations for that genre, you can try the following genres: {getGenre()} ")
    except breakOut:
        pass

recommendMovies()
