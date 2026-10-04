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
          "borrowed_by":borrowed_by
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
   while True:
        try:
            choice=int(input("Please enter your choice(1/2):-"))
        except ValueError:
            print("Choice must be an integer")
        else:
            if choice not in [1,2]:
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

    book_found = False

    for key, value in books.items():
        if bookid == key:
            book_found = True
            found_book = value
            break

    if book_found == False:
        print("Book with given ID not present")
        return

    member_found = False

    for key, value in members.items():
        if memberid == key:
            member_found = True
            break

    if member_found == False:
        print("Member with given ID not present")
        return

    if found_book["status"] == "available":
        found_book["status"] = "issued"
        found_book["borrowed_by"] = memberid
        print("Book", bookid, "issued to Member", memberid, "successfully")
    else:
        print("Book is already issued")
def  returnbook():
    while True:
        try:
           bookid=int(input("Enter Book ID:-"))  
        except ValueError:
            print("ID must be integer")
        else:
            if bookid not in books:
                print("Invalid id")
            else:
                break
    book_found = False
    for key, value in books.items():
        if bookid == key:
            book_found = True
            if value["status"]=='available':
                print("Book isn't issued ")
                break
            else:
                value["status"]='available'
                value["borrowed_by"]=None
                print("book is returned successfully,Thank you")
    if book_found == False:
        print("Book with given id is not present") 
def deletebook():
    while True:
            try:
               bookid=int(input("Enter Book ID:-"))  
            except ValueError:
                print("ID must be integer")
            else:
                if bookid not in books:
                    print("Invalid id")
                else:
                    break
    book_present=True
    bookid_present=False
    for key,value in books.items():
        if bookid==key:
            bookid_present=True
            if value["status"]=='issued':
                book_present=False
                print("Book currently issued try later")
    if bookid_present==False:
        print("Book with give id is not present")
    if book_present==True:
        for key in list(books.keys()):
            if bookid==key:
                books.pop(key)
def deletemember():
    while True:  
            try:  
                mem_id=int(input("Enter member id:-"))
            except ValueError:
                 print("ID must be integer")
            else:
                if mem_id not in members:
                    print("Id is not present please enter correct id")
                else:
                    break
    mem_present=False
    mem_book=False
    for key,value in members.items():
        if key==mem_id:
            mem_present=True
            for k,val in books.items():
                if mem_id==val["borrowed_by"]:
                    mem_book=True
    if mem_present==False:
        print("Member with given ID is not present")
    if mem_book==True:
        print("Member currently has a book. Return it before deleting.")
    if mem_present and mem_book==False:
        for key in list(members.keys()):
            if mem_id==key:
                members.pop(key)
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
    print("10. Exit")
    print()
    choice=int(input("Enter your choice:")) 
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
        break




