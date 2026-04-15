def selection_sort(data):
    for i in range(len(data)):
        min_index = i # sebagai nilai terkecil sementara, indeks ke-0

        # perulangan kedua, mencari apakah ada nilai yang lebih kecil dari posisi min_index
        for j in range (i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j # kalau ada, min_index akan diperbarui
   
        temp = data[i]
        data[i] = data[min_index]
        data[min_index] = temp

    return data

data = [3,6,2,8,7,2,5,1]

print("Data sebelum diurutkan", data)
print("Data sesudah diurutkan", selection_sort(data))
