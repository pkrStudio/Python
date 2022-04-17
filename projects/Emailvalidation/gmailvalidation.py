# must be >=6
# only one @ symbol ,start with lowercase alphabet
# . must be at 3rd or 4 th positin from last, no spaces

from itertools import count


email = input("Enter your email:=")  # g@g.in   pkr@.com
k = 0
d = 0
j = 0
if len(email) >= 6:
    if email[0].isalpha():
        if("@" in email) and (email.count("@") == 1):
            if(email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print('wrong email 5')
                else:
                    print("email is correct")
            else:
                print('wrong email 4')
        else:
            print('wrong email 3')

    else:
        print('wrong email 2')
else:
    print('wrong Email 1')
