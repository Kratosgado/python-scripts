data = """
    Hello there, My name is Nana Mbeah and I am just having fun with python.
    Do you want to earn money from google?

    contact me
    name: Prince Mbeah Essilfie
    email: mbeahessilfieprince@gmail.com
    twitter: https:twitter.com/mbeahessilfieljdsfl
"""

import re

def getEmail(data):
    pattern = r'\w*@gmail\.com'
    result =  re.search(pattern, data)


print(getEmail(data))