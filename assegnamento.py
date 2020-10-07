 """First assignment.
"""

import argparse
import logging
import time
import string


# [1]
logging.basicConfig(level=logging.DEBUG)


def process(file_path):
    """Reads a text file and compile the letter statistics."""
    
    
    start_time = time.time()


    #non ho fatto il logging.info(".." % file_path) perché il logging è intelligente: ha un livello ed è fatto solo per stampare i messaggi sotto un certo livello. Se un messaggio non lo stiampiamo è inutile formattarla questa strigna.Il log è fatto in modo che dopo la virgola passo gli argomenti della formatazzione e poi lui se la vede intermante solo se quel messaggio viene effettivamente stampato.
    #Tenendo solo questo non riesco a stampare nulla dunque va messo il log level a un livello più basso come si vede in [1]
    logging.info("Reading input file %s...", file_path)
    
    
    #apro il file.. devo capire la keyword "with", context menagment
    with open(file_path) as input_file:
        text = input_file.read()
    #facciamo una statistica sui caratteri
    num_chars = len(text)
    logging.info("Done, %d characters found.", num_chars)



    #creo un dizionario!
    # char_dict = {chr(x): 0 for x in range(ord('a'), ord('z') + 1)}
    char_dict = {ch: 0 for ch in string.ascii_lowercase}
    for ch in text:
        ch = ch.lower() #trasforma tutto in minuscolo forse
        if ch in char_dict:  #controllo che sia una chiave
            char_dict[ch] += 1
        # try:
        #     char_dict[ch.lower()] += 1
        # except KeyError:
        #     pass

    elapsed_time = time.time() - start_time
    logging.info("Done in %.3f seconds.", elapsed_time)
    
    #freq relative
    num_letters = sum(char_dict.values())
    for ch, num in char_dict.items():
        print(f"{ch} -> {num / num_letters:.3%}")
        
        
        
        
#########       PERCHE' USARE __main__?        #########


# Usando Python c'è una differenza fondamentale tra eseguire un file (modulo) e importare il contenuto di un modulo da un altro modulo. In particolare quando importiamo un modulo da un altro modulo, tutto quel che è in if __name__ == "__main__" non viene eseguito. Questa '__name__' è una cosa speciale. E' uguale a main quando il file viene chiamato stand alone, ovvero eseguito da solo. E' uguale a qualcos'altro quando questo non è vero.


# Prima di eseguire il codice, l’interprete Python legge il codice sorgente e definisce alcune variabili globali speciali, tra cui la variabile __name__ a cui viene assegnato il nome del modulo principale in esecuzione. Un modulo è un file contenente definizioni e dichiarazioni in Python. Il nome del file è il nome del modulo senza il suffisso .py.

#    Se l’interprete sta eseguendo quel modulo come programma principale (main), imposterà la variabile special __name__  ad avere un valore __main__. Se invece questo file viene importato da un altro modulo, allora __name__ verrà impostata con il nome del modulo.

#  Come potete vedere nei due casi il comportamento è completamente diverso. Infatti, abbiamo definito un file .py come un “modulo“. Questo perché nel file abbiamo una parte del codice come classi e funzioni, che generalmente vengono sviluppate per essere riutilizzate altrove. Quindi con il costrutto visto nell’articolo è possibile utilizzare, o riutilizzare altrove, differenziandone il comportamento. Lasciando nel “main” locale, una parte dell’implementazione valida solo nel contesto del file visto da solo e non come modulo.

# Come dice Baldini, serve in quanto non vogliamo un codice libero che fa qualcosa al di fuori di name uguale a main, altrimento questo modulo non possiamo importarlo senza che lui faccia quello ¿

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
   #serve per -help?
   
    parser.add_argument('infile', type=str, help="Path to the input file")
    
    #Il primo argomento è di quelli posizionali senza opzioni, obbligatorio, di default python ha il type stringa, se mi serve cambiarlo devo specificarlo! https://www.programmareinpython.it/video-corso-python-intermedio/09-il-modulo-argparse-pt1/ per capirci di più
    
    args = parser.parse_args()
    
   #se un programma ha bisogno di delle opzioni gli si danno opzioni di comando
    
    process(args.infile)
    
    
    
#############################################################

########                CHICCHE                         ######
# - Pylint è un'analizzatore statico di sintassi e si scrive da terminare così : pylint nomefile.py
