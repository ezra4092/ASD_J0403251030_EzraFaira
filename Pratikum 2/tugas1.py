# ============================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)

# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
# ============================================================

# ============================================================
# Konstanta Nama File 
# ============================================================
nama_file = "stok_barang.txt"


# ============================================================
# Fungsi: Membaca data dari file
# ============================================================
def baca_stok(nama_file):
    stok_dict = {}
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                baris = baris.strip()
                try:
                    kode_barang, barang, stok_int = baris.split(",")
                    stok_dict[kode_barang] = {
                        "nama_barang": barang,
                        "stok": int(stok_int)
                    }
                except (ValueError, IndexError): # file handling ketika data tidak sesuai dengan format
                    print(f"Data tidak valid, dilewati: {baris}") 
        return stok_dict
    except FileNotFoundError: # file handling ketika file tidak ditemukan
        open(nama_file, "w", encoding="utf-8").close()
        return {}


# ============================================================
# Fungsi: Menyimpan data ke file
# ============================================================
def simpan_stok(nama_file, stok_dict):
     with open(nama_file, "w", encoding="utf-8") as f:
            for kode_barang in stok_dict:
                barang = stok_dict[kode_barang]["nama_barang"]
                stok_int = stok_dict[kode_barang]["stok"]
                f.write(f"{kode_barang},{barang},{stok_int}\n")


# ============================================================
# Fungsi: Menampilkan semua data
# ============================================================
def tampilkan_semua(stok_dict):
    if len(stok_dict) == 0:
        print("Stok Kosong")
        return
    # Membuat Header Tabel
    print("\n========== Daftar Barang ==========")
    print(f"{'Kode':<10} | {'Nama Barang':<15} | {'Stok':<5}") # Mengatur Indentasi Pada Setiap Baris
    print("-" * 32)
    # Perulangan untuk menampilkan data
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama_barang"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<15} | {stok:<5}")


# ============================================================
# Fungsi: Cari barang berdasarkan kode
# ============================================================
def cari_barang(stok_dict):
    kode = input("Masukkan kode barang: ").strip()
    if kode in stok_dict:
        print("\n======= Barang ditemukan =======")
        print(f"Kode barang: {kode}")
        print(f"Nama barang: {stok_dict[kode]['nama_barang']}")
        print(f"Stok: {stok_dict[kode]['stok']}")
    else: 
        print("Barang tidak ditemukan.")


# ============================================================
# Fungsi: Tambah Barang Baru
# ============================================================
def tambah_barang(stok_dict):
    kode = input("Masukan kode barang baru (BRGxx): ")
    if kode in stok_dict:
        print("Kode sudah digunakan, proses dibatalkan.")
    else:
        nama = input("Masukan nama barang: " ).strip()
        try:
            stok = int(input("Masukan Stok Barang: ").strip())
            stok_dict[kode] = {
                "nama_barang": nama,
                "stok": stok
            }
            simpan_stok(nama_file, stok_dict)
            print("Barang berhasil ditambahkan.")
        except ValueError:
            print("Stok harus berupa angka.") # file handling jika pengguna mengetik lima (harusnya 5)
            return
        baca = baca_stok(nama_file)
        tampilkan_semua(baca)
    

# ============================================================
# Fungsi: Update Stok Barang
# ============================================================
def update_stok(stok_dict):
    kode = input("Masukkan kode barang yang akan diupdate jumlah stoknya: ").strip()
    if kode not in stok_dict:
        print("Kode tidak ditemukan, update dibatalkan.")
        return
    print("\n======= Pilih jenis update =======")
    print("1. Tambah Stok")
    print("2. Kurangi Stok")
    pilihan = int(input("Masukkan pilihan (1/2): ").strip())
    jumlah = int(input("Masukkan jumlah: ").strip())
    if pilihan == 1:
        stok_baru = stok_dict[kode]['stok'] + jumlah
    elif pilihan == 2:
        stok_baru = stok_dict[kode]['stok'] - jumlah
        if stok_baru < 0:
            print("Stok dibawah 0, update dibatalkan")
            return
    else:
        print("Pilihan tidak valid. Masukkan angka 1 atau 2.")
        return
    
    stok_dict[kode]["stok"] = stok_baru
    simpan_stok(nama_file, stok_dict)

    print("\n======= Update stok barang =======")
    print(f"Kode barang: {kode}")
    print(f"Nama barang: {stok_dict[kode]['nama_barang']}")
    print(f"Stok: {stok_baru}")


# ============================================================
# Fungsi: Hapus barang
# ============================================================
# def hapus_barang(stok_dict):
#     kode = input("Masukkan kode [BRGXX] yang akan dihapus nilainya: ")
#     if kode not in stok_dict:
#         print("Barang tidak ditemukan, update dibatalkan.")
#         return
#     try:
#         print("Barang tidak ditemukan, hapus dibatalkan")
#     except ValueError:
#         print("Stok tidak valid, update dibatalkan.")
#         return
#     target = stok_dict[kode]
#     sisa = [v for k, v in stok_dict.items() if v != target]

#     with open(nama_file, "w") as file:
#         for k, v in stok_dict.items():
#             if v != target:
#                 file.write(f"{k},{v['barang']},{v['stok']}\n")
#     stok_dict.pop(kode)
#     print("Data barang berhasil dihapus")
#     tampilkan_data(stok_dict)
    
# ============================================================
# Fungsi: Program utama
# ============================================================
def main(): 
    #Menjalankan fungsi 1 load data
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n========== Menu Stok Kantin ==========")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":    
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()  