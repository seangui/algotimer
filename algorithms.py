
# Data of words to choose from for calculating Levenshtein Distance
words = ["its","college","dance","method","magnet","gentle","bowl","underline","spread","unknown"
"dot","oil","hold","brief","graph","stock","leaving","collect","reason","reader"
"declared","city","trunk","sort","during","pour","national","chamber","swimming","sense"
"since","said","boat","experience","thy","social","eager","school","better","whistle"
"famous","out","soil","swing","introduced","division","city","twenty","choice","foot"
"copy","rod","football","hunter","skin","kids","bow","master","strange","part"
"noon","especially","slept","cream","skill","machinery","street","wonderful","problem","principal"
"lake","this","shells","met","vegetable","mice","call","dirty","natural","bite"
"taste","noise","fence","beat","warn","continent","bicycle","author","exciting","happen"
"cook","leg","handle","dried","naturally","find","base","note","prepare","nor"
"older","western","winter","later","cage","appropriate","yesterday","studying","nest","hang"]

print(len(words))

# Levenshtein Distance Algorithm
def levenshtein_distance(A, B, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    if A[m - 1] == B[n - 1]:
        return levenshtein_distance(A, B, m-1, n-1)

    return 1 + min(
        levenshtein_distance(A, B, m, n-1),
        levenshtein_distance(A, B, m-1, n),
        levenshtein_distance(A, B, m-1, n-1)
    )

# Sorting Algorithms
def bubble_sort(list):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]

def selection_sort(list):
    for i in range(0, len(list) - 1):
        minIndex = i
        for j in range(i+1, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        if minIndex != i:
            list[i], list[minIndex] = list[minIndex], list[i]

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = key

# uses last element as pivot
def partition(list, low, high):
    i = (low - 1)
    pivot = list[high]
    for j in range(low, high):
        if list[j] <= pivot:
            i = i + 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[high] = list[high], list[i + 1]
    return (i + 1)

def quick_sort(list, low, high):
    if low < high:
        partitionIndex = partition(list, low, high)
        quick_sort(list, low, partitionIndex - 1)
        quick_sort(list, partitionIndex + 1, high)

def merge_sort(list):
    if len(list) > 1:
        mid = len(list)//2
        L = list[:mid]
        R = list[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i = i + 1
            else:
                list[k] = R[j]
                j = j + 1
            k = k + 1

        while i < len(L):
            list[k] = L[i]
            i = i + 1
            k = k + 1

        while j < len(R):
            list[k] = R[j]
            j = j + 1
            k = k + 1

def countingSort(list, place):
    n = len(list)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = list[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = list[i] // place
        output[count[index % 10] - 1] = list[i]
        count[index % 10] -= 1
        i = i - 1

    for i in range(0, n):
        list[i] = output[i]

def radix_sort(list):
    max_num = max(list)
    place = 1
    while max_num // place > 0:
        countingSort(list, place)
        place = place * 10
