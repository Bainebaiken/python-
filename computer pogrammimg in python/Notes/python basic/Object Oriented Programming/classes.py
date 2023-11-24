#classes 
# classes start with A CAPITAL LETTERS
#a class has properties ,methods,or attributies
class Student:
    #student_no
    #Name
    #email
    #contact
    #age
    #cohort
    #def__init__() is the constructor we use
    def __init__(self,student_no,name,email,contact,age,cohort):
       self.student_no = student_no
       self.name = name
       self.email = email
       self.contact = contact
       self.age =age
       self.cohort =cohort
# string presentation of an object
    def __str__(self) -> str:
        return f'{self.student_no},{self.name},{self.email}'  
    
# CREATE  A FUNCTION THAT RETURND STUDENT NAME ,COHORT,AND EMAIL 
#ACCES THESE FUNCTIONS USING ANY INSTANCE/OBJECT
    def name_email_cohort(self):
        return f"{self.name},{self.contact},{self.email},{self.cohort}"

#objects/instance
#each object has the same attributies with the class
student1=Student("2023/DCSE/0083/SS","lumala mariam nasejje","lumalamariam9@gmail.com","0741716104","20","cohort4")  
print(student1.name_email_cohort())    

# CREATE  A FUNCTION THAT RETURND STUDENT NAME ,COHORT,AND EMAIL 
#ACCES THESE FUNCTIONS USING ANY INSTANCE/OBJECT