# primi blocchi

# Le condizioni sono una struttura di controllo che serve per poter alterare il continuo verificarsi dei processi,
# che devono essere sempre opzionati


# condizione if-elif-else : permette di eseguire istruzioni o gruppi di istruzioni diverse a seconda del verificarsi di una o più condizioni
a = 22
b = 3
if b > a:                           # se || elemento di apertura del blocco | prima condizione da verificare
    print ('b è maggiore di a')
elif b == a:                        # invece se || elemento di concatenazione nelle condizioni opposte | seconda condizione da verificare
    print ('b è uguale ad a')
else:                               # altrimenti || elemento di chiusura del blocco
    print ('b è minore di a')


# in altre parole...
if condizione1:
    # gruppo di istruzioni da eseguire se la condizione1 è vera
elif condizione2:
    # gruppo di istruzioni da eseguire se la condizione2 è vera
elif condizioneN:
    # gruppo di istruzioni da eseguire se la condizioneN è vera
else:
    # gruppo di istruzioni da eseguire se tutte le condizioni sono false
    
    
# condizioni annidate : condizione if dentro altre condizioni if
# esempio:
test_vero = True

if test_vero != False:
    test_vero = False
    if test_vero == False:
        print (test_vero)
# il ragionamento logico è il seguente:
    # attribuiamo ad una variabile chiamata 'test_vero' il valore booleano 'False'
    # 1°condizione : se test_vero è diverso da False (quindi sì), cambiami il valore della variabile da 'True' a 'False'
    # 2°condizione : se test_vero è uguale a False (quindi sì), stampami il valore di 'test_vero' --> quindi False
    

# Comando input + altri modi per ottimizzare la stesura delle condizioni

# La funzione input viene usata per consentire all'utente di immettere dati da tastiera, che verranno poi utilizzati dal programma

# 1°esempio esempio di condizione annidata
n = int (input ('digita un numero: '))

if n > 0:
    print ('il numero è positivo')
else:
    if (n == 0):
        print ('il numero è 0')
    else:
        print ('il numero è negativo')

# questo blocco di codice si può riassumere in:
n = int (input ('digita un numero: '))     

if n > 0:
    print ('il numero è positivo')
elif n == 0:
    print ('il numero è 0')
else:
    print ('il numero è negativo')
    
    
# 2°esempio di condizione annidata:
x = 9

if x > 4:
   { print ('è superiore a 4') }
if x < 10:
   { print ('è minore di 10') }
   
# un modo per avere entrambe le condizioni verificate in meno codice è:
x = 9

{ print (x > 3 and x < 10)}
# la funzione and serve a controllare contemporaneamente la veridicità di più condizioni

# la funzione or invece serve a controllare che almeno anche solo una condizione sia vera
x = 9

{ print (x < 20 or x > 2)}
# quindi se anche solo una delle due condizioni sarà vera, l'intera condizione sarà verificata
