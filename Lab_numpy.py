import numpy as np

print("***********  Question :- 1 : Convert the below list into numpy array then display the array my_list=[1,2,3,4,5]   ********\n")
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print("List : ",my_list)
print("Numpy Array : ",my_array)

print("\n***********  Question :- 2 : Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.My_list=[1,2,3,4,5]   ********\n")


my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print("Array : ", my_array)
print("First element : ", my_array[0])
print("Last element : ", my_array[-1])
multiplied_array = my_array * 2
print("Multiplied array : ", multiplied_array)

print("\n***********  Question :- 3 : Write a numpy program to create an array of 10 zeros,10 ones, and 10 fives.    ********\n")
zeros_array = np.zeros(10)
ones_array = np.ones(10)
fives_array = np.full(10, 5)
print("Array of 10 zeros:", zeros_array)
print("Array of 10 ones:", ones_array)
print("Array of 10 fives:", fives_array)

print("\n***********  Question :- 4 :  Write a numpy program to create a 3x3 matrix with values ranging from 2 to 10  ********\n")
matrix = np.arange(2, 11).reshape(3, 3)
print("3x3 matrix with values ranging from 2 to 10 : ")
print(matrix)