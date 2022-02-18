"""
program perulangan mambaca buku dengan for
"""
jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
print(f'jumlah buku yang sudah di baca {jumlah_buku_yang_sudah_dibaca}')

print('dengan for')
for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f"buku ke {jumlah_buku_yang_sudah_dibaca} sudah di baca")

print(f'jumlah buku yang sudah di baca {jumlah_buku_yang_sudah_dibaca}')

print('tanpa for')
print('buku ke 1 sudah dibaca')
print('buku ke 2 sudah dibaca')
print('buku ke 3 sudah dibaca')
print('buku ke 4 sudah dibaca')
