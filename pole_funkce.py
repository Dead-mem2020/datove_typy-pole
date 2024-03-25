cars = ["Ford", "Volvo", "BMW", "Audi"]

def vypis_pole(prvek):
    for x in range(len(prvek)):
        print(f"Auto s číslem {x+1}: {prvek[x]}")

vypis_pole(cars)
#Uložím do proměné prvek, který budu chtít přidat
prvek_plus = input("Zadejte auto, které chcete přidat")

print(" ")
#přidání prvku do pole
cars.append(prvek_plus)
vypis_pole(cars)


prvek_minus = int(input("Jakou pozici chcete odebrat? "))
cars.pop(prvek_minus)
vypis_pole(cars)