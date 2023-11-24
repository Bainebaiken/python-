#write python programthats takes in a student name 
student_name= input("enter your name:")
student_class = input("enter your class:")
#print(students_class) #whatevercome from the input function is a string 
#therefore we cast to make it a float type since we are to divide 
semester = (input("enter your semester:"))
html_mark =float (input("enter your html mark scored:"))
java_mark =float (input("enter your java mark scored:"))
php_mark = float(input("enter your php mark scored:"))
python_mark =float(input("enter your python mark scored:"))
react=float(input("enter your react mark scored:"))
#summation of the subject, #every subject carries 100marks 
total_mark =(html_mark+java_mark+php_mark+python_mark+react)
print(total_mark)
percentage_mark=(total_mark)/5
print(percentage_mark)

print("\n------output----")
print("student name:",student_name)
print("class:",student_class)
print("semester:",semester)