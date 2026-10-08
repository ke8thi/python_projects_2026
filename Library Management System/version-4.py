books={}
members={}
def addbook():
   while True:
        while True:
          try:
            id=int(input("Please enter id of the book:-"))
          except ValueError:
              print("Book ID must be an integer")
          else:
              if id in books:
                      print("Book with given ID is already present. Please enter a unique ID.")
              else:
                      break
        while True:
          title=input("Please enter the title of the book:-")
          if not title.strip():
              print("Title cannot be empty")
          else:
              break
        while True:
           author=input("Please enter the author of the book:-")
           if not author.strip():
                print("Author name cannot be empty")
           else:
              break
        status="available"
        borrowed_by=None
        book={
          "title":title,
          "author":author,
          "status":status,
          "borrowed_by":borrowed_by,
          "issue_count":0,
          "history": []
        }
        books[id]=book
        while True:
            ans=input("WANT TO CONTINUE ENTER:(y/n):-").lower()
            if ans not in ['y','n']:
                print("Invalid choice. Please enter y or n.")
            else:break
        if ans=='y':
            continue
        else:break
def addmembers():
  while True:
    while True:
          try:
              id=int(input("Please enter id :-"))
          except ValueError:
              print("ID must be an integer")
          else:
              if id in members:
                  print("Member with give id is already present please enter unique id")
              else:
                  break
    while True: 
        name=input("Please enter the name of the member:-")
        if not name.strip():
            print("Name cannot be empty")
        else:
            break
    members[id]={"name":name}
    while True:
        ans=input("WANT TO CONTINUE ENTER:(y/n):-").lower()
        if ans not in ['y','n']:
            print("Invalid choice. Please enter y or n.")
        else:break
    if ans=='y':
        continue
    else:break
def viewbook():
   print("=======BOOKS==========")
   for key,value in books.items():
      id=key
      title=value["title"]
      author=value["author"]
      status=value["status"]
      bor=value["borrowed_by"]
      print("ID: ",id)
      print("Title: ",title)
      print("Author: ",author)
      print("Status: ",status)
      print("Borrowed By: ",bor)
      print()
def viewmembers():
   print("======MEMBERS=============")
   for key,value in members.items():
      id=key
      name=value["name"]
      print("ID: ",id)
      print("Name: ",name)
      print()
def searchbook():
   print("1.Search by Book ID")
   print("2.Search by Title")
   print("3.Search by Author")
   while True:
        try:
            choice=int(input("Please enter your choice(1/2/3):-"))
        except ValueError:
            print("Choice must be an integer")
        else:
            if choice not in [1,2,3]:
                print("Invalid choice")
            else:break
   if choice==1:
      while True:
          try:
            idvalue=int(input("Enter the id to be searched:-"))
          except ValueError:
              print("Id must be integer")
          else:
              if idvalue not in books:
                  print("Book with given ID is not present")
              else:
                  break           
      for key,value in books.items():
          if key==idvalue:
                  id=key
                  title=value["title"]
                  author=value["author"]
                  status=value["status"]
                  bor=value["borrowed_by"]
                  print("ID: ",id)
                  print("Title: ",title)
                  print("Author: ",author)
                  print("Status: ",status)
                  print("Borrowed By: ",bor)
                  print()
   elif choice ==2:
      while True:
            title=input("Please enter the title of the book:-")
            if not title.strip():
                print("Title cannot be empty")
            else:
                 bookfound=False
                 for key,value in books.items():
                    if value["title"]==title:
                        bookfound=True
                 if bookfound:
                     break
                 else:
                    print("Book with given title is not present")
      for key,value in books.items():
          if value["title"]==title:
                  id=key
                  title=value["title"]
                  author=value["author"]
                  status=value["status"]
                  bor=value["borrowed_by"]
                  print("ID: ",id)
                  print("Title: ",title)
                  print("Author: ",author)
                  print("Status: ",status)
                  print("Borrowed By: ",bor)
                  print()
   else:
      while True:
            author=input("Please enter the authpr of the books:-")
            if not author.strip():
                print("author cannot be empty")
            else:
                 bookfound=False
                 for key,value in books.items():
                    if value["author"]==author:
                        bookfound=True
                 if bookfound:
                     break
                 else:
                    print("Books with given author is not present")
      for key,value in books.items():
          if value["author"]==author:
                  id=key
                  title=value["title"]
                  author=value["author"]
                  status=value["status"]
                  bor=value["borrowed_by"]
                  print("ID: ",id)
                  print("Title: ",title)
                  print("Author: ",author)
                  print("Status: ",status)
                  print("Borrowed By: ",bor)
                  print()
