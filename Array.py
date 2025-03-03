from array import *
temps = array ('i',[1,2,3])

#for i in temps:
#       print (temps)

#for i in range (3):
#       print (temps[i])

for i in range (len(temps)):
       print (temps[i])

##temps.append (4)
##print (temps)
##temps.insert (0,0)
##print (temps)
##temps.remove (0)
##print (temps)
##temps.pop ()
##print (temps)

print (temps.index (1))
temps.reverse ()
print (temps.count (2))
print (temps.buffer_info())




#slice array
num_list=[1,2,3,4,5,6,7,8]
number_array=array('i',num_list)
print("numbers are: " , number_array[1:7])



odd = array('i', [1, 3, 5])
even = array('i', [2, 4, 6])

numbers = array('i')  # creating empty array of integer
numbers = odd + even

print(numbers)

