#==========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
#==========================================

#==========================================
# Latihan 4
#==========================================

#fungsi merge sort untuk membagi data menjadi 2
def merge_sort(data):
    # error handling
    if len(data) <= 1:
        return data

    # membagi data menjadi 2
    mid = len(data) // 2
    left = data[:mid] # slicing data dari mid ke kiri
    right = data[mid:] # slicing dara dari mid ke kanan

    # recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

# Soal
# 1. Apa yang dimaksud dengan base case?
# 2. Mengapa fungsi memanggil dirinya sendiri?
# 3. Apa tujuan fungsi merge()?

# Jawaban
# 1. Base Case adalah kondisi dalam fungsi rekursif yang menandai titik pemberhentian perulangan,
# tanpa base case maka fungsi akan loop terus menerus.

# 2. Agar bisa memecahkan masalah kompleks menjadi sub-bagian masalah yang lebih kecil.

# 3. Fungsi merge dipanggil untuk menggabungkan dua bagian atau list terpisah yang sebelumnya
# sudah diurutkan agar menjadi satu list yang tetap terurut.
# Namun, kode ini akan error karena dalam kode yang diberikan di soal, def merge tidak ada.