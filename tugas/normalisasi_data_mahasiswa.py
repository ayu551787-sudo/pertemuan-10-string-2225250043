# ==========================================
# Tugas 4: Normalisasi Data Mahasiswa
# ==========================================

def normalisasi_nama(nama):
    """Menghapus spasi berlebih di awal/akhir dan mengubah format menjadi title case."""
    # Menghilangkan spasi berlebih di ujung dan merapikan spasi antar kata, lalu .title()
    nama_bersih = " ".join(nama.strip().split())
    return nama_bersih.title()

def buat_inisial(nama):
    """Membuat inisial dari huruf awal setiap kata pada nama."""
    kata_list = normalisasi_nama(nama).split()
    inisial = ""
    for kata in kata_list:
        inisial += kata[0].upper()
    return inisial

def normalisasi_kode(kode):
    """Mengubah kode kelas menjadi huruf besar dan mengganti spasi dengan tanda hubung (-)."""
    # Menghapus spasi berlebih, ubah ke huruf kapital, pecah kata, lalu gabung dengan tanda '-'
    kode_bersih = "-".join(kode.strip().upper().split())
    return kode_bersih

# ==========================================
# Program Utama (Input & Eksekusi)
# ==========================================
if __name__ == "__main__":
    print("=" * 50)
    print("     PROGRAM NORMALISASI DATA MAHASISWA")
    print("=" * 50)
    
    # Menerima input dari pengguna
    nama_input = input("Nama       : ")
    kode_input = input("Kode kelas : ")

    # Memproses data menggunakan fungsi
    nama_hasil = normalisasi_nama(nama_input)
    kode_hasil = normalisasi_kode(kode_input)
    jumlah_kata = len(nama_hasil.split())
    inisial_hasil = buat_inisial(nama_input)

    # Menampilkan hasil normalisasi secara rapi sesuai format contoh output
    print("\n" + "-" * 50)
    print("--- HASIL NORMALISASI ---")
    print(f"Nama bersih : {nama_hasil}")
    print(f"Kode kelas  : {kode_hasil}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial     : {inisial_hasil}")
    
    # Format gabungan seperti pada Test Case Wajib
    print(f"\nFormat Gabungan:")
    print(f"{nama_hasil} | {kode_hasil} | {inisial_hasil}")
    print("=" * 50)