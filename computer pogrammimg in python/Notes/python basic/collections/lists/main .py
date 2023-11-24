#create a list storing student marks
student_marks =[60,70,80]
print(type(student_marks))
print (student_marks)

#accessind lists (positive indexing)
print(student_marks[2])
#negative indexing 
print(student_marks[-2])
#slicing lists
print(student_marks[1:2])
print(student_marks[0:2]) 
#checking if item  exists
if 80 in student_marks:
    print("yes ,80 is in the list")
else:
    print("No,80 does not eisit")
