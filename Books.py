
#Class Book
class Books:
    def __init__(self,Title,Author,ISBN,CallNumber,Stock,Loaned):
        self.Title=Title 
        self.Author=Author 
        self.ISBN=ISBN 
        self.CallNumber=CallNumber 
        self.Stock=Stock 
        self.Loaned=Loaned 

#Initializing the inventory list object
inventory=[]

#Opening books.txt and appending each Books object to inventory
try:
    products=open("books.txt","r")
    lst=products.readlines()
    for i in lst:

        #Creating a separate Books object for each book by splitting the string on ";"
        book=Books(i.split(';')[0],i.split(';')[1],i.split(';')[2],i.split(';')[3],i.split(';')[4],i.split(';')[5])
        inventory.append(book)
    products.close()

except FileNotFoundError:
    print("File not found")


#Displaying the books in inventory in the format
def DisplayInventory():

    #Converting the inventory to a list of list object in order to use format function
    table=[]
    table.append(["Name","Author","ISBN","Call Number","Stock","Loaned","Available"])
    for i in inventory:
        table.append([i.Title[:50],i.Author[:20],i.ISBN[:13],i.CallNumber[:13],i.Stock[:10],i.Loaned,str(int(i.Stock)-int(i.Loaned))[:10]])

    #Displaying the inventory in Table format
    print("\nDisplaying Westlands Books Inventory\n")
    for i in table:
         print("{: <50} {: <20} {: <13} {: <13} {: <10} {: <10} {: <10}".format(*i))
    print("\n")

#Appending a new book to inventory
def AddaBook():
    print("\nAdding a New Book\n")

    Title=input("Title>")
    Author=input("Author>")
    ISBN=input("ISBN>")
    CallNumber=input("Call Number>")
    Stock=input("Stock>")
    Loaned=input("Loaned>")
    b=Books(Title,Author,ISBN,CallNumber,Stock,Loaned)
    inventory.append(b)

#Deleting the book using del function
def RemoveaBook():
    print("\nRemoving a Book\n")
    Author=input("Author>")
    Callnum=input("Call Number>")

    #finding entered Author and call number
    for i in range(len(inventory)):
        if(inventory[i].Author==Author and inventory[i].CallNumber==Callnum):
            del inventory[i]

#Exporting inventory to books.txt overwriting the previous data with updated one
def ExportInventory():
    print("\nExporting Inventory\n")
    f=open("books.txt","w")

    #Creating a list of strings to simplify writing to file 
    lst=[]
    for i in inventory:
        #Creating the ";" separated format and appending to lst
        lst.append(i.Title+";"+i.Author+";"+i.ISBN+";"+i.CallNumber+";"+i.Stock+";"+i.Loaned+";\n")

    #Writing to book.txt
    f.writelines(lst)
    f.close()
    print("Export complete\n")


#Main

flag=False
while(flag==False):
    print("\nWestlands Book Inventory Management Subsystem") 
    print("1. Display Inventory")
    print("2. Add Book")
    print("3. Remove a Book")
    print("4. Export Inventory")
    print("5. Quit IMS")
    option=input("Select an option from the menu>")
    
    
    if(option=="1"):
        DisplayInventory()
    elif(option=="2"):
        AddaBook()
    elif(option=="3"):
        RemoveaBook()
    elif(option=="4"):
        ExportInventory()
    elif(option=="5"):
        flag=True



 