import random
import array

def generate_pwd(l,up,low,num,sym,extra):
    LEN = l

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['@', '#', '$', '%']
    extra_symbols = ['=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

    combine_list = []
    temp_pass = ""

    if up==True:
        combine_list += upper
        temp_pass += random.choice(upper)
    if low==True:
        combine_list += lower
        temp_pass += random.choice(lower)
    if num==True:
        combine_list += digits
        temp_pass += random.choice(digits)
    if sym==True:
        combine_list += symbols
        temp_pass += random.choice(symbols)
    if extra==True:
        combine_list += extra_symbols
        temp_pass += random.choice(extra_symbols)

    if len(combine_list)==0:
        return False
    
    for x in range(LEN - len(temp_pass)):
        temp_pass += random.choice(combine_list)
    
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
    
    password = ""
    for x in temp_pass_list:
        password = password + x
    
    return password

# print(generate_pwd(8,True,False,True,True,False))