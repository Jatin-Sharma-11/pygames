print("STAR PATTERN GENERATOR")
print("Enter 1 to add two number")
print("Enter 2 to Subtract two number")
print("Enter 3 to multiply two number")
print("Enter 4 to exit")
a = None
while(a!=0):
    a = int(input("Which operation Do you want to perform?"))
    if(a == 1):
        b = int(input("Enter first Number(P)"))
        c = int(input("Enter Second Number(Q)"))
        print("P + Q =", b+c)
    elif(a==2):
        b = int(input("Enter first Number(P)"))
        c = int(input("Enter Second Number(Q)"))
        print("P - Q = ", b - c)
    elif (a == 3):
        b = int(input("Enter first Number(P)"))
        c = int(input("Enter Second Number(Q)"))
        print(" P X Q = ", b*c)
    else:
        exit()







