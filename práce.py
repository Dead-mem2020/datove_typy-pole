arrays = ["Ford", "Porsche", "Audi", "BMW", "Mercedes", "Škoda"]

#Vypíše všechny pole v délce. která je rovna délce pole
for x in range(len(arrays)):
  print(f"{x+1}: {arrays[x]}")