def viewbookhistory():
    while True:
        try:
            bookid = int(input("Enter Book ID:-"))
        except ValueError:
            print("ID must be integer")
        else:
            if bookid not in books:
                print("Invalid id")
            else:
                break

    print("=======BOOK HISTORY==========")
    print("Book ID:", bookid)

    history = books[bookid]["history"]

    if not history:
        print("No borrowing history found.")
    else:
        for val in history:
            print("Member ID:", val["member_id"])
            print("Action:", val["action"])
            print()
def viewmemberhistory():
    while True:
        try:
            memberid = int(input("Enter Member ID:-"))
        except ValueError:
            print("ID must be integer")
        else:
            if memberid not in members:
                print("Invalid id")
            else:
                break

    print("======= MEMBER HISTORY ========")
    print("Member ID:", memberid)

    found = False

    for bookid, book in books.items():
        for record in book["history"]:
            if record["member_id"] == memberid:
                found = True
                print("Book ID:", bookid)
                print("Action:", record["action"])
                print()

    if not found:
        print("No borrowing history found.")
def recentactivity():
    print("======= RECENT LIBRARY ACTIVITY ========")

    found = False

    for bookid, book in books.items():
        for record in book["history"]:
            found = True
            print("Book ID:", bookid)
            print("Member ID:", record["member_id"])
            print("Action:", record["action"])
            print()

    if not found:
        print("No library activity found.")
def issuebook():
    while True:
        try:
            bookid = int(input("Enter Book ID:-"))
        except ValueError:
            print("ID must be integer")
        else:
            if bookid not in books:
                print("Id is not present please enter correct id")
            else:
                break
    while True:
        try:
            memberid = int(input("Enter Member ID:-"))
        except ValueError:
            print("ID must be integer")
        else:
            if memberid not in members:
                print("Id is not present please enter correct id")
            else:
                break

    if books[bookid]["status"] == "available":
        books[bookid]["status"] = "issued"
        books[bookid]["borrowed_by"] = memberid
        books[bookid]["issue_count"]+=1
        record= {"member_id":memberid,"action":"issued"}
        books[bookid]["history"].append(record)
        print("Book", bookid, "issued to Member", memberid, "successfully")
    else:
        print("Book is already issued")
def returnbook():
    while True:
        try:
            bookid = int(input("Enter Book ID:-"))
        except ValueError:
            print("ID must be integer")
        else:
            if bookid not in books:
                print("Invalid id")
            else:
                break

    if books[bookid]["status"] == "available":
        print("Book isn't issued")
    else:
        books[bookid]["status"] = "available"
        record={"member_id":books[bookid]["borrowed_by"],"action":"returned"}
        books[bookid]["history"].append(record)
        books[bookid]["borrowed_by"] = None
        print("Book is returned successfully, Thank you")
def deletebook():
    while True:
        try:
            bookid = int(input("Enter Book ID:-"))
        except ValueError:
            print("ID must be integer")
        else:
            if bookid not in books:
                print("Invalid id")
            else:
                break

    if books[bookid]["status"] == "issued":
        print("Book currently issued try later")
    else:
        books.pop(bookid)
        print("Book deleted successfully")
def deletemember():
    while True:
        try:
            mem_id = int(input("Enter member id:-"))
        except ValueError:
            print("ID must be integer")
        else:
            if mem_id not in members:
                print("Id is not present please enter correct id")
            else:
                break

    mem_book = False

    for key, value in books.items():
        if mem_id == value["borrowed_by"]:
            mem_book = True
            break

    if mem_book:
        print("Member currently has a book. Return it before deleting.")
    else:
        members.pop(mem_id)
        print("Member deleted successfully")
def librarystats():
    availablebooks=0
    issuesdbooks=0
    totalbooks = len(books)
    totalmemebers = len(members)
    for key,values in books.items():
        if values["status"]=='available':
            availablebooks+=1
        if values["status"]=='issued':
            issuesdbooks+=1
    print("=======LIBRARY STATISTICS========")
    print("Total Books     :",totalbooks)
    print("Total Members   :",totalmemebers)
    print("Available Books :",availablebooks)
    print("Issued Books    :",issuesdbooks)
