import uuid
import getpass

useless_loop = True

while useless_loop == True:
    request = input("\nEnter command - ").lower()

    if "print functions" in request:
        print("\n1. New - for New Account"
            "\n2. "
            "\n"
            "\n"
            "\n")
    #create new profile
    elif "new" in request:
        name = input("\n\nEnter First Name - ").lower()
        last_name = input("Enter Last Name - ").lower()
        email = input("Enter Email Adress - ").lower()
        with open('memory.txt') as f:
            if email not in f.read():
                password = getpass.getpass("Set Password - ")
                plain_uuid = email + password 
                hashed_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, plain_uuid)
                with open('memory.txt', 'a+') as f:                                  #plain Email + (hashed email + hashed password)
                        f.write(email + (str(hashed_uuid)))
                        f.write("\n\n")
            else:
                    print("Email alredy stored!")
    #login
    elif "log in" in request:
        email_log_in = input("Enter Email Adress - ")
        with open('memory.txt') as f:
            if email_log_in in f.read():
                password_log_in = getpass.getpass("Type Password - ")
                log_in_uuid_plain = email_log_in + password_log_in
                log_in_uuid_hashed = uuid.uuid5(uuid.NAMESPACE_DNS, log_in_uuid_plain)
                log_in_credentials = email_log_in + str(log_in_uuid_hashed)
                with open('memory.txt') as f:
                    if log_in_credentials in f.read():
                        print("Logged in succesfully!")
                    else:
                        print("Wrong password or email!")
            else:
                print("Wrong email!")
    elif "close" in request or "exit" in request:
        useless_loop = False
    else:
        print("Try Again!")