#FOR LOAD LISTS FROM CSV FILES
def lister(file):
  f = open(f"{file}","r")
  content = (f.read())
  return content.split(',') 

def reader(file):
  f = open(f"{file}","r")
  print(f.read())
  return None

#FOR WRITING LISTS ON CSV FILES
def writer(file,list):
  sum=0
  f = open (f"{file}.csv","w")
  for x in list:
   sum +=1
   if sum == len(list):                           ## ? checks if it's the last object in list 
     f.write(x)  ## if yes (no comma)
   else:
     f.write(x+',')## if no (add comma for the next one )

#FOR appending LISTS ON CSV FILES
def appender(file,list):
  sum=0
  f = open (f"{file}","a")
  for x in list:
   f.write(","+x)