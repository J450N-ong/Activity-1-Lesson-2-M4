#Creating a tuple with datatypes
tuple1 = ("syntax",True,1.1,2)
print(tuple1)

#Creating a tuple with integers
tuple2 = (1,2,3,4,5)
print(tuple2)

#Creating a tuple by adding an integer to the previous tuple
tuple3 = tuple2 + (6,)
print(tuple3)

#Creating a tuple and counting the repeated integer
tuple4 = (10,20,30,40,50,10)
print(tuple4.count(10))

#Creating a tuple and slicing
tuple5 = (1,2,3,4,5,6,7,8,9,10)
print(tuple5[4:10])