import time
import numpy as np
from algorithms import sort as sort


def bubbleTest(array):
    start = time.time()
    sort.bubble_sort(array)
    end = time.time()
    return end - start


def coctailTest(array):
    start = time.time()
    sort.cocktail_shaker_sort(array)
    end = time.time()
    return end - start


def mergeTest(array):
    start = time.time()
    sort.merge_sort(array)
    end = time.time()
    return end - start


intone = np.random.randint(1, 9999, 50)
inttwo = np.random.randint(1, 9999, 250)
intthree = np.random.randint(1, 9999, 500)
intfour = np.random.randint(1, 9999, 1000)
intfive = np.random.randint(1, 9999, 5000)
intsix = np.random.randint(1, 9999, 7500)

floatone = np.random.uniform(1, 9999, 50)
floattwo = np.random.uniform(1, 9999, 250)
floatthree = np.random.uniform(1, 9999, 500)
floatfour = np.random.uniform(1, 9999, 1000)
floatfive = np.random.uniform(1, 9999, 5000)
floatsix = np.random.uniform(1, 9999, 7500)

print('Bubble sort:')
print('Int 50 element array test: ' + str(bubbleTest(intone)) + 'sec')
print('Float 50 element array test: ' + str(bubbleTest(floatone)) + 'sec')
print('Int 250 element array test: ' + str(bubbleTest(inttwo)) + 'sec')
print('Float 250 element array test: ' + str(bubbleTest(floattwo)) + 'sec')
print('Int 500 element array test: ' + str(bubbleTest(intthree)) + 'sec')
print('Float 500 element array test: ' + str(bubbleTest(floatthree)) + 'sec')
print('Int 1000 element array test: ' + str(bubbleTest(intfour)) + 'sec')
print('Float 1000 element array test: ' + str(bubbleTest(floatfour)) + 'sec')
print('Int 5000 element array test: ' + str(bubbleTest(intfive)) + 'sec')
print('Float 5000 element array test: ' + str(bubbleTest(floatfive)) + 'sec')
print('Int 7500 element array test: ' + str(bubbleTest(intsix)) + 'sec')
print('Float 7500 element array test: ' + str(bubbleTest(floatsix)) + 'sec')

print('Coctail Shaker sort:')
print('Int 50 element array test: ' + str(coctailTest(intone)) + 'sec')
print('Float 50 element array test: ' + str(coctailTest(floatone)) + 'sec')
print('Int 250 element array test: ' + str(coctailTest(inttwo)) + 'sec')
print('Float 250 element array test: ' + str(coctailTest(floattwo)) + 'sec')
print('Int 500 element array test: ' + str(coctailTest(intthree)) + 'sec')
print('Float 500 element array test: ' + str(coctailTest(floatthree)) + 'sec')
print('Int 1000 element array test: ' + str(coctailTest(intfour)) + 'sec')
print('Float 1000 element array test: ' + str(coctailTest(floatfour)) + 'sec')
print('Int 5000 element array test: ' + str(coctailTest(intfive)) + 'sec')
print('Float 5000 element array test: ' + str(coctailTest(floatfive)) + 'sec')
print('Int 7500 element array test: ' + str(coctailTest(intsix)) + 'sec')
print('Float 7500 element array test: ' + str(coctailTest(floatsix)) + 'sec')

print('Merge sort:')
print('Int 50 element array test: ' + str(mergeTest(intone)) + 'sec')
print('Float 50 element array test: ' + str(mergeTest(floatone)) + 'sec')
print('Int 250 element array test: ' + str(mergeTest(inttwo)) + 'sec')
print('Float 250 element array test: ' + str(mergeTest(floattwo)) + 'sec')
print('Int 500 element array test: ' + str(mergeTest(intthree)) + 'sec')
print('Float 500 element array test: ' + str(mergeTest(floatthree)) + 'sec')
print('Int 1000 element array test: ' + str(mergeTest(intfour)) + 'sec')
print('Float 1000 element array test: ' + str(mergeTest(floatfour)) + 'sec')
print('Int 5000 element array test: ' + str(mergeTest(intfive)) + 'sec')
print('Float 5000 element array test: ' + str(mergeTest(floatfive)) + 'sec')
print('Int 7500 element array test: ' + str(mergeTest(intsix)) + 'sec')
print('Float 7500 element array test: ' + str(mergeTest(floatsix)) + 'sec')
