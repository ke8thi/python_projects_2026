students={}
def addstudent():
  while True:
    while True:
        try:
             id=int(input("Please enter student-id:-"))
        except ValueError:
            print("ID must be number only")
        else:
            try:
                if id in students.keys():
                    raise ValueError("ID already exists")
            except ValueError as v:
                print(v)
            else:
                try:
                    if id<=0:
                        raise ValueError("ID cannot be negative or ZERO")
                except ValueError as v:
                    print(v)
                else:
                    break
    while True:
       name=input("Please enter student name:-").strip()
       if len(name)<=0:
           print("Name cannot be empty")
       else:
           break
    while True:
      try:
        math_marks=int(input("Please enter student math marks:-"))
      except ValueError:
          print("Marks must be integer only")
      else:
          try:
              if math_marks<0 or math_marks>100:
                  raise ValueError("Marks must be between 0-100 only")
          except ValueError as v:
              print(v)
          else:
              break
    while True:
          try:
            science_marks=int(input("Please enter student science marks:-"))
          except ValueError:
              print("Marks must be integer only")
          else:
              try:
                  if science_marks<0 or science_marks>100:
                      raise ValueError("Marks must be between 0-100 only")
              except ValueError as v:
                  print(v)
              else:
                  break
    while True:
          try:
            english_marks=int(input("Please enter student english marks:-"))
          except ValueError:
              print("Marks must be integer only")
          else:
              try:
                  if english_marks<0 or english_marks>100:
                      raise ValueError("Marks must be between 0-100 only")
              except ValueError as v:
                  print(v)
              else:
                  break
    stu={
            "name":name,
            "marks":{
            "math":math_marks,
            "science":science_marks,
            "english":english_marks
        }
        }
    students[id]=stu
    conti=False
    while True:
          answer=input("Do you want to continue(y/n):-").lower()
          if answer=='y':
            conti=True
            break
          elif answer=='n':
              break
          else:
              print("Enter on y/n please")
    if conti:
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
     while True:
        try:
          option=int(input("---Please select an optiont----:-"))
        except ValueError:
              print("Please Enter a number")
        else:
              try:
                  if(option<=0 or option>8):
                        raise ValueError("Please enter a number between 1-8 only")
              except ValueError as v:
                  print(v)
              else:
                  break         
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
      while True:
        try:
          id=int(input("Please enter id of student to be searched:-"))
          if id not in students:
              print("Student ID not found")
              continue
          searchstudent(id)
        except ValueError:
             print("ID must be a number")
        else:
            break
        
     elif option==7:
      while True:
        try:
          id=int(input("Please enter id of student to be deleted:-"))
          if id not in students:
                    print("Student ID not found")
                    continue
          deletestudent(id)
        except ValueError:
             print("ID must be a number")
        else:
            break
     elif option==8:
          break
          
     
