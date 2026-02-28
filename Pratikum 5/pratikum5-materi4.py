# ===========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
# ===========================================

# ===========================================
# Materi Backtracing 1: Kombinasi biner (n)
# ===========================================

def biner(n, hasil=""):
    #base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # choose + explore: tambah '0'
    biner(n, hasil + "0")

    # choose + explore: tambah '1'
    biner(n, hasil + '1')

biner(2)