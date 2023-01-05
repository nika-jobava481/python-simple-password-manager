import getpass
from cryptography.fernet import Fernet

master_password=getpass.getpass("Master password: ")

        
def get_key():
    with open("key.key","rb") as keyFile:
        return keyFile.read()

fer=Fernet(get_key() + master_password.encode())

# def set_key():
#     key=Fernet.generate_key()
#     with open("key.key","wb") as keyFile:
#         keyFile.write(key)
# set_key()


def get():
    soc=input("website/app name: ").lower()
    with open("passwords.txt") as f:
        for line in f.readlines():
            print(line.rstrip().split(" | ")[0].lower())
            if line.rstrip().split(" | ")[0].lower() == soc:
                web,user,passwd=line.rstrip().split(" | ")
                print(f"for {web} Username: {user} password is \"{fer.decrypt(passwd.encode()).decode()}\"")

def add():
    soc=input("website/app name: ")
    username=input("account username: ")
    password=getpass.getpass("account password: ")
    with open("passwords.txt","a") as f:
        f.write(f"{soc} | {username} | {fer.encrypt(password.encode()).decode()}\n")


while True:
    mode=input("select mode | get,add | print q to quit: ").lower()
    if mode=="q":
        break
    if mode=="get":
        get()
    elif mode=="add":
        add()
    else:
        print("wrong input!\n")