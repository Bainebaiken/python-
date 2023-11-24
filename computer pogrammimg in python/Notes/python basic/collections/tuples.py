#tuples 
#working with tuples 
#Accesing tuples iterms
#marks =(80,79,69,70)
#marks[0]
#print(type(marks))
#print(marks[0])# accessing the first iterm 
#print (len(marks))# lenth of the tuple 

#marks=(80,)
#print(marks)
#print(type(marks))

# questions
# check whether 79 exists in the variable marks (frist method)
#access79
marks =(80,79,69,70)
sevetynine = marks[1]
for value in marks :
  if value ==79:
    print(f"{sevetynine} is a member of variable marks ")
  else:
    print("88 doesnot exist")

    #second method 
    marks =(80,79,69,70)
    if 79 in marks :
      print("yes  79 is a member of variable ")
    else:
      print ("88 does not exist")

#print {79 is a member of variable marks }

# check whether 88 does exists if not 
#print iterm /value does not exist 

# work out 
name="baine"
age =(20)
print (f"Am {name} and lam {age}")

#replacing 
#modifications of tuples 
marks =(60,79,69,70) 

# changing a tuple to a list 
# replacing a value or iterm

new_marks =list(marks)
print(type(new_marks),new_marks)
marks =(60,79,69,70)
new_list =list(marks )
new_list[1]=88
marks=tuple(new_list)
print(marks)

# add 99 to the tuple 
updated_marks =tuple(new_marks)
updated_lists_marks = list(updated_marks)
updated_lists_marks .append(99)
print(tuple(updated_lists_marks))


