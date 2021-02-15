
import itertools
arr = [3, 7, 2, 5]

sum_arr = []
# dividing arr into pairs and calculating their sums.
sum_arr = [(x+y) for x, y in itertools.combinations(arr, 2)]
diff_arr = []
# dividing sum_arr into pairs and calculating their abs diff.
diff_arr = [abs(a-b) for a, b in itertools.combinations(sum_arr, 2)]
# finally,printing the minimum difference.
print(min(diff_arr))
