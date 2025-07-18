# 🔐 AES ECB Encryption & Decryption Tool (Python)

Tool sederhana berbasis Python untuk mengenkripsi dan mendekripsi teks menggunakan algoritma **AES-128 ECB**. Mendukung input teks langsung maupun dari file `.txt`, serta output ke terminal atau disimpan kembali ke file.

---

## ✨ Fitur

✅ Enkripsi teks menggunakan AES-128 (ECB Mode)  
✅ Dekripsi ciphertext (format Base64)  
✅ Input teks bisa dari:
- Ketikan manual
- File `.txt`

✅ Output dekripsi bisa:
- Tampil langsung di terminal
- Disimpan ke file `.txt`

✅ Menu interaktif dengan pilihan:
- `1` Enkripsi
- `2` Dekripsi
- `0` atau `exit` untuk keluar

---

## 🧰 Persyaratan

- Python 3.x
- Library: `pycryptodome`

Instalasi library:
```bash
pip install pycryptodome

🚀 Cara Menjalankan
1. Clone Repo
git clone https://github.com/username/aes-tools.git
cd aes-tool
2. Jalankan Program
python AES.py
🧪 Contoh Penggunaan
🔒 Enkripsi
Pilih menu 1
Masukkan key (16 karakter)
Pilih input dari file (Y) atau manual (N)
Jika dari file, masukkan path file .txt
Hasil enkripsi (Base64) akan ditampilkan
🔓 Dekripsi
Pilih menu 2
Masukkan key yang sama (16 karakter)
Pilih input dari file (Y) atau manual (N)
Jika dari file, masukkan path file .txt
Pilih output ke file (Y) atau hanya tampil (N)


