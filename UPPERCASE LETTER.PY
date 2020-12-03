import re
def uppercase_letter(text):
    pattern="^[A-Z]*$"
    if re.search(pattern,text):
        print("UPPERCASE IS MATCHED!")
    else:
        print("UPPERCASE IS NOT MATCHED!!")

uppercase_letter("SANDHIYA")
uppercase_letter("sandhiya")
