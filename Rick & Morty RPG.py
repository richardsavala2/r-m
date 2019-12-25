from tkinter import *
import os

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()
    
def delete4():
    screen5.destroy()

def delete7():
    screen8.destroy()

def logout():
    screen7.destroy()



def c137():
    screen9 = Toplevel(screen)
    screen9.title()
    screen9.geometry('400x400')
    Label(screen9, text = 'select character below', height = '2', width = '400', bg = 'limegreen').pack()
    mainframe = Frame(root)
    mainframe.grid(column=0, row=0, sticky=(N,W,E,S) )
    mainframe.columnconfigure(0, weight = 1)
    mainframe.pack(pady = 100, padx = 100)

    tkvar = Stringvar(root)

    choices = {'Rick', 'morty', 'summer', 'beth', 'mr. poopybutthole',  'jerry' }
    tkvar.set('Rick')

    PopupMenu = OptionMenu(mainframe, tkvar, *choices)
    Label(mainframe, text = 'choose a character').grid(row = 1, column = 1)
    popupMenu.grid(row = 2, column = 1 )
    def change_dropdown(*args):
        print(tkvar.get() )
    tkvar.trace('w', change_dropdown)
    root.mainloop()

def session():
    global screen8
    title = 'rick and morty RPG'
    screen8 = Toplevel(screen)
    screen8.title(title)
    screen8.geometry('400x400')
    Label(screen8, text = 'item: portal gun ', height = '2', width = '400', bg = 'limegreen').pack()
    Label(screen8).pack()
    Button(screen8, text = 'select dimension', command = delete7).pack()

def login_success():
    session()

    global screen3
    screen3 = Toplevel(screen)
    screen3.title('Success')
    screen3.geometry('150x100')
    Label(screen3, text = 'oOOoEEe Login Success').pack()
    Button(screen3, text = 'OK', bg = 'limegreen', command = delete2).pack()
           
def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen, bg = 'purple')
    screen4.title('Success')
    screen4.geometry('150x100')
    Label(screen4, text = 'incorrect broh!').pack()
    Button(screen4, text = 'OK', command =delete3).pack()
    
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title('Success')
    screen5.geometry('150x100')
    Label(screen5, text = 'broh not found!', bg = 'purple',font = 'calibri').pack()
    Button(screen5, text = 'OK', command = delete4).pack()

        
def register_user():
    print('working...')
    
    username_info = username.get()
    password_info = password.get()

    file=open(username_info, 'w')   
    file.write(username_info+'\n')
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = 'Registration Success', fg = 'green', font = ('Calibri',11)).pack()

def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognized() 
            
    else:
        user_not_found() 
        
    
def register():
    global screen1
    screen1 = Toplevel(screen, bg = 'limegreen')
    screen1.title('Register')
    screen1.geometry('300x250')

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text='Please enter details below').pack()
    Label(screen1, text='').pack()
    Label(screen1, text='Username * ').pack()
    
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text = 'Password * ').pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = '').pack()
    Button(screen1, text = 'Register', width = 10, height = 1, command = register_user).pack()
    
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title('Login')
    screen2.geometry('300x250')
    Label(screen2, text = 'Please enter details below', bg = 'limegreen').pack()
    Label(screen2, text = '').pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1
    
    Label(screen2, text = 'Username * ').pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = '').pack()
    Label(screen2, text = 'Password * ').pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = '').pack()
    Button(screen2, text = 'Login', width = 10, height = 1, command = login_verify).pack()
    
    
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title('Rick & Morty RPG')
    Label(text = 'Rick & Morty RPG', bg = 'limegreen', width ='300', height = '2', font = ('Calibri', 13)).pack()
    Label(text = '').pack()
    Button(text = 'Login', height = '2', width = '30', command = login).pack()
    Label(text = '').pack()                                               
    Button(text = 'Register', height = "2", width = '30', command = register).pack()

    screen.mainloop()
                                                   
main_screen()

def start_screen():
    global screen9
    screen = Tk
    screen.geometry("300x250")
    screen.title('Rick & Morty RPG')
    Label(text = 'Stay in the fucking car!', bg = 'limegreen', width ='300', height = '2', font = ('Calibri', 13)).pack()
    Label(text = '').pack()
    Button(text = 'yes', height = '2', width = '30').pack()
    Label(text = '').pack()
    Button(text = 'no', height = "2", width = "30").pack()

