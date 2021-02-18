#my approach.(not in linear time )(basic approach)
#this algorithm handles all negative elements case also.
array = [-2 ,-3 ,-1 ,-4 ,-6]

#finding all contiguous non-empty subarrays. (n*(n+1)/2)
subarrays=[]
for x in range(len(array)):
    for i in range(len(array)-1):
        n = (i+x)+1
        if n<=len(array):
            subarrays.append(array[i:n])

#finding maximum possible sum of all contiguous non-empty subarrays.
print(max(list(sum(x) for x in subarrays)))