def viewbookbystatus():
    print("========BOOK FILTER===========")
    print("1. Available Books")
    print("2. Issued Books")
    while True:
        try:
          choice=int(input("Enter your choice:-"))  
        except ValueError:
            print("Choice must be integer")
        else:
            if choice not in [1,2]:
               print("Chocie must be between [1/2]:")
            else:
               break
    availablebooks=0
    issuedbooks=0
    for key,values in books.items():
        if values["status"]=='available':
            availablebooks+=1
        if values["status"]=='issued':
            issuedbooks+=1
    if choice ==1:
        if availablebooks:
          for key,value in books.items():
             if value["status"]=='available':
                id=key
                title=value["title"]
                author=value["author"]
                print("ID: ",id)
                print("Title: ",title)
                print("Author: ",author)
                print()
        else:
            print("No available books found.")
    else:
      if issuedbooks:
        for key,value in books.items():
            if value["status"]=='issued':
              id=key
              title=value["title"]
              author=value["author"]
              bor=value["borrowed_by"]
              print("ID: ",id)
              print("Title: ",title)
              print("Author: ",author)
              print("Borrowed By: ",bor)
              print()
      else:
          print("No issued books found.")
def memberborrowingstats():
    print("====== MEMBER BORROWING STATISTICS======")
    mem=len(members)
    if mem:
          for keys,values in members.items():
            borrowed=0
            id=keys
            name=values["name"]
            print("Member ID: ",id)
            print("Name: ",name)
            for key,value in books.items():
              if keys==value["borrowed_by"]:
                borrowed+=1
            print("Books Borrowed:",borrowed)
            print()
    else:
        print("No members found.")
def mostissuedbooks():
    print("========== MOST ISSUESED BOOKS ===========")
    if not books:
        print("No books found.")
    if books:
      bookcount=0
      for key,value in books.items():
          bookcount=max(bookcount,value["issue_count"])
      if bookcount==0:
          print("No books have been issued yet.")
      if bookcount:
          for key,value in books.items():
              if value["issue_count"]==bookcount:
                        id=key
                        title=value["title"]
                        author=value["author"]
                        print("Book ID: ",id)
                        print("Title: ",title)
                        print("Author: ",author)
                        print("Times Issued:",bookcount)
def librarysummaryreport():
    print("==============================")
    print("   LIBRARY SUMMARY REPORT     ")
    print("==============================")
    availablebooks=0
    issuesdbooks=0
    totalissueactivity=0
    totalbooks = len(books)
    totalmemebers = len(members)
    for key,values in books.items():
        totalissueactivity+=values["issue_count"]
        if values["status"]=='available':
            availablebooks+=1
        if values["status"]=='issued':
            issuesdbooks+=1
    
    print("=======LIBRARY STATISTICS========")
    print("Total Books             :",totalbooks)
    print("Available Books         :",availablebooks)
    print("Issued Books            :",issuesdbooks)
    print("Total Members           :",totalmemebers)
    print("Total Issue Activity    :",totalissueactivity)
def bookactivityreport():
    print("======= BOOK ACTIVITY REPORT ========")

    if not books:
        print("No books found.")
        return

    for bookid, book in books.items():
        print("Book ID:", bookid)
        print("Title:", book["title"])
        print("Times Issued:", book["issue_count"])
        print("History Records:", len(book["history"]))
        print()              
while True:
    print("====================================")
    print("      LIBRARY MANAGEMENT SYSTEM     ")
    print("====================================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Add Member")
    print("5. View Members")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Delete Book")
    print("9. Delete Member")
    print("10. Library Statistics")
    print("11. View Book By Status")
    print("12. Member Borrowing Statistics")
    print("13. Most Issued Books")
    print("14. View Book History")
    print("15. View Member History")
    print("16. Recent Library Activity")
    print("17. Book Activity Report")
    print("18. Exit")
    print()

    while True:
        try:
            choice = int(input("Enter your choice:"))
        except ValueError:
            print("Choice must be an integer")
        else:
            if choice not in range(1, 19):
                print("Choice must be between 1 and 18")
            else:
                break

    if choice==1:
        addbook()
    elif choice==2:
        viewbook()
    elif choice==3:
        searchbook()
    elif choice==4:
        addmembers()
    elif choice==5:
        viewmembers()
    elif choice==6:
        issuebook()
    elif choice==7:
        returnbook()
    elif choice==8:
        deletebook()
    elif choice==9:
        deletemember()
    elif choice==10:
        librarystats()
    elif choice==11:
        viewbookbystatus()
    elif choice==12:
        memberborrowingstats()
    elif choice==13:
        mostissuedbooks()
    elif choice==14:
        viewbookhistory()
    elif choice==15:
        viewmemberhistory()
    elif choice==16:
        recentactivity()
    elif choice==17:
        bookactivityreport()
    else:
        break