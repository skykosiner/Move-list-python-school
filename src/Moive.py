from .MovieData import Movie
import requests

class Movies:
    def getMovies(self) -> list[Movie]:
        response = requests.get("https://imdb-api.com/en/API/Top250Movies/k_zc0xrv4c")

        movies = response.json().get("items")

        movieList = []
        for i in range(0x45):
            movieList.append(Movie(movies[i].get("title"), movies[i].get("year"), movies[i].get("crew"), movies[i].get("rank")))

        return movieList

    def printMovies(self) -> None:
        movies = self.getMovies()
        for i in range(len(movies)):
            print("{}. {} ({}) Directed by: {}".format(i + 1, movies[i].title,
                movies[i].year, movies[i].crew[:movies[i].crew.find("(") +
                    len("(")].replace("(", "")))
