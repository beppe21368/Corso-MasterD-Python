# il paradigma di Py è OOP
# i due livelli di tipizzazione (  DEBOLE come Py, FOTYE come Java  )


# variabili
# dato che al suo interno racchiude una tipologia di dati che possiamo utilizzare per gestire a livello tecnico un codice
# (contenitore di dati, che possono essere modificati, in una porzione di memoria)

# esempio:
x = 12          # int, intero || integer : può contenere solo numeri interi

x = "Gabri"     # str, stringa || string : può contenere qualsiasi combinazione di lettere e numeri all'interno degli apici --> ""

x = True        # bool, booleani : può contenere solo True o False

x = 123.23434   # float, numero complesso || float : può contenere numeri con la virgola fino alla determinata soglia

# ogni variabile è caratterizzata da un tipo di dato


# dati semplici: int, long (interi lunghi), float
# dati complessi: complex (numeri complessi), bool

# sequenze immutabili: str, tuple
# insiemi immutabili: list, dict


# Tipi di testo:
    # str, stringa: può contenere qualsiasi combinazione di lettere e numeri all'interno degli apici --> ""

# Tipi numerici:
    # -int, intero
    # -float
    # -complex

# Tipi di sequenze:
    # -list
    # -tuple
    # -range

# Tipi di mappatura:
    #-dict
    
# Tipi di set:
    #-set
    #-frozenset
    
# Tipi di booleani:
    # -bool
    
# Tipi binari:
    #-bytes
    # -bytearray
    # -memoryview
    
# Tipi None:
    # -NoneType


# comando print() : mandare a schermo il valore assegnato ad una variabile

# differenza tra = e == :
    # il segno = è un operatore di assegnazione e modifica tutto ciò che si trova sul lato sinistro dell'operatore,
    # prendendo il valore o la variabile che gli è stata assegnata
        # a = 1 # Setta il valore di "a" a 1 
        # b = a # Setta il valore di "b" assegnandogli il valore di "a" 
        
    # il segno == è un comparatore e confronta il valore di sinistra con quello di destra
        # a == b    # "a" è uguale a "b"
    # altri comparatori sono:
        # a != b    # "a" è disuguale da "b"
        # a < b     # "a" è minore di "b" 
        # a > b     # "a" è maggiore di "b" 
        # a <= b    # "a" è minore o uguale a "b" 
        # a >= b    # "a" è maggiore o uguale a "b" 


# come effettuare il casting di un dato:
    x = str (3)     # x ora è '3'
    x = int (1)     # x ora è 1
    x = float (9)   # x ora è 9.0
    
# analizziamo:
    x = str (3)     # x ora è '3'
    x2 = 3
    
print ( x2 == x )   # il risultato sarà False perchè la stringa e l'intero sono 2 tipi di dato diversi

# se invece confrontassimo:
    x = str (3)     # x ora è '3'
    x2 = '3'
    
print ( x2 == x )   # il risultato sarebbe True perchè confrontiamo 2 stringhe aventi stesso valore



