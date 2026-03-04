#==========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
#==========================================

#==========================================
# Latihan 2
#==========================================

def insertion_sort(data):
    for i in range(1, len(data)):
        
        key = data[i]
        j = i - 1 
        
        while j >= 0 and ( ) :
            data[j+1] = data[j]
            j -= 1
        
        ( )
    return data

# Soal
# 1. Lengapi kondisi agar menjadi sorting ascending.
# 2. Ubah agar menjadi descending.

# Jawaban
# 1
def insertion_sort(data):
    # loop mulai dari data kedua (index ke-1)
    for i in range(1, len(data)):
        
        key = data[i] # simpan nilai yang disisipkan
        j = i - 1 # index elemen terakhir di bagian kiri
        
        # geser ke kiri
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        # sisipkan key ke posisi yang benar
        data[j+1] = key
    return data

angka = [8,7,5,2,4]
print("Data awal: ",angka)
print("Hasil sorting: ",insertion_sort(angka))

# 2
def descending(data):
    for i in range(1, len(data)):
        
        key = data[i]
        j = i - 1 
        
        while j >= 0 and data[j] < key:
            data[j+1] = data[j]
            j -= 1
        
        data[j+1] = key
    return data

angka = [8,7,5,2,4]
print("\nData awal: ",angka)
print("Hasil sorting: ",descending(angka))