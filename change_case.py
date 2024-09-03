def change_case(string,style):
    if(style=='c' or style == 'C'):
        print(capital_case(string))
    elif style == 's' or style == 'S':
        print(small_case(string))
    elif style == 'u' or style == 'U':
        print(alternate_case(string))
    else:
        print("Provide a valid style")
        

def capital_case(string):
    length_of_string=len(string)
    s=""
    for i in range(len(string)):
        if(string[i]>=chr(65) and string[i]<=chr(90)):
            s+=string[i]
            
        elif(string[i]>=chr(97) and string[i]<=chr(122)):
            temp=chr(ord(string[i]-32))
            s+=string[i]
            
            return s
        
def small_case(string):
    length_of_string=len(string)
    s = ""
    for i in range(len(string)):
        if(string[i]>=chr(97) and string[i]<=chr(122)):
            s+=string[i]
            
        elif(string)
