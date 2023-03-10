def bubble_sort(T):
   n = len(T)
   i = n - 1
   while i >= 1:
        j = 0
        while j < i:
            if T[j] > T[j+1]:
               T[j], T[j+1] = T[j+1], T[j]
               print(True)
            else:
                print(False)
            j += 1
        i -= 1

Lista = [-2, 0, 4, -3, 2, 7, 1]
bubble_sort(Lista)
print(Lista)