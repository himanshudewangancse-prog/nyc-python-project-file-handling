from pathlib import Path
import os

def create():
    try:
        name = input("Create a file name:- ")
        path = Path(name)
        if not path.exists():
            print("Your file is succesfully created")
            with open(path, "w") as fs:
                data = input("Write what you want to write in you file:- ")
                fs.write(data)
        else:
            print("File name already exist")
    except Exception as err:
        print("Error is occured",err)
def read():
    try:
        name = input("Name a file which one want to read:- ")
        path = Path(name)
        if path.exists():
            with open(path, "r") as fs:
                content = fs.read()
                print(f"There is your content \n {content}")
        else:
            print("This file does not exist")
    except Exception as err:
        print("Error is occured",err)
def update():
    try:
        name = input("Name a file which you want to update:- ")
        path = Path(name)
        if path.exists():
            print("1 for rename")
            print("2 for append")
            print("3 for overwrite")
            a = int(input("Enter your No. :- "))
            if a == 1:
                rename = input("Rename your file:- ")
                npath = Path(rename)
                if not npath.exists():
                    path.rename(npath)
                    print("Renamed succesfully")
                else:
                    print("File name already exist")
            elif a == 2:
                with open(path, "a") as fs:
                    w = input("write here:- ")
                    fs.write(" \n"+w)
                    print("Append succesfully")
            elif a == 3:
                with open(path, "w") as fs:
                    ow = input("Write what you want to overwrite:- ")
                    fs.write(ow)
                    print("Overwrite succesfully")
        else:
            print("This file does not exist")
    except Exception as err:
        print("Error is occured",err)
def delete():
    try:
        name = input("Name a file which want to delete:- ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("File is deleted succesfully")
        else:
            print("This file does not exist")
    except Exception as err:
            print("Error is occured",err)



# Show option what we provide
# we folllow crud opration 
print("Welcome to File Handling")
print("1 To create a file")
print("2 To read a file")
print("3 To update a file")
print("4 To delete a file")
# Take a input from user what he want to do
a = int(input("Select a number which is suitable for you:- "))
# calling a function
if a == 1:
    create()
if a == 2:
    read()
if a == 3:
    update()
if a == 4:
    delete()