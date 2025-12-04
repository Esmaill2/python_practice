import random

tale=0
head=0

def tests():
  return 'fuck'
def printer():
 global head, tale
 total = head+tale
 x = (f"Heads : {head} , Percetnage : {(head/total*100):0.2f}%\nTales : {tale} , Percetnage : {(tale/total*100):0.2f}%\nTotal Flips = {total}")
 return x


def fliper():
  global head, tale
  random_integer = random.randint(1, 10)
  if random_integer%2 == 0:
   #  print('== Head ==')
    head +=1

  elif random_integer%2 != 0:
    #  print('== Tale ==')
    tale +=1

if __name__ == "__main__":
 while True:
   input('Press Enter To Flip  ')
   fliper()
   print(printer())

  
 
