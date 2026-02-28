# ===========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
# ===========================================

# ===========================================
# Latihan 2: Tracing Rekursi
# ===========================================

def countdown(n):
    # base case
    if n == 0: 
        print("Selesai")
        return
    # proses sebelum rekursi
    print("Masuk:", n)
    # recursive case
    countdown(n-1)
    # proses setelah rekursi selesai
    print("Keluar", n)

# proses pemanggilan countdown(3)
# Masuk: 3
#   Masuk: 2
#       Masuk: 1
#           countdown(0)
#           Selesai  ← base case tercapai, return
#
# proses kembali (dari bawah ke atas):
# Keluar 1
# Keluar 2
# Keluar 3

countdown(3)