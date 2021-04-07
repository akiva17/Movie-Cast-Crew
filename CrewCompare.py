import imdb 

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
#Scans all of the attributes of the movie for the Cast and Crew and puts them
#In the lists above.
#Super ugly but it basically works.
for items in movie.keys():
    if items == ('cast'):
        for names in movie[items]:
            movie1.append(names)
    elif items == ('director'):
        for names in movie[items]:
            movie1.append(names)     
    elif items == ('writers'):
        for names in movie[items]:
            movie1.append(names)        
    elif items == ('producers'):
        for names in movie[items]:
            movie1.append(names)  
    elif items == ('composers'):
        for names in movie[items]:
            movie1.append(names)
    elif items == ('cinematographers'):
        for names in movie[items]:
            movie1.append(names) 
    elif items == ('editors'):
        for names in movie[items]:
            movie1.append(names)             
    elif items == ('editorial department'):
        for names in movie[items]:
            movie1.append(names)  
    elif items == ('casting directors'):
        for names in movie[items]:
            movie1.append(names)   
    elif items == ('production designers'):
        for names in movie[items]:
            movie1.append(names)  
    elif items == ('assistant directors'):
        for names in movie[items]:
            movie1.append(names) 
    elif items == ('set decorators'):
        for names in movie[items]:
            movie1.append(names)  
    elif items == ('art department'):
        for names in movie[items]:
            movie1.append(names)   
    elif items == ('costume designers'):
        for names in movie[items]:
            movie1.append(names)               
    elif items == ('make up department'):
        for names in movie[items]:
            movie1.append(names)                    
    elif items == ('production managers'):
        for names in movie[items]:
            movie1.append(names)                
    elif items == ('sound department'):
        for names in movie[items]:
            movie1.append(names)        
    elif items == ('special effects'):
        for names in movie[items]:
            movie1.append(names)        
    elif items == ('visual effects'):
        for names in movie[items]:
            movie1.append(names)        
    elif items == ('stunts'):
        for names in movie[items]:
            movie1.append(names)        
    elif items == ('camera department'):
        for names in movie[items]:
            movie1.append(names)   
    elif items == ('animation department'):
        for names in movie[items]:
            movie1.append(names)      
    elif items == ('casting department'):
        for names in movie[items]:
            movie1.append(names)      
    elif items == ('costume department'):
        for names in movie[items]:
            movie1.append(names)       
    elif items == ('location management'):
        for names in movie[items]:
            movie1.append(names)       
    elif items == ('music department'):
        for names in movie[items]:
            movie1.append(names)       
    elif items == ('script department'):
        for names in movie[items]:
            movie1.append(names)      
    elif items == ('transportation department'):
        for names in movie[items]:
            movie1.append(names)      
    elif items == ('miscellaneous'):
        for names in movie[items]:
            movie1.append(names)                  
    elif items == ('thanks'):
        for names in movie[items]:
            movie1.append(names)
            
#for person in movie1:
    #print (person)

#Same thing as all the stuff above, but for the second movie.
#Again, not elegant.
name2 = input('Type in the second movie you want to search: ')

search2 = ia.search_movie(name2)

id = search2[0].getID()

movie2 = ia.get_movie(id)

title2 = movie2 ['title']
year2 = movie2['year']
print(str(title2) + ' - ' + str(year2))

for items in movie2.keys():
    if items == ('cast'):
        for names in movie2[items]:
            movie2list.append(names)
    elif items == ('director'):
        for names in movie2[items]:
            movie2list.append(names)     
    elif items == ('writers'):
        for names in movie2[items]:
            movie2list.append(names)        
    elif items == ('producers'):
        for names in movie2[items]:
            movie2list.append(names)  
    elif items == ('composers'):
        for names in movie2[items]:
            movie2list.append(names)
    elif items == ('cinematographers'):
        for names in movie2[items]:
            movie2list.append(names) 
    elif items == ('editors'):
        for names in movie2[items]:
            movie2list.append(names)             
    elif items == ('editorial department'):
        for names in movie2[items]:
            movie2list.append(names)  
    elif items == ('casting directors'):
        for names in movie2[items]:
            movie2list.append(names)   
    elif items == ('production designers'):
        for names in movie2[items]:
            movie2list.append(names)  
    elif items == ('assistant directors'):
        for names in movie2[items]:
            movie2list.append(names) 
    elif items == ('set decorators'):
        for names in movie2[items]:
            movie2list.append(names)  
    elif items == ('art department'):
        for names in movie2[items]:
            movie2list.append(names)   
    elif items == ('costume designers'):
        for names in movie2[items]:
            movie2list.append(names)               
    elif items == ('make up department'):
        for names in movie2[items]:
            movie2list.append(names)                    
    elif items == ('production managers'):
        for names in movie2[items]:
            movie2list.append(names)                
    elif items == ('sound department'):
        for names in movie2[items]:
            movie2list.append(names)        
    elif items == ('special effects'):
        for names in movie2[items]:
            movie2list.append(names)        
    elif items == ('visual effects'):
        for names in movie2[items]:
            movie2list.append(names)        
    elif items == ('stunts'):
        for names in movie2[items]:
            movie2list.append(names)        
    elif items == ('camera department'):
        for names in movie2[items]:
            movie2list.append(names)   
    elif items == ('animation department'):
        for names in movie2[items]:
            movie2list.append(names)      
    elif items == ('casting department'):
        for names in movie2[items]:
            movie2list.append(names)      
    elif items == ('costume department'):
        for names in movie2[items]:
            movie2list.append(names)       
    elif items == ('location management'):
        for names in movie2[items]:
            movie2list.append(names)       
    elif items == ('music department'):
        for names in movie2[items]:
            movie2list.append(names)       
    elif items == ('script department'):
        for names in movie2[items]:
            movie2list.append(names)      
    elif items == ('transportation department'):
        for names in movie2[items]:
            movie2list.append(names)      
    elif items == ('miscellaneous'):
        for names in movie2[items]:
            movie2list.append(names)                  
    elif items == ('thanks'):
        for names in movie2[items]:
            movie2list.append(names)

#--------------------TO DO--------------------------------
#This is supposed to be the compare function. I need to compare the 
#names of the objects in movie1 and movie2list to see if they're the same 
#and just spit out whichever ones match. It is currently running into 
#a TypeError where the 'Person' object isn't callable. And both of the lists
#are filled with 'Person' objects. SO I may have to edit the big ugly lines of
#if statements. Or find some other crafty way of extracting the strings of 
#names from the person objects (preferably while they're already in the lists
#I've made so I didn't waste my time with these big ugly if-statements!).
easy = []
for items in movie1:
    for items2 in movie2list:
        if items(['name']) == items2(['name']):
            print(items)
    
    
#All jokes aside I for sure wasted a bit of time with those if statements but 
#they KINDA WORK!




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
        
    