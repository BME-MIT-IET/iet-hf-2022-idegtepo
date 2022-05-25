from algorithms import sort as sortAlgorithms
from algorithms import strings as stringAlgorithms
from algorithms import search as searchAlgorithms


def BubbleSortTestOne():
    originalList = [56, 87, 2, 45, 92]
    sortedList = [2, 45, 56, 87, 92]
    result = sortAlgorithms.bubble_sort(originalList)
    return sortedList == result


def BubbleSortTestTwo():
    originalList = [0.98, 0.44, 0.34, 0.78, 0.55, 0.45]
    sortedList = [0.34, 0.44, 0.45, 0.55, 0.78, 0.98]
    result = sortAlgorithms.bubble_sort(originalList)
    return sortedList == result


def CoctailShakerSortOne():
    originalList = [56, 87, 2, 45, 92]
    sortedList = [2, 45, 56, 87, 92]
    result = sortAlgorithms.cocktail_shaker_sort(originalList)
    return sortedList == result


def CoctailShakerSortTwo():
    originalList = [0.98, 0.44, 0.34, 0.78, 0.55, 0.45]
    sortedList = [0.34, 0.44, 0.45, 0.55, 0.78, 0.98]
    result = sortAlgorithms.cocktail_shaker_sort(originalList)
    return sortedList == result


def CaesarChiperTestOne():
    originalString = 'We are testing the code'
    codedString = 'Ai evi xiwxmrk xli gshi'
    result = stringAlgorithms.caesar_cipher(originalString, 4)
    return codedString == result


def CaesarChiperTestTwo():
    originalString = 'We are testing the code'
    codedString = 'Ks ofs hsghwbu hvs qcrs'
    result = stringAlgorithms.caesar_cipher(originalString, 14)
    return codedString == result


def SearchRangeTestOne():
    originalList = [2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 8, 8]
    resultList = [-1, -1]
    result = searchAlgorithms.search_range(originalList, 1)
    return resultList == result


def SearchRangeTestTwo():
    originalList = [5, 7, 7, 8, 8, 8, 10]
    resultList = [3, 5]
    result = searchAlgorithms.search_range(originalList, 8)
    return resultList == result


print('BubbleSortTestOne:')
print('\t' + str(BubbleSortTestOne()) + '\n')

print('BubbleSortTestTwo:')
print('\t' + str(BubbleSortTestTwo()) + '\n')

print('CoctailShakerSortOne:')
print('\t' + str(CoctailShakerSortOne()) + '\n')

print('CoctailShakerSortTwo:')
print('\t' + str(CoctailShakerSortTwo()) + '\n')

print('CaesarChiperTestOne')
print('\t' + str(CaesarChiperTestOne()) + '\n')

print('CaesarChiperTestTwo:')
print('\t' + str(CaesarChiperTestTwo()) + '\n')

print('SearchRangeTestOne:')
print('\t' + str(SearchRangeTestOne()) + '\n')

print('SearchRangeTestTwo:')
print('\t' + str(SearchRangeTestTwo()) + '\n')