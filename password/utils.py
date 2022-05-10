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
    temp_pass = ''

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

    # print(combine_list)
    if len(combine_list)==0:
        return False
    
    for x in range(LEN - len(temp_pass)):
        temp_pass = temp_pass + random.choice(combine_list)

    password = ""
    for x in temp_pass:
        password = password + x
    
    return password

# print(generate_pwd(8,True,False,True,True,False))

# import random
# import array

# def generate_pwd(l,up,low,num,sym,extra):
#     LEN = l

#     digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     symbols = ['@', '#', '$', '%']
#     extra_symbols = ['=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

#     combine_list = []
#     temp_pass = ''

#     if up==True:
#         combine_list += upper
#         temp_pass += random.choice(upper)
#     if low==True:
#         combine_list += lower
#         temp_pass += random.choice(lower)
#     if num==True:
#         combine_list += digits
#         temp_pass += random.choice(digits)
#     if sym==True:
#         combine_list += symbols
#         temp_pass += random.choice(symbols)
#     if extra==True:
#         combine_list += extra_symbols
#         temp_pass += random.choice(extra_symbols)

#     # print(combine_list)
#     if len(combine_list)==0:
#         return False
    
#     # temp_pass_list = array.array('u', temp_pass)
#     for x in range(LEN - len(temp_pass)):
#         temp_pass = temp_pass + random.choice(combine_list)
#         # temp_pass_list = array.array('u', temp_pass)
#         # random.shuffle(temp_pass)
    
#     print(temp_pass)
#     print(random.shuffle(list(temp_pass)))
#     print(temp_pass)

#     password = ""
#     for x in temp_pass:
#         password = password + x
    
#     return password

# print(generate_pwd(8,True,False,True,True,False))


# MAX_LEN = 12

# DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

# COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

# rand_digit = random.choice(DIGITS)
# rand_upper = random.choice(UPCASE_CHARACTERS)
# rand_lower = random.choice(LOCASE_CHARACTERS)
# rand_symbol = random.choice(SYMBOLS)

# temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

# for x in range(MAX_LEN - 4):
#     temp_pass = temp_pass + random.choice(COMBINED_LIST)
#     temp_pass_list = array.array('u', temp_pass)
#     random.shuffle(temp_pass_list)

# password = ""
# for x in temp_pass_list:
#     password = password + x