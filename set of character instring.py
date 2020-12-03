import re
def allowed_specific_character(string):
    charRe=re.compile(r"[^a-zA-Z0-9.]")
    string=charRe.search(string)
    return not bool(string)

print(allowed_specific_character("ABCDEFabvfdgee112"))
print(allowed_specific_character("$#%###@&*(("))
