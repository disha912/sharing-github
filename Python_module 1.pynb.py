
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


