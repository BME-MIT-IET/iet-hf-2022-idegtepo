from algorithms import strings as strings

class TestData:
    def __init__(self):
        self.funcionName = "def"
        self.testName = "def"
        self.test_string= "def"
        self.test_string_reverse= "def"
        self.test_string_reverse_reverse= "def"
#This is a manual test for reverse_string.py
def printer(testData):
    print("-----------------------------------------")
    print(testData.funcionName+" tesztje")
    print(testData.testName)
    print("-----------------------------------------")
    print("Test:                 " + testData.test_string)
    print("Test reverse:         " + testData.test_string_reverse)
    print("Test reverse-reverse: " + testData.test_string_reverse_reverse)
    print("-----------------------------------------")
    print()

def recursive_reverse_string_test():
    testData = TestData()
    testData.funcionName = "recursive(s)"

    testData.testName = "Általános teszt"
    testData.test_string = "This is a test string."
    testData.test_string_reverse = strings.recursive(testData.test_string)
    testData.test_string_reverse_reverse = strings.recursive(testData.test_string_reverse)
    printer(testData)

    testData.testName ="Különleges karakteres teszt"
    testData.test_string = "¤ß$Łłí][Đđä*>;"
    testData.test_string_reverse = strings.recursive(testData.test_string)
    testData.test_string_reverse_reverse = strings.recursive(testData.test_string_reverse)
    printer(testData)

    testData.testName ="Ékezetes karakteres teszt"
    testData.test_string = "Égig érő fű."
    testData.test_string_reverse = strings.recursive(testData.test_string)
    testData.test_string_reverse_reverse = strings.recursive(testData.test_string_reverse)
    printer(testData)

def iterative_reverse_string_test():
    testData = TestData()
    testData.funcionName ="iterative(s)"

    testData.testName ="Általános teszt"
    testData.test_string = "This is a test string."
    testData.test_string_reverse = strings.iterative(testData.test_string)
    testData.test_string_reverse_reverse = strings.iterative(testData.test_string_reverse)
    printer(testData)

    testData.testName ="Különleges karakteres teszt"
    testData.test_string = "¤ß$Łłí][Đđä*>;"
    testData.test_string_reverse = strings.iterative(testData.test_string)
    testData.test_string_reverse_reverse = strings.iterative(testData.test_string_reverse)
    printer(testData)

    testData.testName ="Ékezetes karakteres teszt"
    testData.test_string = "Égig érő fű."
    testData.test_string_reverse = strings.iterative(testData.test_string)
    testData.test_string_reverse_reverse = strings.iterative(testData.test_string_reverse)
    printer(testData)

def pythonic_reverse_string_test():
    testData = TestData()
    testData.funcionName ="pythonic(s)"

    testData.testName ="Általános teszt"
    testData.test_string = "This is a test string."
    testData.test_string_reverse = strings.pythonic(testData.test_string)
    testData.test_string_reverse_reverse = strings.pythonic(testData.test_string_reverse)
    printer(testData)

    testData.testName ="Különleges karakteres teszt"
    testData.test_string = "¤ß$Łłí][Đđä*>;"
    testData.test_string_reverse = strings.pythonic(testData.test_string)
    testData.test_string_reverse_reverse = strings.pythonic(testData.test_string_reverse)
    printer(testData)

    testData.testName ="Ékezetes karakteres teszt"
    testData.test_string = "Égig érő fű."
    testData.test_string_reverse = strings.pythonic(testData.test_string)
    testData.test_string_reverse_reverse = strings.pythonic(testData.test_string_reverse)
    printer(testData)

def ultra_pythonic_reverse_string_test():
    testData = TestData()
    testData.funcionName ="ultra_pythonic(s)"

    testData.testName ="Általános teszt"
    testData.test_string = "This is a test string."
    testData.test_string_reverse = strings.ultra_pythonic(testData.test_string)
    testData.test_string_reverse_reverse = strings.ultra_pythonic(testData.test_string_reverse)
    printer(testData)

    testData.testName ="Különleges karakteres teszt"
    testData.test_string = "¤ß$Łłí][Đđä*>;"
    testData.test_string_reverse = strings.ultra_pythonic(testData.test_string)
    testData.test_string_reverse_reverse = strings.ultra_pythonic(testData.test_string_reverse)
    printer(testData)

    testData.testName ="Ékezetes karakteres teszt"
    testData.test_string = "Égig érő fű."
    testData.test_string_reverse = strings.ultra_pythonic(testData.test_string)
    testData.test_string_reverse_reverse = strings.ultra_pythonic(testData.test_string_reverse)
    printer(testData)

recursive_reverse_string_test()
iterative_reverse_string_test()
pythonic_reverse_string_test()
ultra_pythonic_reverse_string_test()