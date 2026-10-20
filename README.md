
# Pertemuan 10 - String dan Pengolahan Teks

Nama: Ayu Syarifatu Zahra  
NIM: 2225250043  
Kelas: 3B

## Tujuan

Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan

Jalankan program melalui terminal dengan perintah berikut:

```bash
python3 tugas/normalisasi_data_mahasiswa.py
```

## Algoritma

Proses normalisasi data mahasiswa dilakukan melalui langkah-langkah berikut:

1. Menerima input data mahasiswa berupa teks.
2. Menghapus spasi berlebih di awal dan akhir teks menggunakan `strip()`.
3. Memisahkan teks menjadi beberapa kata menggunakan `split()`.
4. Menggabungkan kembali kata-kata menggunakan `join()` agar spasi lebih rapi.
5. Mengubah format penulisan nama menggunakan `title()`.
6. Menyesuaikan penggunaan huruf kapital dan huruf kecil sesuai kebutuhan.
7. Menampilkan hasil normalisasi data mahasiswa.

## Test Case

| No | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | `"  aan hendrayana, pmat a 2026  "` | `Aan Hendrayana PMAT-A-2026 AH` | Aan Hendrayana PMAT-A-2026 AH | sesuai |
| 2 | `"fATHIYYAH mUTHAMAINNAH, kelas b"` | `Fathiyyah Muthmainnah KELAS-B FM` | Fathiyyah Muthmainnah KELAS-B FM | sesuai |
| 3 | `"  BUDI, pmtk01 "` | `Budi, PMTK-01 B` | Budi, PMTK-01 B | sesuai |
| 4 | `"siti nur aisyah, kelas c"` | `Siti Nur Aisyah KELAS-C SNA` | Siti Nur Aisyah KELAS-C SNA | sesuai |

## Refleksi

Salah satu masalah yang dapat ditemukan dalam pengolahan teks adalah penulisan data yang tidak konsisten, seperti penggunaan huruf kapital yang tidak beraturan dan adanya spasi berlebih.

Untuk mengatasi masalah tersebut, digunakan beberapa fungsi string Python, yaitu:

- `strip()` untuk menghapus spasi di awal dan akhir teks.
- `split()` untuk memisahkan teks menjadi beberapa kata.
- `join()` untuk menggabungkan kembali kata dengan spasi yang rapi.
- `title()` untuk mengubah huruf pertama setiap kata menjadi kapital.
- `lower()` untuk mengubah seluruh huruf menjadi kecil.
- `upper()` untuk mengubah seluruh huruf menjadi kapital.

Dengan menggunakan fungsi-fungsi tersebut, data mahasiswa dapat dinormalisasi sehingga penulisannya menjadi lebih rapi, konsisten, dan mudah dibaca.
