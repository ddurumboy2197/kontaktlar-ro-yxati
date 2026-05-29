class Kontakt:
    def __init__(self, ism, telefon):
        self.ism = ism
        self.telefon = telefon

class KontaktlarRo'yhati:
    def __init__(self):
        self.kontaktlar = []

    def qo'sh_kontakt(self, ism, telefon):
        kontakt = Kontakt(ism, telefon)
        self.kontaktlar.append(kontakt)

    def o'chir_kontakt(self, ism):
        for kontakt in self.kontaktlar:
            if kontakt.ism == ism:
                self.kontaktlar.remove(kontakt)
                return

    def ko'rish_kontaktlar(self):
        for kontakt in self.kontaktlar:
            print(f"Ism: {kontakt.ism}, Telefon: {kontakt.telefon}")

    def ko'rish_kontakt(self, ism):
        for kontakt in self.kontaktlar:
            if kontakt.ism == ism:
                print(f"Ism: {kontakt.ism}, Telefon: {kontakt.telefon}")
                return

def main():
    kontaktlar_ro'yhati = KontaktlarRo'yhati()

    while True:
        print("1. Qo'sh kontakt")
        print("2. O'chir kontakt")
        print("3. Ko'rish kontaktlar")
        print("4. Ko'rish kontakt")
        print("5. Chiqish")

        savol = input("Izoh: ")

        if savol == "1":
            ism = input("Ism: ")
            telefon = input("Telefon: ")
            kontaktlar_ro'yhati.qo'sh_kontakt(ism, telefon)
        elif savol == "2":
            ism = input("Ism: ")
            kontaktlar_ro'yhati.o'chir_kontakt(ism)
        elif savol == "3":
            kontaktlar_ro'yhati.ko'rish_kontaktlar()
        elif savol == "4":
            ism = input("Ism: ")
            kontaktlar_ro'yhati.ko'rish_kontakt(ism)
        elif savol == "5":
            break
        else:
            print("Xato savol!")

if __name__ == "__main__":
    main()
