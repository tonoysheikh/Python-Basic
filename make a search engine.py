import re

txt = "hello world"

s = input("Search here :")
test = re.search(s , txt)

if test :
    print("yes!find your text")
else :
    print("can't find your text")   