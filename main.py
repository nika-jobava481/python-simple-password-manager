import getpass

master_password=getpass.getpass("Master password: ")

def get():
    soc=input("website/app name: ").lower()
    with open("passwords.txt") as f:
        for line in f.readlines():
            print(line.rstrip().split(" | ")[0].lower())
            if line.rstrip().split(" | ")[0].lower() == soc:
                print(line)

def add():
    soc=input("website/app name: ")
    username=input("account username: ")
    password=getpass.getpass("account password: ")
    with open("passwords.txt","a") as f:
        f.write(f"{soc} | {username} | {password}\n")


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