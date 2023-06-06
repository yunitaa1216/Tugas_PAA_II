import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Iterasi ke-{i + 1}: {arr}")
        time.sleep(1)  # Waktu delay setiap iterasi (opsional)

# Contoh penggunaan
arr = [53, 75, 87, 20, 100, 72]
print("Array awal:", arr)
start_time = time.time()
bubble_sort(arr)
end_time = time.time()
print("Array terurut:", arr)
print("Waktu eksekusi:", end_time - start_time, "detik")