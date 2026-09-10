expenses={}
count=1

def addexpense(count):
    while True:

         amount = int(input("Enter your amount: "))
         category = input("Enter category: ")
         date = input("Enter date of spending: ")
         description = input("Enter description: ")

         val = {
           "Amount": amount,
           "Category": category,
           "Date": date,
           "Description": description
           }

         expenses[count] = val
         count+=1

         another = input("Another expense: y/n: ").lower()

         if another == "n":
            break
    return count
def viewexpense():
    print("=======EXPENSES=======")
    for key,value in expenses.items():
        print("ID:",key)
        for id,details in value.items():
            print(id,":",details)
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
        if word.lower() in v["Category"].lower() or word.lower() in v["Description"].lower():
            val+=v["Amount"]
    return val;
def deleteexpense(id):
     expenses.pop(id)
   
    
while(True):
    print("==============EXPENSE TRACKER==============")
    print(" -----1.Add Expense -----")
    print(" -----2.View Expense -----")
    print(" -----3.Total Expense -----")
    print(" -----4.Spending by Category ----")
    print(" -----5.Search Expense -----")
    print(" -----6.Delete Expense -----")
    print(" -----7.Exit ----")
    choice=int(input("Please enter your choice:-"))
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
        id=int(input("Please enter id to be deleted:-"))
        deleteexpense(id)
    elif(choice==7):
        break
    
    