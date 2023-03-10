import random

m = 10
L = []

for i in range(m):
    L.append(random.randint(-10, 10))
    print(L[i], end=' ')

# dodaj instrukcje wyszukiwania

def TaskOne (val, list):
    '''
    Search value in inputed list.
    @param list - inputed list;
    @param val - desired value;
    '''
    isFound = False
    for i in list:
        if not isFound:
            isFound = val == i 
    return isFound

# Smoke test of TaskOne()
a = TaskOne(m, L)
print(a)

def TaskTwo (list):
    '''
    Search MINIMAL value in inputed list.
    @param list - inputed list;
    '''
    min = False
    for i in list:
        if i < min:
           min = i
    return min

# Smoke test of TaskTwo()
b = TaskTwo(L)
print(b)