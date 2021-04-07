# Movie Cast Crew
Movie cast crew is an application for comparing cast and crew between movies.

## Usage
### Simple Search
To search for movie staff, use the search command. The search can optionally be filtered by any number of staff categories.

`python main.py search movie_name --category category1 category2`

Examples:

```
> python main.py search heat --category director

Searching on IMDb...
Heat - 1995
---director----
Michael Mann, director
```

```
> python main.py search e.t. --category writer director

Searching on IMDb...
E.T. the Extra-Terrestrial - 1982
----writer-----
Melissa Mathison, writer
---director----
Steven Spielberg, director
```

```
> python main.py search the green mile -c thanks

Searching on IMDb...
The Green Mile - 1999
----thanks-----
Stephen King, thanks
Robyn Smith, thanks
Don Sundquist, thanks
```