import time
start  = time.time()

array = [x for x in range(10000, 0, -1)]
n = 1
for j in array:
   sort = False
   for i in range(len(array) - n):
      if array[i] > array[i+1]:
         array[i], array[i+1] = array[i+1], array[i]
         sort = True
   if not sort:
      break
   n += 1

# print(array)
print("time requiered in millisecond:", time.time() - start)

# worst case = o(n^2)
# average case = o(n^2)
# best case = o(n)
