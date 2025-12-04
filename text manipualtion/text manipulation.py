import os
import glob




database = []

# data initializer
def data():
     for file in glob.glob("*.txt"):
       database.append(file)

def write():
     name = input("what's the name of your new file: ")
     name = name.replace(" ","_")
     f = open(f"{name}.txt",'w')
     f.write(input(" write whatever you want : "))
     f.close()
     print("\033c")  # ANSI escape sequence

def read():
     for file in glob.glob("*.txt"):
           print(file)
     name = input("what's the name of your file (wihtout the extintion): ")
     name = name.replace(" ","_")
     f = open(f"{name}.txt",'r')
     print(f.read())
     f.close()
     

def append():
    for file in glob.glob('*.txt'):
        print(file)

    name = input('which one you want to append on? : ')
    f = open(f"{name}.txt",'r')
    txt = input(f'{f.read()} ')
    f = open(f"{name}.txt",'a')
    f.write(txt)
    f.close()
    print("\033c")  # ANSI escape sequence




########### Main ###########

while True:
    data()
    print(database)
    x=input("what do you want w/r/a: ")
    if x == 'w':
        write()
    elif x == 'r':
         read()
    elif x == 'a':
          append()
    


