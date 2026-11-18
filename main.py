from logger import Logger

l1 = Logger()
l1.log("démarrage")

l2 = Logger()
l2.log("conversion terminée")

print(l1 is l2)              # True
print(len(l1.tous_les_logs()))  # 2 — les deux logs dans la même BD