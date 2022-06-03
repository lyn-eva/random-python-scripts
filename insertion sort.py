import time
start = time.time()

array = [x for x in range(10000, 0, -1)]

sortedArray = [array[0]]
for j in range(1, len(array)-1):
   value = array[j]
   # j = i
   sortedArray.append(value)
   while j > 0 and sortedArray[j-1] < value:
      sortedArray[j] = sortedArray[j-1]
      j -= 1
   sortedArray[j] = value

# print(sortedArray)
print("time required in millisecond", time.time() - start)


# [1,3,68,2,6,69,46,5674,4]

# (n-1)(k)  = nk

# 1,2 p-3 --1 n-n+1
# 1,3,68 p-68 -- 2
# 1,3,68,2 p-2 --3
# 1,2,3,68,69 p-69 --4
# 1,2,3,68,69,46 p-46 --5
# 1,2,3,46,68,69,5674 p-5674 --6
# 1,2,3,46,68,69,5674,4 p-4 --7
# 1,2,3,4,46,68,69,5674


