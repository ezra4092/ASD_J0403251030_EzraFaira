#==========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
#==========================================

#==========================================
# Latihan 5
#==========================================

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if ( ):
            result.append(left[i])
            i += 1
        
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Soal
# 1. Lengkapi kondisi agar menjadi ascending
# 2. Jelaskan fungsi result.extend()

# Jawaban
# 1. Tambahkan left[i] <= right[j]
def merge(left, right):
    #untuk menampung hasil penggabungan
    result = []

    #mulai dari index 0 untuk list left
    i = 0

    #mulai dari index 0 untuk list right
    j = 0

    #selama masih ada elemen di dua list
    while i < len(left) and j < len(right):

        #jika elemen left lebih kecil atau sama dengan right
        if left[i] <= right[j]:
            #tambahkan elemen left ke result
            result.append(left[i])
            i += 1
        
        #jika elemen left lebih besar dari right
        else:
            #tambahkan elemen right ke result
            result.append(right[j])
            j += 1
    #jika masih ada sisa elemen tambahkan semuanya ke result
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# 2. Pada proses merge sort, result.extend() digunakan untuk menambahkan sisa elemen dari salah satu list
# setelah while berhenti. Karena kedua list sudah terurut, sisa elemen pasti
# sudah pada posisi yang benar sehingga bisa langsung dimasukkan ke result.