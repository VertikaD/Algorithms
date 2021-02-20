# code by Vertika Dhingra.
grid = [
    [0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1]
]

# logic: subtracting the first occurrence of 1 from len of row and print the max count's index
# here , I have used list comprehension and if any is used instead of break.
count = [i for i in grid if any(x for e, x in enumerate(i) if x == 1)]

print(count.index(max(count)))
