#Basic PassWord Manager Using Dictionary\
Login_Name='admin'
Login_Pw='Admin@1234'

#MenuSystem
def menu():
    while True:
        print("\n\tWELCOME")
        print("1. Add Password")
        print("2. Update Password")
        print("3. Delete Password")
        print("4. Search Password")
        print("0. Exit")
        option=input("Enter a Choice:")
        if option== "0":
            break
        option_selector(option)

#Option Selection
def option_selector(opt):
    if(opt== "1"):
        print("Add")
    elif(opt== "2"):
        print("Update")
    elif(opt== "3"):
        print("Delete")
    elif(opt== "4"):
        search()
    else:
        print("Wrong Input(0-4)")
    
#database
def search():
    database_data= {'jugalnepali@gmail.com':'Jugalkobau','jugaldaikoac@gmail.com':'Jugalko1234'}
    email= input("Enter the email/ username:")
    search=database_data[email]
    print("The password for ("+email+") is:"+search)


#Login System
def login():
    while True:
        Login_Name_Input= input("NAME:").lower()
        Login_Pw_Input= input("PASSWORD:")
        if Login_Name_Input == Login_Name and Login_Pw_Input == Login_Pw:
            menu()
            break
login()