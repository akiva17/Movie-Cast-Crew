from __future__ import annotations
from typing import Optional, List, Set
# Don't worry about these imports, they just make notation clearer with less comments

import imdb
from imdb.Person import Person


# Goal for syntax
# >>> movie1 = MyMovie("Braveheart")
# >>> movie2 = MyMovie("Passion of the Christ")
# >>> print(movie1.compare(movie2))
# ["Mel Gibson", etc...]

class MyMovie(object):
    """Information and functions for a movie."""

    def __init__(self, name: str):
        """
        This method is called whenver an instance of this object is created. It is used to define an objects
        attributes on creation. For example:

        >>> movie = MyMovie('The Big Lebowski')
        >>> movie.name
        "The Big Lebowski"
        """
        self.name = name

        # Using an underscore before a variable name means the attribute is private. _imdb_data should only be used
        # inside the MyMovie class. This way, you don't have to know the imdb package to find useful information on a
        # movie. It's all within this class.

        # self._imdb_data = ia....
        # self.title = ....
        pass  # pass is the same as "do nothing"

    def __str__(self) -> str:
        """
        This method determines the string representation of this object. For example:

        >>> movie = MyMovie('Heat')
        >>> print(movie)
        "Heat - 1995"

        :return: MyMovie as a printable string
        """
        # return (however you want this object represented as a string)
        pass

    def get_cast(self, categories: Optional[List[str]] = None) -> List[str]:
        """
        Returns a list of all the people involved with the movie.

        Example:
        >>> for cast in movie.get_cast()
        >>>     print(cast)
        Actor1
        Actor2
        etc...

        :param categories: an optional list of categories to filter cast
        :return: a list of crew member names
        """
        pass

    def compare(self, other_movie: MyMovie) -> Set[str]:
        """
        Returns a set of crew members common to both movies. Once you write this method, Python has a very easy way
        to expand it to multiple movies.

        NOTE: IT DOES NOT PRINT THE COMPARISON. A movie object does not care how you want to look at it, all it cares
        about is giving you the correct data.

        :param other_movie: MyMovie object for comparison
        :return: set of crew member names
        """
        pass

ia = imdb.IMDb()
#Prompts user to type in movie.
name = input('Type in the movie you want to search: ')
#This line takes the input and searches the IMDb search system for it.
search = ia.search_movie(name)
#This takes the first result of the search and makes it the object.
#So be sure to type whatever movie right.
id = search[0].getID()
#Basically just takes that first search result and makes it an object.
movie = ia.get_movie(id)
#Empty lists for these ugly if-statements.
movie1 = []
movie2list = []
#Prints out the title and year of whatever movie grabbed.
#Helps to be sure.
title = movie ['title']
year = movie['year']
print(str(title) + ' - ' + str(year))

#Lines 23-33 takes the 'name' attribute from all 'Person' objects in the 1st movie.
for key, data in movie.items():
    if not hasattr(data, '__iter__'):
        # Only process the data if it is iterable (a list)
        continue

    for value in data:
        # Look in the movie data for person objects, then print their attributes
        if type(value) is Person:
            person: Person = value
            movie1.append(person.get('name', 'Unnamed'))


#Same thing as all the stuff above, but for the second movie.
name2 = input('Type in the second movie you want to search: ')

search2 = ia.search_movie(name2)

id = search2[0].getID()

movie2 = ia.get_movie(id)

title2 = movie2 ['title']
year2 = movie2['year']
print(str(title2) + ' - ' + str(year2))

for key, data in movie2.items():
    if not hasattr(data, '__iter__'):
        # Only process the data if it is iterable (a list)
        continue

    for value in data:
        # Look in the movie data for person objects, then print their attributes
        if type(value) is Person:
            person: Person = value
            movie2list.append(person.get('name', 'Unnamed'))



easy = []    
#Takes the names in both of the lists for both movies, sees if there are
#any in common, and creates a set so there are no duplicates.
for names1 in movie1:
    for names2 in movie2list:
        if names1 == names2:
            easy.append(names1)
            
easyset = set(easy)

#Checks to see if any matches were found. If not, feeds back no matches found.
#If yes, feeds back all cast and crew in common.
if len(easyset) == 0:
    print("----These movies have no cast or crew in common.----")
else:
    for item in easyset:
        print(item)
        
 

#All possible crew categories.

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


#Ignore this this didn't work.
#x = 1
              
#while x < len(crewCategory):
    #for items in movie.keys():
        #if items == crewCategory[x]:
            #for names in movie[items]:
                #print(names)
        #x=x+1
        
    