n1=int(input("enter number :"))
n2=int(input("enter number :"))
n3=int(input("enter number :"))
n4=int(input("enter number :"))
 
if(n1>n2 and n1>n3 and n1>n4):
  print(n1) 
elif(n2>n1 and n2>n3 and n2>n4):
  print(n2)
elif(n3>n1 and n3>n2 and n3>n4):
  print(n2)
else:
  print(n4)