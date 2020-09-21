#index   0   1    2   3  4   5   6
aldre = [15, 12, 15, 12, 13, 52, 17]

førstealder = aldre[0]
sidstealder = aldre[len(aldre)-1]

antal = len(aldre)
summen = sum(aldre)

print("Antallet: ", antal)
print("Summen: ", summen)
print("Gennemsnit: ", summen/antal)