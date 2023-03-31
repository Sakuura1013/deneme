meme_sozlugu = {
    "LOL": "Komik bir şeye verilen cevap",
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "ROFL": "Bir şakaya karşılık cevap",
    "SHEESH": "Onaylamamak",
    "CREEPY": "Korkunç",
    "TO AGGRO": "Agresifleşmek/Sinirlenmek"
}

print("Hoşgeldiniz!")

while True:
    kelime = input("Lütfen anlamadığınız bir kelimeyi büyük harf kullanarak yazın:")
    
    if kelime in meme_sozlugu.keys():
        print(meme_sozlugu[kelime])
    else:
        print("Bu kelime sözlüğümüzde yok.")
    
