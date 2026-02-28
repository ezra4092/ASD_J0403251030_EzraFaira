# ===========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
# ===========================================

# ===========================================
# Latihan 1: Rekursi Pangkat
# ===========================================

def pangkat(a, n):
    #base case
    if n == 0:
        return 1
    # recursive case
    return a * pangkat(a, n-1)

# proses pemanggilan pangkat(2,4)
# 2 * pangkat(2,3)
#   2 * pangkat(2,2)
#       2 * pangkat(2,1)
#           2 * pangkat(2,0)
#               ketika n == 0, return 1
#
# proses pengembalian nilai (dari bawah ke atas):
# pangkat(2,0) = 1
# pangkat(2,1) = 2 * 1 = 2
# pangkat(2,2) = 2 * 2 = 4
# pangkat(2,3) = 2 * 4 = 8
# pangkat(2,4) = 2 * 8 = 16

print(pangkat(2,4)) #output : 16