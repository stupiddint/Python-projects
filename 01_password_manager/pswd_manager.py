from cryptography.fernet import Fernet

master_pwd = input("What is the master password?")


def add():
    name = input("Account name:")
    pwd = input("Password:")

    with open('password.txt', 'a') as f:
        f.write(name + " - " + pwd + "\n")
        f.close()


def view():
    f = open('password.txt', 'r')
    for line in f.readlines():
        data = line.rstrip()
        user, passw = data.split(" - ")
        print("User: " + user + ", Password: " + passw)


while True:
    mode = input("would you like to add a new password or view existing ones (view, add), press q to quit?").lower()
    if mode == 'q':
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("invalid mode")
        continue
