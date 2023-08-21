def Addition(x,y):
    return x+y
def Subtraction(x,y):
    return x-y
def Multiplication(x,y):
    return x*y
def Division(x,y):
    if y==0:
        print("Cannot divide by zero")    
    else :
        return x/y
print("Select Option:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    select=input("Enter any option from 4 mentioned:")
    if select in('1','2','3','4'):
        try:
            value1=int(input("Enter the first value:"))
            value2=int(input("Enter the second value:"))
            
        except ValueError:
            print("Incorrect input.\nPlease Enter a correct number.")
            continue
        
        if select == '1':
            print(value1,"+",value2,"=",Addition(value1,value2))
            
        elif select =='2':
            print(value1,"-",value2,"=",Subtraction(value1,value2))
            
        elif select == '3':
            print(value1,"*",value2,"=",Multiplication(value1,value2))
            
        elif select == '4':
            print(value1,"/",value2,"=",Division(value1,value2))
            
        further_operation=input("Further Operation:/n(Yes/No)")
        if further_operation == "Yes":
            continue
        elif further_operation == "No":
            print("Exit")
            break
        else:
            print("Invalid Input.")
    break