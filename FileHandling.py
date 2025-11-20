from pathlib import Path
import os

def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")
                           
def createfile():
    try:
        readfileandfolder()
        name=input("please tell your file name: ")
        p=Path(name)
        if not p.exists() and p.is_file():
            with open(p,"w") as fs:
                data = input("what you want to write: ")
                fs.write(data)
            print("file created sucessfully") # we created Project2.py using this function
        else:
            print("this file already exists")
    except Exception as err:
        print("error occurred")   
        
def readfile():
    try:    
        readfileandfolder()
        name = input("which file you want to read?")
        p=Path(name)
        if p.exists() and p.is_file(): 
            with open(p,'r') as fs:  #here P is the path of the file
                    data = fs.read()
                    print(data)
            print("file reading successfully")
        else:
            print("the file doesn't exist")
    except Exception as err:
        print("an error occured")        


def updatefile():
    try:
        readfileandfolder()
        name=input("tell the name of file you want to update")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file")
            print("Press 2 for overwriting the name of your file")
            print("press 3 for appending come content of your file")
            
            res= int(input("tell me your response: "))

            if res ==1:
                name2=input("tell your new file name: ")
                P2=Path(name2)
                p.rename(P2)
            if res ==2:
                with open(p,'w') as fs:
                    data=input("tell what you want to write this will overwrite the data: ")
                    fs.write(data)
            if res == 3:
                with open(p,'a') as fs:
                    data=input("tell what you want to append:  ")
                    fs.write(data)
    except Exception as err:
        print("an error occurred")



def deletefile():

    try:
        readfileandfolder()
        name=input("which file you want ot delete?")
        p =Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("file removed successfully")


        else:
            print("no such file exists")


    except Exception as err:
        print("No such file exists")



print("press 1 for creating a file ")
print("press 2 for reading a file ")
print("press 3 for updating a file ")
print("press 4 for deletion a file ")


check=int(input("please tell your response: "))
if check==1:
    createfile()

if check==2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()
