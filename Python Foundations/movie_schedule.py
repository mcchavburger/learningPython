#as with javascript, can define dictionarys (objects) in multiple ways
current_movies = {"die hard 1" : "11:00am"}

#assign more keys
current_movies["die hard 2"] = "10:30pm"
current_movies["die hard 3"] = "9:30pm"

#to delete
del current_movies["die hard 1"]

#accessing keys that dont exsist will error eg
#my_favourite_movie = current_movies["die hard 1"]

#to see if a key exists use, returns "none" evaluates to false
my_favourite_movie = current_movies.get("die hard 1")

if my_favourite_movie:
    print(my_favourite_movie)
else:
    print("Key doesnt exsist")

#list keys
for key in current_movies:
    print(key)

#to list keys and values
for key, movie in current_movies.items():
    print(key, "showing at", movie)