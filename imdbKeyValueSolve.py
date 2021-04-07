import imdb 

ia = imdb.IMDb()

name = input('Type in the movie you want to search: ')

search = ia.search_movie(name)

id = search[0].getID()

movie = ia.get_movie(id)

title = movie ['title']
year = movie['year']
print(str(title) + ' - ' + str(year))

for items in movie.keys():
    if items == ('cast'):
        for names in movie[items]:
           print(names)
    elif items == ('director'):
        for names in movie[items]:
            print(names)     
    elif items == ('writers'):
        for names in movie[items]:
            print(names)        
    elif items == ('producers'):
        for names in movie[items]:
            print(names)  
    elif items == ('composers'):
        for names in movie[items]:
            print(names) 
    elif items == ('cinematographers'):
        for names in movie[items]:
            print(names) 
    elif items == ('editors'):
        for names in movie[items]:
            print(names)             
    elif items == ('editorial department'):
        for names in movie[items]:
            print(names)   
    elif items == ('casting directors'):
        for names in movie[items]:
            print(names)   
    elif items == ('production designers'):
        for names in movie[items]:
            print(names)   
    elif items == ('assistant directors'):
        for names in movie[items]:
            print(names)   
    elif items == ('set decorators'):
        for names in movie[items]:
            print(names)   
    elif items == ('art department'):
        for names in movie[items]:
            print(names)   
    elif items == ('costume designers'):
        for names in movie[items]:
            print(names)               
    elif items == ('make up department'):
        for names in movie[items]:
            print(names)                    
    elif items == ('production managers'):
        for names in movie[items]:
            print(names)                
    elif items == ('sound department'):
        for names in movie[items]:
            print(names)        
    elif items == ('special effects'):
        for names in movie[items]:
            print(names)        
    elif items == ('visual effects'):
        for names in movie[items]:
            print(names)        
    elif items == ('stunts'):
        for names in movie[items]:
            print(names)        
    elif items == ('camera department'):
        for names in movie[items]:
            print(names)    
    elif items == ('animation department'):
        for names in movie[items]:
            print(names)       
    elif items == ('casting department'):
        for names in movie[items]:
            print(names)       
    elif items == ('costume department'):
        for names in movie[items]:
            print(names)        
    elif items == ('location management'):
        for names in movie[items]:
            print(names)       
    elif items == ('music department'):
        for names in movie[items]:
            print(names)       
    elif items == ('script department'):
        for names in movie[items]:
            print(names)       
    elif items == ('transportation department'):
        for names in movie[items]:
            print(names)       
    elif items == ('miscellaneous'):
        for names in movie[items]:
            print(names)                   
    elif items == ('thanks'):
        for names in movie[items]:
            print(names)                   
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
        
    