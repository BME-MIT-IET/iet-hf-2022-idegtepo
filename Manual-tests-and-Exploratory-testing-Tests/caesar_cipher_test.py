from algorithms.strings import caesar_cipher

# This is a manual test for caesar_cipher.py
def caesar_chipher_test(string, rotation, expResult):
    result = caesar_cipher(string, rotation)
    print("------------------------------------")
    print("caesar_cipher(s, k) tesztje")
    print("------------------------------------")
    print("Expected result: ", expResult)
    print("Result:          ", result)
    print("------------------------------------")
    print()


caesar_chipher_test("default", 3, "ghidxow")
caesar_chipher_test("default", 1000, "pqrmgxf")
caesar_chipher_test("default", 0, "default")
caesar_chipher_test("default", -1, "cdeztks")
caesar_chipher_test("default", -123, "klmhbsa")
caesar_chipher_test("abc1~2ˇ3^4˘5", 3, "??????") #itt azt teszteljük történik-e bármi
caesar_chipher_test("pápópé", 3, "??????") #itt azt teszteljük, hogyan kezeli az ékezetes betűket
#caesar_chipher_test("default", "almafa", "?????") #A teszthez ki kell kapcsolni