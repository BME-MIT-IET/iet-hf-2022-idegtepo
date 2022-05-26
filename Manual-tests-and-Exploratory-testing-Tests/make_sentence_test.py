from algorithms.strings import make_sentence

# This is a manual test for reverse_string.py
def make_sentence_test(str_piece, dictionaries, result):
    res = make_sentence(str_piece, dictionaries)
    print("------------------------------------")
    print("make_sentence(str_piece, dictionaries) tesztje")
    print("------------------------------------")
    print("Expected result: ", result)
    print("Result:          ", res)
    print("------------------------------------")
    print()


make_sentence_test("thing", {"thing"}, 1)
make_sentence_test("applet", {"app", "let", "apple", "t", "applet"}, 3)
make_sentence_test("appletablet", {"app", "let", "apple", "t", "applet"}, 4)

