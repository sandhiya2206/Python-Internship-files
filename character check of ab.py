import re
string1="This will give abnormal as ans"
string2="this will return No word found"

def character_check(string):
    word=re.compile("ab+\w*")
    word_found=word.findall(string)
    if len(word_found)!=0:
        for word in word_found:
            print("WORD")
    else:
        print(" NO WORD FOUND LIKE AB")

character_check(string1)

