import hashlib

nama1 = input("Nama awal: ")
email1 = input("Email awal: ")
hp1 = input("HP awal: ")

hash_awal = hashlib.md5(f"{nama1}{email1}{hp1}".encode()).hexdigest()
print("Hash awal:", hash_awal)

nama2 = input("\nNama baru: ")
email2 = input("Email baru: ")
hp2 = input("HP baru: ")

hash_baru = hashlib.md5(f"{nama2}{email2}{hp2}".encode()).hexdigest()
print("Hash baru:", hash_baru)

if hash_awal == hash_baru:
    print("Data tidak berubah.")
else:
    print("Data telah dimodifikasi!")