def addition(n1,n2):
    print("Addition =",n1+n2)
def substraction(n1,n2):
    print("Substraction =",n1-n2)
def multiplication(n1,n2):
    print("multiplication =",n1*n2)
def division(n1,n2):
    if n2!=0:
        print("Division =",n1/n2)
    else:
        print("Cannot divide by zero")
print("******* Sample calculator******")
print("1.Addition")
print("2.Substraction")
print("3.multiplication")
print("4.Division")
print("5.Exit")
while True:
    choice=int(input("Enter your choice: "))
    if choice==5:
        print("Exit")
        break
    if choice in[1,2,3,4]:
        n1=int(input("Enter first number: "))
        n2=int(input("Enter second number: "))
        
        if choice==1:
            addition(n1,n2)
        elif choice==2:
            substraction(n1,n2)
        elif choice==3:
            multiplication(n1,n2)
        elif choice==4:
            division(n1,n2)
    else:
        print("Invalid choice! Please select 1 to 5.")
    
