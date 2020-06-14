"""
#Use a stride value of 2 to print out every second character of the string E:

E = 'clocrkr1e1c1t'
print( E[0::2] )


##################################################

#Convert the variable F to uppercase:


F = "You are wrong"
print(F.upper())


#########################################################

#Consider the variable G, and find the first index of the sub-string snow:

G = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
print(G.find('snow'))




############################################################

#In the variable G, replace the sub-string Mary with Bob




G = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
print(G.replace('Mary','Bob'))



#############################################################



# Concatenate two tuples

tuple1 = ("disco",10,1.2 )
tuple2 = tuple1 + ("hard rock", 10)
print( tuple2 )


#############################################################


# Slice from index 3 to index 4

tuple1 = ("disco",10,1.2 )
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2[3:5])




#############################################################

# Sort the tuple

tuple2 = (11, 10, 15, 3, 20, 6, 5, 12)
print(sorted(tuple2))




#############################################################


# access the nested tuples

NestedTuple =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print("First Element is " , NestedTuple[0])
print("Third Element's first element is " , NestedTuple[2][1])
print("Fifth Element's second element's second element is " , NestedTuple[4][1][1])




#############################################################


#Find the length of the tuple, genres_tuple

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
print(len(genres_tuple))



#############################################################


# Use slicing to obtain indexes 3, 4 and 5

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco")
print(genres_tuple[2:5])




#############################################################



#Find the first two elements of the tuple genres_tuple

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco")
print(genres_tuple[:2])




#############################################################



#Find the first index of "disco"

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco")
print(genres_tuple.index('disco'))



#############################################################



#Generate a sorted List from the Tuple
C_tuple=(-5, 1, -3)
print(sorted(C_tuple))


#############################################################



# create a dictionary

Dict = {"Disha":1991 , "Saish":1988, "Aakanksha":1990, "China":1992}
print(Dict)


#############################################################



# Access to the value by the key
Dict = {"Disha":1991 , "Saish":1988, "Aakanksha":1990, "China":1992}
print(Dict["Saish"])
print(Dict[(0,1)])



#############################################################




# Get all the keys in dictionary
Dict = {"Disha":1991 , "Saish":1988, "Aakanksha":1990, "China":1992}
print(Dict.keys())



#############################################################




# Get all the values in dictionary
Dict = {"Disha":1991 , "Saish":1988, "Aakanksha":1990, "China":1992}
print(Dict.values())



#############################################################



# Append value with key into dictionary

Dict = {"Disha":1991 , "Saish":1988, "Aakanksha":1990, "China":1992}
Dict["Praful"] = 1989
print(Dict)




#############################################################




# Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the values

album_sales_dict = {"JLO":50000 ,"Taylor Swift":650000, "Katy Perry":40000 }
print(album_sales_dict)
print(album_sales_dict.keys())
print(album_sales_dict.values())




#############################################################



# Convert list to set

list1 = ["pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"]
print(set(list1))




#############################################################



# Add and remove element to set

A = set(["Thriller", "Back in Black", "AC/DC"])
A.add("Freedom")
A.remove("Thriller")
print(A)




#############################################################



# Verify if the element is in the set

A = {"Thriller", "Back in Black", "AC/DC","Freedom"}
print("AC/DC" in A)




#############################################################


#Find the intersections, difference, union of two sets

album_set1 = {"Thriller", 'AC/DC', 'Back in Black'}
album_set2 = { "AC/DC", "Back in Black", "The Dark Side of the Moon"}
print("Intersection of both the sets is ", album_set1 & album_set2 )
print("Intersection of both the sets using intersect function is ", album_set1.intersection(album_set2))
print("Difference in the set1 as compared to set2 is ", album_set1.difference(album_set2))
print("Union of both the sets is ", album_set1.union(album_set2))

album_set3 = album_set1 & album_set2
print("whether set3 is subset of set1: ", album_set3.issubset(album_set1))
print("whether set1 is superset of set3: ", album_set1.issuperset(album_set3))




#############################################################

"""

#does sum(List A) = sum(set B)

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print("sum of list A is ", sum(A))
print("sum of list B is ", sum(B))
