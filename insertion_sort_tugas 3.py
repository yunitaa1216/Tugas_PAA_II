# YUNITA ANGGERAINI
#  F55121070
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Iterasi ke-{i}: {arr}")
        time.sleep(1)  # Waktu delay setiap iterasi (opsional)

# Contoh penggunaan
arr =  [53, 75, 87, 20, 100, 72]
print("Array awal:", arr)
start_time = time.time()
insertion_sort(arr)
end_time = time.time()
print("Array terurut:", arr)
print("Waktu eksekusi:", end_time - start_time, "detik")