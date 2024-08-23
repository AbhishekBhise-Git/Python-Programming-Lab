def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

print("Please select operation -\n" \
    "1.ADD\n"\
    "2.SUB\n"\
    "3.MUL\n"\
    "4.DIV\n")

select = int(input("Select operation for calcii 1,2,3,4:2 "))

number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))

if select == 1:
    print(number_1,"+", number_2,"=",
    add(number_1,number_2))
    
elif select == 2:
    print(number_1,"-",number_2,"=",
    sub(number_1,number_2))
    
elif select == 3:
    print(number_1,"*",number_2,"=",
    mul(number_1,number_2))
    
elif select == 4:
    print(number_1,"/",number_2,"=",
    div(number_1,number_2))
    
else:
    print("Invalid Input")
    
    
    
        
    
    
    
    
        
    
