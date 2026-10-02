books={}
members={}
def addbook():
   while(True):
        id=int(input("Please enter id of the book:-"))
        title=input("Please enter the title of the book:-")
        author=input("Please enter the author of the book:-")
        status="available"
        borrowed_by=None
        book={
          "title":title,
          "author":author,
          "status":status,
          "borrowed_by":borrowed_by
        }
        books[id]=book
        ans=input("WANT TO CONTINUE ENTER:(y/n):-").lower()
        if ans=='y':
            continue
        else:break
def addmembers():
  while True:
     id=int(input("Please enter id :-"))
     name=input("Please enter the name of the member:-")
     members[id]={"name":name}
     ans=input("WANT TO CONTINUE ENTER:(y/n):-").lower()
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
   choice=int(input("Please enter your choice(1/2):-"))
   if choice==1:
      idvalue=int(input("Enter the id to be searched:-"))
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
      title=input("Please enter the title of the book:-")
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
    bookid = int(input("Enter Book ID:-"))
    memberid = int(input("Enter Member ID:-"))

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
    bookid=int(input("Enter Book ID:-"))  
    book_found = False
    for key, value in books.items():
        if bookid == key:
            book_found = True
            if value["status"]=='available':
                print("Book isnt issued ")
                break
            else:
                value["status"]='available'
                value["borrowed_by"]=None
                print("book is returned successfully,Thank you")
    if book_found == False:
        print("Book with given id is not present") 
def deletebook():
    bookid=int(input("Enter Book Id to be deleted:-"))
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
    mem_id=int(input("Enter member id:-"))
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




