import re
def check_number_at_end_of_word(string):
    number=re.compile(r".*[0-9]$")
    if number.match(string):
        print("THE NUMBER FOUND AT THE END OF WORD")
    else:
        print("THE NUMBER NOT FOUND AT THE END OF WORD")

check_number_at_end_of_word("SANDHIYA4455")
check_number_at_end_of_word("SANDHIYA")
