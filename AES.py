from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(plaintext, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(ciphertext).decode()

def decrypt(ciphertext, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(base64.b64decode(ciphertext))
        return unpad(decrypted, AES.block_size).decode()
    except Exception as e:
        return f"[!] Gagal dekripsi: {str(e)}"

def get_input_text(mode):
    opsi = input("Pilih sumber input (1.ketik manual / 2.baca dari file.txt): ")
    if opsi == '1':
        return input("Masukkan teks: ")
    elif opsi == '2':
        path = input("Masukkan nama file .txt: ")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print("[!] File tidak ditemukan.")
            return None
    else:
        print("[!] Pilihan tidak valid.")
        return None

def save_to_txt(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[+] Hasil disimpan ke file: {filename}")

def main():
    print("=== AES-128 ECB Tool ===")
    while True:
        print("\nPilih mode:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("0. Keluar")
        mode = input("Pilihan: ").strip()

        if mode in ['0', 'exit']:
            print("Keluar dari program.")
            break

        key = input("Masukkan key (16 karakter): ")
        if len(key) != 16:
            print("[!] Key harus 16 karakter.")
            continue

        text = get_input_text(mode)
        if text is None:
            continue

        if mode == '1':
            hasil = encrypt(text, key)
            print("\n[+] Ciphertext (Base64):", hasil)

        elif mode == '2':
            hasil = decrypt(text.strip(), key)
            print("\n[+] Plaintext:", hasil)

            simpan = input("Simpan plaintext ke file? (y/n): ").lower()
            if simpan == 'y':
                save_to_txt("hasil_dekripsi.txt", hasil)

        else:
            print("[!] Mode tidak valid.")

if __name__ == "__main__":
    main()
