# ciclo while

# il ciclo while itera fintanto che una condizione è vera
i = 0
while i < 6:        # condizionalità di ripetizione || finchè la condizione riporterà il valore 'True', essa si ripeterà
    print (i)       # printa la nostra variabile di iterazione
    i += 1          # aumenta la variabile di iterazione
# così manderemo a schermo tutti i valori in sequenza, partendo da 0 e concludendo con 5 e non 6
    
# Ragioniamo andando in sequenza:
#   - assegnamo alla variabile i valore 0
#   - impostiamo una condizione di ripetizione 
#   - a questo punto printiamo il valore della variabile e verrà mandato a schermo perchè la condizione è True
#   - la variabile ora prende il valore iniziale +1
#   - ora il ciclo si ripeterà in automatico fino a quando la condizione impostata riporterà la condizione True

# proviamo ora a spostare l'aumento della variabile di iterazione:
i = 0
while i < 6:
    i += 1
    print (i)
# in questo caso, manderemo a schermo tutti i valori in sequenza, partendo da 1 e concludendo con 6, perchè seguendo i passaggi
# in sequenza, avviene prima l'aumento della variabile rispetto che il comando print

# se non impostiamo una condizione di ripetizione, manderemo a schermo in loop il valore che abbiamo assegnato alla variabile,
# perchè il ciclo ricomincia sempre da essa, senza mai aumentare


# funzione continue : serve a saltare un valori presenti all'interno del ciclo:
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print (i)

# la logica del ciclo è uguale a prima, però quando il ciclo incontrerà valore == 3, questo verrà saltato e il ciclo riprenderà
# fino a quando la condizione di ripetizione sarà vera

# quindi in questo caso manderemo a schermo in sequenza tutti i valori da 1 a 5 senza il 3
# quando all'interno del ciclo avremo un valore che non rientrerà più nella condizione impostata, esattamente come con la funzione if,
# eseguiremo la funzione else, quindi in questo caso printeremo tutti i valori in sequenza compresi tra 1 e 5, escluso il 3, ripetendo
# alla fine il 5 (funzione else)


# la funzione break interrompe il ciclo ad una certa condizione:
i = 0
while i < 5:
    i += 1
    if i == 3:
        break
    print(i)
else:
    print (i)

# in questo caso manderemo a schermo in sequenza soltanto i valori 1 e 2


# altro esempio:
i = 0
x = 10
while 1 < 5 and x > 6:
    print (x, i)
    x -= 1
    i += 1
    
# in questo caso, manderemo a schermo in sequenza tutti i valori a coppie che, ciclando, rispettino la condizione impostata da noi