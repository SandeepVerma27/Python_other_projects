# --------Using regex validation-----------
# basics email
# ( a-z )
# (0-9)
# . _ at time 1
# @ time 1
# . 2nd ya 3rd from reverse
'''
{
    ^ --> start with
    [a-z] ---> range pass 
    + ----> join all
    [\._]--->search any char in regex
    ?------->at a time 1 
    \w---->search in all string
    {}---->condition
    
    
    
    
}
'''

import re
email_condition="^[a-z]+[\._]?[a-z-0-9]+[@]\w+[.]\w{2,3}"
user_email=input("Enter the your email: ")

if re.search(email_condition,user_email):
    print("Valid email ")
else:
    print("Invalid email ")




