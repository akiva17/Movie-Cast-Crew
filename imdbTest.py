import imdb 

ia = imdb.IMDb()

#name = "matrix"

while True:
    
    try:
        name = input('Type in the movie you want to search: ')

        search = ia.search_movie(name)
        
        id = search[0].getID()
        
        movie = ia.get_movie(id)
        
        title = movie ['title']
        year = movie['year']
        cast = movie['cast']
        director = movie['directors'] 
        writers = movie['writers']
        producers = movie['producers']
        composers = movie['composers']
        cinematographers = movie['cinematographers']
        editors = movie['editors']
        
        
        
        print(str(title) + ' - ' + str(year))
        
        for i in cast:
            print(i)
        for i in director:
            print(i)    
        for i in writers:
            print(i)
        for i in producers:
            print(i)
        for i in composers:
            print(i)
        for i in cinematographers:
            print(i)
        for i in editors:
            print(i)    
        #print(movie.keys())
        
        #moviesDB = ia
    except KeyError:
        print("This movie does not have one or more of the crew parameters.")
        continue
    break
        