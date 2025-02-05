import random
import matplotlib.pyplot as plt

sonuclar = [random.choice(["Yazı", "Tura"]) 
            for _ in range (10000)]

yazi_sayisi = sonuclar.count("Yazı")
tura_sayisi = sonuclar.count("Tura")


labels = ["Yazı", "Tura"]
sizes = [yazi_sayisi, tura_sayisi]
colors = ["red", "blue"]

plt.bar(labels, sizes, color=colors)

plt.title("10000 Adet Yazı Tura atışının Dağılımı")
plt.xlabel("Sonuç")
plt.ylabel("Frekans")

plt.show()
