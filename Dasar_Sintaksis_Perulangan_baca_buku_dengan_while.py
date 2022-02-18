"""
program perulangan mambaca buku dengan while
"""

jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
print(f'jumlah buku yang sudah di baca {jumlah_buku_yang_sudah_dibaca}')

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f'beku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca')

print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')
