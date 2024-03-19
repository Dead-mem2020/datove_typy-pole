cislo = int(1) #tohle je datový typ celého čísla
cislo_float = float (3,23) #tohle je číslo s des, čárkou
text = str("String je sada znaků, například pro text")
boolean = True #Booleanská hodnota, značí buď pravdu/nepravdu (True/False)

#Pravý alt + f pro []
#Datový typ - pole, kde můžeme mít více prvků
#V poli se začíná na pozici 0, ačkoliv je délka pole 6, poslední prvek je na pozici 5
            #0      #1         #2     #3       #4          #5
arrays = ["Ford", "Porsche", "Audi", "BMW", "Mercedes", "Škoda"]

#Tohle vypíše úplně celé pole včetně hranatých závorek a uvozovek s čárkama
print(arrays)


#Vypíše pouze jeden prvek bez uvozovek, čárek a hranatých závorek. Vypíše jen to slovo
#Na pozici 1 se nachází string "Porsche"
print(arrays[1])

#Vypíše nám error, že není nic na pozici 6 v poli
print(arrays[6])

for x in arrays:
  print(x)