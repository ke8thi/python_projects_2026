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
         avg=round(avg,2)
         print(f"id:- {key},name:-{value['name']},average:-{avg}")
def calculatepercentage():
     for key,value in students.items():
         maths=value["marks"]["math"]
         sciences=value["marks"]["science"]
         englishs=value["marks"]["english"]
         total=maths+englishs+sciences
         percentage=(total/300)*100
         percentage=round(percentage,2)
         print(f"id:- {key},name:-{value['name']},percentage:-{percentage}")
def topstudent():
     top=0
     for key,value in students.items():
          maths=value["marks"]["math"]
          sciences=value["marks"]["science"]
          englishs=value["marks"]["english"]
          total=maths+englishs+sciences
          avg=total/3
          avg=round(avg,2)
          if avg>top:
              top=avg
              top_id=key
              name=value["name"]
     print("========== TOP PERFORMING STUDENT ==========")
     print("ID:-",top_id)
     print("Name",name)
     print("Average:-",top)
def loweststudent():
     lowest=None
     for key,value in students.items():
          maths=value["marks"]["math"]
          sciences=value["marks"]["science"]
          englishs=value["marks"]["english"]
          total=maths+englishs+sciences
          avg=total/3
          avg=round(avg,2)
          if lowest is None:
             lowest=avg
             lowe_id=key
             name=value["name"]
          elif avg<lowest:
              lowest=avg
              lowe_id=key
              name=value["name"]
     print("========== LOWEST PERFORMING STUDENT ==========")
     print("ID:-",lowe_id)
     print("Name",name)
     print("Average:-",lowest)
def classaverage():
        avg_sum=0
        count=0
        for key,value in students.items():
             maths=value["marks"]["math"]
             sciences=value["marks"]["science"]
             englishs=value["marks"]["english"]
             total=maths+englishs+sciences
             avg=total/3
             avg=round(avg,2)
             avg_sum+=avg
             count+=1
  
        classavg=avg_sum/count
        print("class average:-",classavg)
        
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
def gradedistribution():
    a=0
    b=0
    c=0
    d=0
    f=0
    for key,value in students.items():
                 maths=value["marks"]["math"]
                 sciences=value["marks"]["science"]
                 englishs=value["marks"]["english"]
                 total=maths+englishs+sciences
                 avg=total/3
                 if avg>=90:
                      a+=1
                 elif avg>=80:
                      b+=1
                 elif avg>=70:
                      c+=1
                 elif avg>=60:
                      d+=1
                 else:
                      f+=1
    print("====GRADE DISTIBUTION====")
    print("A-Grade:-",a)
    print("B-Grade:-",b)
    print("C-Grade:-",c)
    print("D-Grade:-",d)
    print("F-Grade:-",f)
def passfailstudents():
        passed=0
        failed=0
        for key,value in students.items():
                 maths=value["marks"]["math"]
                 sciences=value["marks"]["science"]
                 englishs=value["marks"]["english"]
                 total=maths+englishs+sciences
                 avg=total/3
                 if avg>=60:
                     passed+=1
                 else:
                     failed+=1
        print("============PASS/FAIL STATISTICS==============")
        print("Passed Students:-",passed)
        print("Failed Students:-",failed)
        

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
     print("---6.Calculate Percentage")
     print("---7.Top Performing Student----")
     print("---8.Lowest Performing Student---")
     print("---9.Class Average----------")
     print("---10.Grade Distribution--------")
     print("---11.Pass/Fail Statistics-----")
     print("---12.Search Student----")
     print("---13.Delete Student----")
     print("---14.Exit--------")
     while True:
        try:
          option=int(input("---Please select an optiont----:-"))
        except ValueError:
              print("Please Enter a number")
        else:
              try:
                  if(option<=0 or option>14):
                        raise ValueError("Please enter a number between 1-14 only")
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
          calculatepercentage()
     elif option==7:
       if not students:
           print("No Students available")
       else:
           topstudent()
     elif option==8:
        if not students:
           print("No Students available")
        else:
         loweststudent()
     elif option==9:
         if not students:
                   print("No Students available")
         else:
           classaverage()
     elif option==10:
         gradedistribution()
     elif option==11:
         passfailstudents()
     elif option==12:
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
        
     elif option==13:
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
     elif option==14:
          break
