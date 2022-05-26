from algorithms.strings import roman_to_int


# This is a manual test for roman_to_int.py
def roman_to_int_test(num, expected):
    result = roman_to_int(num)
    print("------------------------------------")
    print("make_sentence(str_piece, dictionaries) tesztje")
    print("------------------------------------")
    print("Number:          ", num)
    print("Expected result: ", expected)
    print("Result:          ", result)
    print("------------------------------------")
    print()


roman_to_int_test("MMMDLXIX", 3569)
roman_to_int_test("MCCXXXIV", 1234)
roman_to_int_test("CLXXXVII", 187)
roman_to_int_test("I", 1)
roman_to_int_test("MMMCMXCIX", 3999)
#roman_to_int_test("", 0)
roman_to_int_test("MMMM", 4000)
roman_to_int_test("MCMCMMILDMLC", -1) #szintaktikailag nem helyes római szám
roman_to_int_test("asdf", "??????")
