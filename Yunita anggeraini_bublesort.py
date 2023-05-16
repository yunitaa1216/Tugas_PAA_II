# Yunita anggeraini
# F55121070
# Kelas B
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        flag = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            break
    return arr
arr = [50, 10, 30, 40, 20]
sorted_arr = bubble_sort(arr)
print(sorted_arr)