import random

print("şifre oluşturucusuna hoş geldiniz")
print("güçlü bir şifre\nEn az 8 karakterden oluşur.\nHarflerin yanı sıra, rakam ve “?, @, !, %, +, -, *, %” gibi özel karakterler içerir.\nBüyük ve küçük harfler bir arada kullanılır.")
print("şifre oluşturma işleminin başlaması için 'başla' yazınız")
while True:
  basla = input()
  if basla == "başla":
    karakterler = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '?', '@', '!', '%', '+', '-', '*', '%'
    ]
    
    sifre = ""
    for i in range(8):
        sifre += random.choice(karakterler)
    
    print("Oluşturulan şifre: " + sifre)