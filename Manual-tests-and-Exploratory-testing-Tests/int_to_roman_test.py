from algorithms.strings import int_to_roman
#This is a manual test for int_to_roman.py
def int_to_roman_test(num, expected):
    result = int_to_roman(num)
    print("------------------------------------")
    print("make_sentence(str_piece, dictionaries) tesztje")
    print("------------------------------------")
    print("Number:          ", num)
    print("Expected result: ", expected)
    print("Result:          ", result)
    print("------------------------------------")
    print()

int_to_roman_test(3569, "MMMDLXIX")
int_to_roman_test(1234, "MCCXXXIV")
int_to_roman_test(187, "CLXXXVII")
int_to_roman_test(1, "I")
int_to_roman_test(3999, "MMMCMXCIX")
int_to_roman_test(0, "_nothing")
int_to_roman_test(-1, "_nothing")
int_to_roman_test(-165, "_nothing")
int_to_roman_test("asdf", "??????") #hibát dob
int_to_roman_test("1234", "MCCXXXIV") #hibát dob
int_to_roman_test(4000, "I̅V̅") #hibát dob