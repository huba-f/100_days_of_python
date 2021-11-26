from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.chicagotribune.com/featured/sns-stacker-best-films-all-time-20210430"
                        "-sd3hxsnsjrhu3ngv4tbyovc32q-photogallery.html")
emp_web_page = response.text

soup = BeautifulSoup(emp_web_page, "html.parser")

all_movies = soup.find_all(name="h6")

movie_titles = [movie.getText() for movie in all_movies[1:]]


for movie in movie_titles:
    with open("movies.txt", mode="a") as file:
        file.write('\n')
        file.write(movie)


