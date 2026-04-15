# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Ezra Faira Azzahra Faisal
# NIM     : J0403251030
# Kelas   : TPL B / P1
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
nama_file = "buku.txt"
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    # TODO: Implementasikan kode pembacaan file di sini
    database_buku = {}     # Dictionary kosong untuk menyimpan data buku
    
    try:
        # Membuka file dalam mode read (r) dengan encoding utf-8
        with open(nama_file, "r", encoding="utf-8") as f:
            # Membaca file baris per baris
            for baris in f:
                # Menghapus spasi lalu memecah data berdasarkan tanda koma
                kode_buku, judul, harga = baris.strip().split(",")
                try:
                    # Menyimpan data ke dictionary dengan kode_buku sebagai key
                    database_buku[kode_buku] = {
                    "judul" : judul, # Value judul buku
                    "harga" : int(harga) # Harga diubah menjadi int
                }
                except (ValueError, IndexError): # file handling ketika data tidak sesuai dengan format
                    print(f"Data tidak valid, dilewati: {baris}") 
        return database_buku # Mengembalikan dictionary berisi data buku
    
    except FileNotFoundError: # file handling ketika file tidak ditemukan
        open(nama_file, "w", encoding="utf-8").close()
        return {}

#  fungsi tambahan agar tampilan katalog lebih rapi
def tampilkan_katalog(database_buku):
    if len(database_buku) == 0:
        print("Stok Kosong")
        return
    # Membuat Header Tabel
    print("\n============= Katalog Buku =============")
    print(f"{'Kode':<8} | {'Nama Buku':<20} | {'Harga':<10}") # Mengatur Indentasi Pada Setiap Baris
    print("-" * 40)
    # Perulangan untuk menampilkan data
    for kode in sorted(database_buku.keys()):
        judul = database_buku[kode]["judul"]
        harga = database_buku[kode]["harga"]
        # Menampilkan data dengan format yang rapi
        print(f"{kode:<8} | {judul:<20} | {harga:<10}")


# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul):
        self.data = judul # Menyimpan data (judul buku)
        self.next = None # Pointer ke node berikutnya
        
class LinkedListPromosi:
    def __init__(self):
        self.head = None # Node pertama dalam Linked List

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        # TODO: Implementasikan penambahan node
        new_node = Node(judul) # Membuat node baru
        
        # jika linked list masih kosong
        if not self.head:
            self.head = new_node # Node baru menjadi head
            return
        temp = self.head # Mulai dari node pertama
        
        # Mencari node terakhir
        while temp.next:
            temp = temp.next
        temp.next = new_node # menghubungkan node terakhir dengan node baru

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        # TODO: Implementasikan traversal linked list
        current = self.head # Mulai dari node pertama
        
        # Traversal linked list sampe node terakhir
        while current is not None: 
            print(current.data) # menampilkan data node
            current = current.next # pindah ke node berikutnya
            
        

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
        
class AntreanKasir:
    def __init__(self):
        self.front = None # Elemen pertama dalam antrean
        self.rear = None # Elemen terakhir dalam antrean

    def is_empty(self):
        return self.front is None # Mengecek apakah antrean kosong
    
    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue)"""
        # TODO: Implementasikan prinsip FIFO
        nodeBaru = Node(nama_pelanggan) # Membuat node baru untuk pelanggan yang masuk

        # JIka antrean masih kosong, node baru menjadi front dan rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        # Menambahkan node baru di belakang antrean
        self.rear.next = nodeBaru
        self.rear = nodeBaru
        

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        # TODO: Implementasikan prinsip FIFO
        # JIka antrean kosong, tidak ada pelanggan yang bisa dilayani
        if self.is_empty():
            return None
        layani_pelanggan = self.front.data
        
        # mengambil pelanggan yang berada di depan antrean dan menghapusnya dari antrean
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return layani_pelanggan

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan 
    Insertion Sort atau Merge Sort.
    """
    # TODO: Implementasikan algoritma sorting secara manual
    # Perulangan mulai dari elemen kedua hingga akhir list
    for i in range(1, len(list_harga)):
        
        key = list_harga[i] # Elemen yang akan dibandingkan dengan elemen sebelumnya
        j = i - 1 # Membandingkan dengan elemen sebelumnya
        
        # Menggeser elemen yang lebih besar dari key ke posisi berikutnya
        while j >= 0 and list_harga[j] > key:
            list_harga[j+1] = list_harga[j]
            j -= 1
        
        # Menempatkan key pada posisi yang benar setelah elemen yang lebih besar telah digeser
        list_harga[j+1] = key
    return list_harga
    

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tampilkan_katalog(data_buku) # Menampilkan katalog buku
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            # VAlidasi input agar judul tidak kosong
            if judul_baru.strip() == "":
                print("Judul tidak boleh kosong")
            else:
                list_promosi.tambah_buku_promosi(judul_baru) # Menambahkan buku ke daftar promosi
            list_promosi.tampilkan_promosi() # Menampilkan daftar promosi setelah penambahan buku baru

        elif pilihan == '3':
            nama = input("Nama Pelanggan: ")
            
            # Menambahkan pelanggan ke antrean kasir
            antrean_toko.tambah_antrean(nama)
            print("Pelanggan berhasil ditambahkan ke antrian")
            
            # Melayani pelanggan di depan antrean
            dilayani = antrean_toko.layani_pelanggan()
            if dilayani is not None:
                print(f"Pelanggan Dilayani: {dilayani}")
            
        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()