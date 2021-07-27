
#IMDB TOP 100 MOVIE LIST FINDER

#Imports the libraries we will use
import requests
from bs4 import BeautifulSoup

#Imdb website URL as an input


def Movie_List_Maker(url):

    #Parse the website

    html = requests.get(url)
    soup = BeautifulSoup(html.content , 'html.parser')

    #In the source code, movie names are in the h3 tag

    movies = soup.find_all("h3" , {"class" : "lister-item-header"})
    imdb_ratings = soup.find_all("div" , {"class" : "inline-block ratings-imdb-rating"})
    #Creates a list and text file to write movies and imdb ratings to a text file

    movie_list = list()
    ratings = list()
    file = open("movies.txt","a")

    for rating in imdb_ratings:
        ratings.append(rating.text.strip())
    #Iterate all the movie names and print them
    for movie in movies:
        movie_list.append(movie.text.strip())

    for i in range (0,50):
        file.write("\n")
        file.write(movie_list[i])
        file.write("\n")
        file.write("Imdb Rating: " + ratings[i])
        file.write("\n")


    file.close()

Movie_List_Maker("https://www.imdb.com/search/title/?groups=top_100")
Movie_List_Maker("https://www.imdb.com/search/title/?groups=top_100&start=51&ref_=adv_nxt")