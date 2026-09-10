students={}
def addstudent():
    while True:
        id=int(input("Please enter student-id:-"))
        name=input("Please enter student name:-")
        math_marks=int(input("Please enter student math marks:-"))
        science_marks=int(input("Please enter student science marks:-"))
        english_marks=int(input("Please enter student english marks:-"))
        stu={
            "name":name,
            "marks":{
            "math":math_marks,
            "science":science_marks,
            "english":english_marks
        }
        }
        students[id]=stu
        answer=input("Do you want to continue(y/n):-").lower()
        if answer=='y':
            continue
        else:
            break
def viewstudent():
    print("============STUDENTS===============")
    for key,value in students.items():
        print("--------------------------------")
        print("Id:-",key)
        print("Name:-",value["name"])
        print("Math:-",value["marks"]["math"])
        print("Science:-",value["marks"]["science"])
        print("English:-",value["marks"]["english"])
        print("--------------------------------")
def totalmarks():
     
     for key,value in students.items():
         maths=value["marks"]["math"]
         sciences=value["marks"]["science"]
         englishs=value["marks"]["english"]
         total=maths+englishs+sciences
         print(f"Total marks for student with id:- {key},name:-{value['name']} is:-{total}")
def averagemarks():
     for key,value in students.items():
         maths=value["marks"]["math"]
         sciences=value["marks"]["science"]
         englishs=value["marks"]["english"]
         total=maths+englishs+sciences
         avg=total/3
         print(f"Average marks for student with  id:- {key},name:-{value['name']} is:-{avg}")
def calculategrade():
    for key,value in students.items():
             maths=value["marks"]["math"]
             sciences=value["marks"]["science"]
             englishs=value["marks"]["english"]
             total=maths+englishs+sciences
             avg=total/3
             if avg>=90:
                  grade='A'
             elif avg>=80:
                  grade='B'
             elif avg>=70:
                  grade='C'
             elif avg>=60:
                  grade='D'
             else:
                  grade='F'
             print(f"ID:{key},Name:{value['name']},Grade:-{grade}")
def searchstudent(id):
     for key,value in students.items():
          if id==key:
                print("Id:-",key)
                print("Name:-",value["name"])
                print("Math:-",value["marks"]["math"])
                print("Science:-",value["marks"]["science"])
                print("English:-",value["marks"]["english"])
def deletestudent(id):
     for key in list(students.keys()):
          if id==key:
               students.pop(key)
               break
while True:
     print("############### WELCOME ####################")
     print("---1.Add Student----")
     print("---2.View Students---")
     print("---3.Total Marks---")
     print("---4.Average Marks---")
     print("---5.Calculate Grade----")
     print("---6.Search Student----")
     print("---7.Delete Student----")
     print("---8.Exit--------")
     option=int(input("---Please select an optiont----:-"))
     if option==1:
          addstudent()
     elif option==2:
          viewstudent()
     elif option==3:
          totalmarks()
     elif option==4:
          averagemarks()
     elif option==5:
          calculategrade()
     elif option==6:
          id=int(input("Please enter id of student to be searched:-"))
          searchstudent(id)
     elif option==7:
          id=int(input("Please enter id of student to be deleted:-"))
          deletestudent(id)
     elif option==8:
          break
          
     