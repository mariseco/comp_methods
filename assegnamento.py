""" First assigment.
""" # i doct strings, racchiusi tra tre pedici doppi, sono cose importanti
import argparse
import logging
import time


logging.basicConfig(level=logging.DEBUG)

def process(file_path):
    """ Read a text file and compile the letter statistics."""
    start_time = time.time()
    logging.info("Reading input file %s. . .", file_path)
    with open(file_path) as input_file:
        text = input_file.read()



    #il logging è fatto per stampare messaggi sopra un certo livello.. se un messaggio non lo stampiamo è inutile questo lavoro! Per stampare qualcosa dobbiamo impostare il logging a un livello più alto 36:00 vedi cos'è pylint.. digiti sul terminale - pylint assegnamento1.py-  ascolta a 46:00

if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help="Path to the input file")
    args = parser.parse_args()
    #30:00

    process(args.infile)

#chiamare le variabili in maniera espressiva
# la funzione ord('val') mi dà il valore di val in tabella ASCII
#char(val) mi dà il valore che corrisponde nella tabella ASCII a un mio carattere