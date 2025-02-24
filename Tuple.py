# list is mutable 
# tuple and string are immutable

tuple=(2,4,3,1,23,1,1,1,1)
print(tuple)

print(tuple.index(23))  #this tells us the index

#slice
print(tuple[2:4])


#count method
print(tuple.count(1))



print("....................................")
#WRP that check the that given word is palindrome or not 
word=["b"]
copy_word=word.copy()
copy_word.reverse()

if(copy_word==word):
    print("Palindrome")
else:
    print("Not palindrome")



