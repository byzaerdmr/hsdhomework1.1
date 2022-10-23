""" üniversite notunu kullanıcıdan alıp hangi harf notu ile geçtiğini hesaplama """
a=int(input("studentnote: "))
if (100>=a>=90):
    print("A")
elif (90>a>=80):
    print("B")
elif (80>a>=65):
    print("C")
elif (65>a>=0):
    print("D")
else:
    print("Böyle bir veri bulunamadı. Lütfen 0-100 arası bir değer giriniz!")