#6-misol
class Hamyon:
    def __init__(self, egasi, balans):
        self.egasi = egasi
        self.balans = balans

    def pul_korsat(self):
        print(f"Egasi: {self.egasi}")
        print(f"Balans: {self.balans} so'm")


class ElektronHamyon(Hamyon):
    def __init__(self, egasi, balans, xizmat):
        super().__init__(egasi, balans)
        self.xizmat = xizmat

    def pul_korsat(self):
        super().pul_korsat()
        print(f"Xizmat: {self.xizmat}")


hamyon = ElektronHamyon("Jasur", 150000, "Payme")
hamyon.pul_korsat()

#7-misol
class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif

    def malumot(self):
        print(f"Kitob: {self.nomi}")
        print(f"Muallif: {self.muallif}")

    def sotib_olish(self):
        print("Kitob sotib olindi.")


class ElektronKitob(Kitob):
    def __init__(self, nomi, muallif, format):
        super().__init__(nomi, muallif)
        self.format = format

    def malumot(self):
        super().malumot()
        print(f"Format: {self.format}")

    def sotib_olish(self):
        super().sotib_olish()
        print("Elektron nusxa yuklab olishga tayyor.")


kitob = ElektronKitob(
    "Python asoslari",
    "Anvar Narzullayev",
    "PDF"
)

kitob.malumot()
kitob.sotib_olish()

#8-misol
class Talaba:
    def __init__(self, ism, universitet):
        self.ism = ism
        self.universitet = universitet

    def malumot(self):
        print(f"Ism: {self.ism}")
        print(f"Universitet: {self.universitet}")

    def oqish(self):
        print("Talaba o'qimoqda.")


class ITTalaba(Talaba):
    def __init__(self, ism, universitet, mutaxassislik):
        super().__init__(ism, universitet)
        self.mutaxassislik = mutaxassislik

    def malumot(self):
        super().malumot()
        print(f"Mutaxassislik: {self.mutaxassislik}")

    def oqish(self):
        super().oqish()
        print(
            f"Talaba {self.mutaxassislik} "
            "yo'nalishida o'qimoqda."
        )


talaba = ITTalaba(
    "Muhammad",
    "Urganch davlat universiteti",
    "Backend dasturlash"
)

talaba.malumot()
talaba.oqish()


#9-misol
class Mahsulot:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narxi = narxi

    def malumot(self):
        print(f"Mahsulot: {self.nomi}")
        print(f"Narxi: {self.narxi} so'm")

    def chegirma(self):
        print("Mahsulotga chegirma berildi.")


class Elektronika(Mahsulot):
    def __init__(self, nomi, narxi, kafolat):
        super().__init__(nomi, narxi)
        self.kafolat = kafolat

    def malumot(self):
        super().malumot()
        print(f"Kafolat: {self.kafolat} oy")

    def chegirma(self):
        super().chegirma()
        yangi_narx = self.narxi - (self.narxi * 10 // 100)
        print(f"Chegirmadan keyingi narx: {yangi_narx} so'm")


mahsulot = Elektronika("Noutbuk", 8000000, 12)

mahsulot.malumot()
mahsulot.chegirma()

#10-misol
class Qahramon:
    def __init__(self, ism, jon):
        self.ism = ism
        self.jon = jon

    def malumot(self):
        print(f"Qahramon: {self.ism}")
        print(f"Jon: {self.jon}")

    def hujum(self):
        print("Qahramon hujum qilmoqda.")


class Jangchi(Qahramon):
    def __init__(self, ism, jon, qurol):
        super().__init__(ism, jon)
        self.qurol = qurol

    def malumot(self):
        super().malumot()
        print(f"Qurol: {self.qurol}")

    def hujum(self):
        super().hujum()
        print(f"{self.ism} {self.qurol} bilan hujum qilmoqda.")


jangchi = Jangchi("Knight", 100, "Qilich")

jangchi.malumot()
jangchi.hujum()
