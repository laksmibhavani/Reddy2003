n=int(input("Enter a number:"))
if n>1:
    for i in range(2,n):
        if n%1==0:
            print("Not prime")
            break
        else:
            print("prime")
    else:
      print("Not prime")