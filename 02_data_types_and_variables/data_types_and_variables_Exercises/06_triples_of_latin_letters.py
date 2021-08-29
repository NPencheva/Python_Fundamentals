number = int(input())

for letter1 in range(0, number):
    for letter2 in range(0, number):
        for letter3 in range(0, number):
            current_string = chr(97 + letter1) + chr(97 + letter2) + chr(97 + letter3)
            #print(f"{chr(97 + letter1)}{chr(97 + letter2)}{chr(97 + letter3)}")    #И ТОЗИ print РАБОТИ!!!!!!
            print(current_string)
# -----------------------------------------------------------------------
# number = int(input())
#
# a_small_letter_ascii = ord("a")
#
# for letter_1 in range(a_small_letter_ascii, a_small_letter_ascii + number):
#     for letter_2 in range(a_small_letter_ascii, a_small_letter_ascii + number):
#         for letter_3 in range(a_small_letter_ascii, a_small_letter_ascii + number):
#             print(f"{chr(letter_1)}{chr(letter_2)}{chr(letter_3)}")