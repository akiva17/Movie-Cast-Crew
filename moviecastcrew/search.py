from typing import List

import imdb
from imdb.Person import Person


def search(name: str, category: List[str] = None):
    ia = imdb.IMDb()

    print('Searching on IMDb...')
    query = ia.search_movie(name)
    id = query[0].getID()
    movie: imdb.Movie = ia.get_movie(id)

    print(str(movie['title']) + ' - ' + str(movie['year']))

    # Print the cast and staff of a movie
    for key, data in movie.items():
        if category and key not in category:
            continue

        if not hasattr(data, '__iter__'):
            # Only process the data if it is iterable (a list)
            continue

        if Person in [type(item) for item in data]:
            # If a person is in the data, print the category name
            print('{:-^15}'.format(key))
        for value in data:
            # Look in the movie data for person objects, then print their attributes
            if type(value) is Person:
                person: Person = value
                print(', '.join([
                    person.get('name', 'Unnamed'),
                    person.currentRole.get('name', key)
                ]))