user={}

def register():
    print("============== USER REGISTRATION ==============")
    user_name=str(input("User name : "))
    password=str(input("Password : "))
    confirmpassword=str(input("Confirm Password : "))
    email=str(input("Email-id : "))
    
    try:
        phone=int(input("Phone: "))
        if len(str(phone)) != 10:
            print("Invalid phone number. The phone number must be exactly 10 digits.")
            main()
            return
    except ValueError:
        print("Invalid phone number. Please enter numeric values only.")
        main()
        return


    if password==confirmpassword :
        user[user_name]= {"password": password, "email": email, "phone": phone}
        print("User registered Sucessfully")
        login()
    else:
        print("Passwords do not match. Please try again.")
    main()



def login():
    print("================== USER LOGIN =================")
    if user:
        user_name=str(input("User name : "))
        password=str(input("Password : "))

    
        if user_name in user:
            stored_password = user[user_name]["password"]
            if stored_password == password :
                print("login sucessfully")
            else:
                count=0
                while count<2:
                    print("Passwords do not match. Please try again.")
                    password=str(input("Password : "))
                    if(stored_password==password):
                        print("login sucessfully")
                        break
                    else:
                        count+=1
                if count==3:
                    print("Failed to login - 3 unsuccessful attempts made by the user. Please try again later.")
        else:
            print("!!!No user exists!!!")
    else:
        print("!!!No user available!!!")
    main()

    
    


def main():
    print("============ User Authentication System =======")
    print("1-> USER REGISTRATION")
    print("2-> USER LOGIN")
    print("3-> Exit")
    
    option=int(input("Choose any on of them : "))

    if (option==1):
        register()
    elif (option==2):
        login()
    elif (option==3):
        print("!!!Exiting thank you!!!")
    else:
        print("Invalid Input")

main()
