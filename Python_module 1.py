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



#does sum(List A) = sum(set B)

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print("sum of list A is ", sum(A))
print("sum of list B is ", sum(B))




#############################################################


# If statement example

age = 18
if age > 18:
    print("this person is allowed")
else:
    print("this person is minor")




#############################################################


# Elif statment example

age=18
if age > 18:
    print("This person is allowed")
elif age < 18:
    print("this person is minor")
else:
    print("this person will not be minor from next year")
    



#############################################################


# Condition statement example

age = 60
if age > 60 or age == 60:
    print("this person is senior citizen")
else:
    print("this person is not a senior citizen")
        



#############################################################


# Condition statement example with NOT

age = 18
if not age== 21:
    print("this peron is not 21")
            



#############################################################


# Write an if statement to determine if an album had a rating greater than 8. Test it using the rating for the album “Back in Black” that had a rating of 8.5. 
# If the statement is true print "This album is Amazing!". If the rating is less than or equal to 8 print “this album is ok”.

album_Back_in_Black = 8.5
if album_Back_in_Black > 8:
    print("This album is Amazing!")
else:
    print("this album is ok")
                



#############################################################


#Write an if statement to determine if an album came out before 1980 or in the years: 1991 or 1993. If the condition is true print out the year the album came out.

album_year=1979
if album_year < 1980 or album_year == 1991 or album_year == 1993:
    print("Album came out in", album_year )
                



#############################################################


#Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. If the score is less than 6, exit the loop. 
# The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
Rating = PlayListRatings[0]

while Rating > 6:
    print(Rating)
    Rating=PlayListRatings[i]
    i+=1
                



#############################################################


#Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange'

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i=0

while squares[i] == 'orange':
    new_squares.append(squares[i])
    i+=1
print(new_squares)
                



#############################################################



# First function example: Add 1 to a and store as b

def add1(a):
    a=a+1
    b=a
    print(b)

add1(1)
                



#############################################################


# Define a function for multiple two numbers

def mult(a,b):
    c=a*b
    print(c)

mult(5,7)
mult(2, 'Disha')
                



#############################################################


#calculating a equation

def equat(a,b):
    c = a + b + 2 * a * b - 1
    if( c <0 ):
        c=0
    else:
        c=5
    print(c)

equat(3,7)
                



#############################################################


#print list using function

def prlist(plist):
    for i in plist:
        print(i)

prlist(['1', 1, 'the man', "abc"])
                



#############################################################


#Come up with a function that divides the first input by the second input

def div(a,b):
    c=a/b
    print(c)

div(1400,7)
                



#############################################################


# Use the con function for the following question

def con(a, b):
    print(a + b)

con(3,5)
                



#############################################################


# create a list using function

lis=[]
def con(a, b):
    for i in range(6):
        lis.append(a + b)
        a+=1
        b+=2
    print(lis)

con(7, 4)
                



#############################################################



#Draw a rectangle using objects, functions and method


class Rect(object):

    def __init__(self, l, h, color):
        self.l = l
        self.h = h
        self.color = color

    def drawRectangle(self):
        import matplotlib.pyplot as plt
        plt.gca().add_patch(plt.Rectangle(0,0), width=self.l, height = self.h, fc =  self.color )
        plt.axis("scaled")
        plt.show()

GreenRectangle = Rect(5,6,'Green')
GreenRectangle.drawRectangle()

                



#############################################################



#Reading Text Files

file1 = 'C:\\Disha\\Python\\file.txt'
file2 = open(file1,'r')
fileread= file2.read()
print(file2.name)
print(file2.mode)
print(fileread)
file2.close()

                



#############################################################


#read a file using with

file1 = 'C:\\Disha\\Python\\file.txt'
with open(file1,'r') as file2:
    fileread = file2.read()
    print(fileread)
    
                



#############################################################

"""
#read a file line by line

file1 = 'C:\\Disha\\Python\\file.txt'
count=0
with (open(file1,'r')) as file2:
    for i in file2:
        filestr=str(i)
        print(filestr[8:16])




    
