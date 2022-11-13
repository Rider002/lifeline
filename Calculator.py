# making a simple calculator by using python

def add (A,B):
    return(A+B)

def sub (A,B):
    return(A-B)

def mul (A,B):
    return(A*B)

def ssb (A,B):
    return(A/B)

print('chose any one')
print('1 addition')
print('2 subtration')
print('3multipitin')
print('4division')


while True:
    chose=input("choice(1,2,3,4)")
    if chose in ('1','2','3','4'):
        num1=float(input("Enter frist number:"))
        num2=float(input("Enter second number:"))

        if chose =='1':
            print(add(num1,num2))

        elif chose =='2':
            print(sub(num1,num2))

        elif chose =='3':
            print(mul(num1,num2))
        
        elif chose =='4':
            print(ssb(num1,num2))
        next_calculation=input("do you want another calculation(yes/no):>")
        if next_calculation =="no":
            break


    else:
      print("Wrong input")








