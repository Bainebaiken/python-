# Student Marks
#"student_marks"
#"studentMarks"

#"total_average_marks"
#"totalAverageMark"

#part 3
age=22
age_float=float(age)
print(age_float)
print (type(age_float))

#qtn2 create a function to find the average of two numbers , arguments aof the functio are (x,y)
def  average(x,y):
    sum=x+y
    average_score=sum/2
    print(f"Average_score is {average_score}")

average(90,80)
numOne=90
numTwo=80   
def sum (numOne,numTwo):
    totalSum=numOne+numTwo
    return totalSum

#qtn2(ii)
# program that asks the user to input 3 numbers and finds the minimum number test your program by entering 3 diffent numbers
def minimumNumber(a,b,c):
    a=int(input("Enter the first number"))
    b=int(input("second number"))
    c=int(input("third number"))
    if(a<b and a<c):
       print(f"{a} is the minimumNumber")
    elif(b<a and b<c):   
         print(f"{b} is the minimumNumber")
    else:
        print(f"{c}is the minimumNumber")
minimumNumber(70,60,80)   

# program of grading 
grade=[90,88,84,71,49]
def gradeCourseUnit(mark):
     if(mark >= 90 and mark <= 100):
        print(f"you scored A")
     elif(mark >= 80 and mark <= 89):
         print(f"you scored a B")
     elif(mark >= 70 and mark <= 79):
         print(f"you scored are C")
     else:
         print(f"you scored a D,below average")
gradeCourseUnit(88)
#logocaial or
(89,100)
def guess_number(num):
    if(num==89 or num==100):
      print("you guessed it right")
    else:
        print("try again ,wrong attempt")