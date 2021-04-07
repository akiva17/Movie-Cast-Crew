import imdb
from imdb.Person import Person

ia = imdb.IMDb()

name = input('Type in the movie you want to search: ')

search = ia.search_movie(name)

id = search[0].getID()

movie = ia.get_movie(id)

title = movie ['title']
year = movie['year']
print(str(title) + ' - ' + str(year))

# Print the cast and staff of a movie
for key, data in movie.items():
    if not hasattr(data, '__iter__'):
        # Only process the data if it is iterable (a list)
        continue

    for value in data:
        # Look in the movie data for person objects, then print their attributes
        if type(value) is Person:
            person: Person = value
            print(', '.join([
                person.get('name', 'Unnamed'),
                person.currentRole.get('name', key)
            ]))

#crewCategory = ['cast','director' , 'writers','producers' ,'composers', 
                #'cinematographers' ,  'editors' , 'editorial department',
                #'casting directors', 
                #'production designers', 'art directors', 'set decorators', 
                #'costume designers', 'make up department', 
                #'production managers', 
                #'assistant directors', 'art department', 'sound department', 
                #'special effects', 'visual effects', 'stunts', 
                #'camera department', 'animation department', 
                #'casting department', 'costume department', 
                #'location management', 'music department',
                #'script department', 'transportation department', 
                #'miscellaneous', 'thanks']

#x = 1
              
#while x < len(crewCategory):
    #for items in movie.keys():
        #if items == crewCategory[x]:
            #for names in movie[items]:
                #print(names)
        #x=x+1
        
    