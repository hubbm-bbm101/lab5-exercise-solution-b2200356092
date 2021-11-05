email = str(input("please give e-mail: "))
if type(email.find("@")) == int and email.find("@") != -1:
    if type(email.find(".")) == int and email.find(".") != -1:
        print("suitable email")
    elif email.find(".") == -1:
        print("not suitable email")
elif email.find("@") == -1:
    print("not suitable email")
