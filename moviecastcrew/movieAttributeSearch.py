import imdb 

ia = imdb.IMDb()

name = "goodfellas"

#name = input('Type in the movie you want to search: ')

search = ia.search_movie(name)

id = search[0].getID()

movie = ia.get_movie(id)

for items in movie.keys():
    print(items)