zbozi = ["CPU", "GPU", "HDD", "RAM", "SSD", "Motherboard", "Chlazení (vodní)", "Zdroj", "Case"]
kosik = []

print("Vítej v Techtownu! Máme zde ta nejlepší zařízení pro vaše PC! Zde je naše nabídka dne: ")

def nabidka(itemy):
    for x in range(len(itemy)):
        print(f"{x+1}: {itemy[x]}")
#odstranění (předání) a přidání itemů z jednoho pole do druhého
def premisteni(dk):
    kosik.append(dk)
    zbozi.pop(dk)
    print("Zde je stav vašeho e-košíku: ")
    nabidka(kosik)

nabidka(zbozi)
#Zadání čísel produktů uživatelem
dk = int(input("Zadejte číslo produktu pro umístění do vašeho košíku").split())

print(" ")
print = premisteni(kosik)