def memento(path):
    try:
        with open(path,"r") as file_path:
            Message=int(file_path.read())
            print("Finally you found the correct one! The password is: "+str(Message))
    except ValueError:
        print("Wrong file, try again!")
    except FileNotFoundError:
        print("File not found, try again!")

