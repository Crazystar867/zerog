nama = "mr.ibrahim"
hobi = "main game"
lagu = "fighting my self"
umur = 20

print(f"halo {nama}, umur {umur} tahun!")
print(f"kamu suka {hobi}!, dan kamu suka dengerin {lagu}!")
print("ketik 'capek' atau 'seneng' buat lihat respon ku!")

pesan = input("kamu lagi gimana?")

if "capek" in pesan.lower():
    print(f"capek ya? mau {hobi} dulu?, {nama}!")
    print(f"atau mau dengerin {lagu}")

elif "seneng" in pesan.lower():
     print("kayak nya ada yang lagi seneng nih? habis gajian ya? haha")

else :
     print("aku selalu belajar dari kamu!")
