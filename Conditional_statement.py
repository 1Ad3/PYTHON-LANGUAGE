#create a program of odd and even

num=int(input("Enter the number:"))
if(num%2==0):
    print("Number is even")
else:
    print("Number is odd")


#Create the grading method of students

print("....................................")
name=input("Enter the name of student :")
section=input("Enter the section name:")
math=int(input("Enter the marks of math:"))
eng=int(input("Enter the marks of english:"))
ict=int(input("Enter the marks of ict:"))

totalmarks=math+eng+ict
percentage=(totalmarks/300)*100

print("............................................")
print("Name:",name)
print("Section:",section)
print("Percentage:",percentage)

if(percentage<=100 and percentage>80):
    print("Grade:A1")
elif(percentage<=80 and percentage>60):
    print("Grade:A")
else:
    print("Grade:C")
    

print("......................................")


# WAT a number is a multiple of 7 or not

num=int(input("Enter the number:"))
if(num%7==0):
    print("this number is multiple of 7")
    
else:
    print("not multiple of ")