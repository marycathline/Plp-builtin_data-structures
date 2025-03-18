#Creating an empty list

my_list=[]
print(my_list)
print("Datatype", type(my_list))

#Append ellements to my_list: 10, 20, 30, 40.

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#Inserting the value 15 at the second position in the list
insert_position = 1
my_list.insert(insert_position, 15)
print(my_list)

#Extending my_list with another list: [50, 60, 70].

my_list.extend([50, 60, 70])
print(my_list)

#Removing the last element from my_list
my_list.remove(70)
print(my_list)  

#Sorting my_list in ascending order
my_list.sort()
print(my_list)

#Finding and printing the index of the value 30 in my_list.
index = my_list.index(30)
print("Index of 30 is:", index)
