import random
import string


string_length = int(input("enter length of string   :="))
res = "".join(random.choices(string.ascii_letters +
              string.digits, k=string_length))

# print("the generated string is  : {}".format(res))
print(res)
