from datetime import datetime
import json
expenses={}
count=1
def saveexpenses():
    with open("expenses.json","w") as file:
        json.dump(expenses,file,indent=4)
def loadexpenses():
        global expenses
        global count
        try:
            with open("expenses.json","r") as file:
                data=json.load(file)
                new_dict={}
                for key,value in data.items():
                    new_dict[int(key)]=value   
                expenses=new_dict
                if len(expenses)<=0:
                  count=1
                else:
                  val=max(expenses.keys())
                  count=val+1
        except FileNotFoundError:
                expenses = {}
                count = 1
def addexpense(count):
    while True:
        while True:
            try:
             amount = int(input("Enter your amount: "))
            except ValueError:
                print("Please enter a number")
            else:
                try:
                 if amount<=0:
                     raise ValueError ("amount must be greater than zero")
                except ValueError as v:
                    print(v)
                else:
                    break
        while True:
           category = input("Enter category: ")

           if not category.strip():
              print("Category cannot be empty")
           else:
               break

        while True:
                date = input("Enter date: ")
                if not date.strip():
                    print("Date cannot be empty")
                    continue
                try:
                    datetime.strptime(date,"%Y-%m-%d")
                except ValueError :
                        print("Enter correct format of date")
                else:
                    break
                

        while True:
            description = input("Enter description: ")

            if not description.strip():
                print("Description cannot be empty")
            else:
                break
                                   
                        
        val = {
                "Amount": amount,
                "Category": category,
                "Date": date,
                "Description": description
            }
                        
        expenses[count] = val
        saveexpenses()
        count+=1
                    
        
        while True: 
            another = input("Another expense: y/n: ").lower()  
            if another not in ['y','n']:
                print("Please enter y(yes) or n(no)")
            else:
                break
        if another=="n":
            break
    return count
def viewexpense():
    print("========EXPENSES=========")
    for key,value in expenses.items():
        print("ID:",key)
        for id,details in value.items():
            print(id,":",details)
        print("----------------------")
def totalexpense():
  amount=0;
  for key,value in expenses.items():
     amount+=value["Amount"]
  return amount
def spendingbycategory():
    newlist={}
    for key,v in expenses.items():
            if v["Category"] not in newlist:
                newlist[v["Category"]]=v["Amount"]
            else:
               newlist[v["Category"]]+=v["Amount"]
    return newlist
def searchexpense(word):
    val=0;
    for k,v in expenses.items():
        if word.lower() in v["Category"].lower() or word.lower() in v["Description"].lower() or word.lower() in v["Date"]:
            val+=v["Amount"]
    return val;
def deleteexpense(id):
     expenses.pop(id)
     saveexpenses()
def editexpense(id):
          while True:
                    try:
                     amount = int(input("Enter your amount: "))
                    except ValueError:
                        print("Please enter a number")
                    else:
                        try:
                         if amount<=0:
                             raise ValueError ("amount must be greater than zero")
                        except ValueError as v:
                            print(v)
                        else:
                            break
          while True:
                   category = input("Enter category: ")
        
                   if not category.strip():
                      print("Category cannot be empty")
                   else:
                       break
        
          while True:
                        date = input("Enter date: ")
                        if not date.strip():
                            print("Date cannot be empty")
                            continue
                        try:
                            datetime.strptime(date,"%Y-%m-%d")
                        except ValueError :
                                print("Enter correct format of date")
                        else:
                            break
                        
        
          while True:
                    description = input("Enter description: ")
        
                    if not description.strip():
                        print("Description cannot be empty")
                    else:
                        break
                                           
                                
          val = {
                        "Amount": amount,
                        "Category": category,
                        "Date": date,
                        "Description": description
                    }
          expenses[id]=val
          saveexpenses()
               
   
loadexpenses()   
while(True):
    print("==============EXPENSE TRACKER==============")
    print(" -----1.Add Expense -----")
    print(" -----2.View Expense -----")
    print(" -----3.Total Expense -----")
    print(" -----4.Spending by Category ----")
    print(" -----5.Search Expense -----")
    print("------6.Edit Expense-------")
    print(" -----7.Delete Expense -----")
    print(" -----8.Exit ----")
    
    try:
       choice=int(input("Please enter your choice:-"))
    except ValueError:
        print("Invalid choice.Please enter a number")
    else:
        if choice >= 1 and choice <= 8:
            if(choice==1):
             count=addexpense(count)
            elif(choice==2):
                viewexpense()
            elif(choice==3):
                tc=totalexpense()
                print("Total Expense:-",tc)
            elif(choice==4):
                print(spendingbycategory())
            elif(choice==5):
                w=input("Please enter a word:-")
                print("Expense is:-",searchexpense(w))
            elif(choice==6):
                 try:
                     id=int(input("Please enter id to be edited:-"))
                     if id not in expenses:
                        raise KeyError ("Id is not present")
                 except ValueError:
                        print("Id can only be a number")
                 except KeyError as k:
                        print(k)
                 else:
                     editexpense(id)
            elif(choice==7):
                try:
                   id=int(input("Please enter id to be deleted:-"))
                   if id not in expenses:
                        raise KeyError ("Id is not present")
                except ValueError:
                    print("Id can only be a number")
                except KeyError as k:
                    print(k)
                else:
                    deleteexpense(id)
            elif(choice==8):
                break
        else:
            print("Invalid choice .Please choose 1-8 only")
        
        