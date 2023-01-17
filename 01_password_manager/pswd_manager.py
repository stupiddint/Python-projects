from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password?")
key = load_key() + master_pwd.bytes
fer = Fernet(key)


def add():
    name = input("Account name:")
    pwd = input("Password:")

    with open('password.txt', 'a') as f:
        f.write(name + " - " + fer.encrypt(pwd.encode()).decode() + "\n")
        f.close()


def view():
    f = open('password.txt', 'r')
    for line in f.readlines():
        data = line.rstrip()
        user, passw = data.split(" - ")
        print("User: " + user + ", Password: " + fer.decrypt(passw.encode()).decode())


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
