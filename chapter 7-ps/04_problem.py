num=int(input("enter the number :"))

for i in range(2,num):
  if(num%i==0):
    print("Not a prime")
    break
  else:
    print(" a prime")
    break
