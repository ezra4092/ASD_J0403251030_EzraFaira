#==========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
#==========================================

#==========================================
# Latihan 1
#==========================================


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

# Soal
# 1. Mengapa perulangan dimulai dari indeks 1? 
# 2. Apa fungsi variabel key?
# 3. Mengapa digunakan while, bukan for?
# 4. Operasi apa yang terjadi di dalam while?

# Jawaban
# 1. Karena proses penyisipan membutuhkan minimal satu elemen pembanding di sebelah kiri.
# Jika perulangan dimulai dari i = 0, maka key = data[0] dan j = -1. Kondisi while j >= 0 tidak terpenuhi sehingga tidak ada proses apa apa.

# 2. Fungsi variabel key adalah untuk menyimpan sementara elemen yang akan sedang dicari posisi yang benar. Kalau tidak disimpan terlebih dahulu, nilainya bisa tertimpa

# 3. Karena kita akan membandingkan semua elemen dan kita tidak tahu pasti berapa kali pergeseran akan terjadi. Pada while j >= 0 and data[j] > key
# kode akan menggeser ke kanan selama masih ada elemen di kiri dan nilainya lebih besar dari key.

# 4. Operasi perbandingan, yaitu membandingkan elemen di kiri dengan key (data[j] > key).
# Operasi pergeseran, menggeser elemen yang lebih besar ke kanan (data[j+1] = data[j]).
# Operasi pengurangan indeks, pindah satu langkah ke kiri untuk cek elemen berikutnya