import os
import glob
import funcies



def product_adder ():
   file_name=input("new file name : ")
   print('enter you products put x when you finish ')
   products =[]
   sum=0
   while True:
         sum += 1
         x = input(f"product num  {sum}")
         if x == 'x':
            break
         else:
          products.append(x)
   funcies.writer(f"{file_name}",products)




database = []

# data initializer
def data():
     for file in glob.glob("*.txt"):
       database.append(file)

########### Main ###########
while True :
    print("what do you want to do ?\n 1) Make New File\n 2) Edit File\n")
    x= int(input("hopa : "))
    match x :
     case 1 :
       product_adder()
