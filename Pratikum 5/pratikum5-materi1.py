# ===========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
# ===========================================

# ===========================================
# Materi Rekursif: Faktorial
# recursice case => 3! = 3 x 2 x 1 
# base case => 0 berhenti
# ===========================================

def faktorial(n):
    # base case
    if n == 0:
        return 1

    # recursive case
    return n*faktorial(n-1) # n-1"n-2"n-3 ....... n-?

print("===== Program Faktorial =====")
print("Hasil faktorial 3!:", faktorial(3))