import sys;

arg = int(sys.argv[1])

def fatorial(n):
  if(n<=1):
    return 1
  else:
    return n * fatorial(n-1)
  

for i in range(0, arg+1):
  print "{0}! = {1}".format(i, fatorial(i))