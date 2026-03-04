#==========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
#==========================================

#==========================================
# Insertion Sort (Ascending)
#==========================================

def insertion_sort(data):
    # melihat data awal
    print("Data awal", data)
    print("="*50)

    # loop mulai dari data kedua (index ke-1)
    for i in range(1, len(data)):

        key = data[i] # simpan nilai yang disisipkan
        j = i - 1 # index elemen terakhir di bagian kiri

        print("Iterasi ke-:", i)
        print("Nilai key :", key)
        print("Bagian kiri (terurut):", data[:i])
        print("Bagian kanan (blm terurut):", data[i:])
        
        # geser
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        # sisipkan key ke posisi yang benar
        data[j+1] = key
        print("Setelah disisipkan ke kiri:", data)
        print("=" * 50)
    return data

angka = [5, 2, 4, 6, 1, 3]
print("Hasil sorting: ",insertion_sort(angka))


        