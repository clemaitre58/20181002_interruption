import RPi.GPIO as GPIO


# variable globale qui sera vue dans toutes les fonctions
flag_callback = False

def init():
    # configuration de la broche 7 en entree
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.IN)
    # definition de l'interruption
    GPIO.add_event_detect(7, GPIO.RISING, callback=my_callback, bouncetime=300)
    # initialisation du flag
    flag_callback = False


def my_callback():
    # function qui sera appelé lorsque le programme sur interrompu
    flag_callback = True


def process_ny_callback():
    print("Interruption détectée sur la broche 7")

if __name__ == '__main__':

    # 1- initiation de la l'interruption
    init()
    # 2- boucle infini = tache principale
    while True:
        # 3- si une interruption c'est produite alors on lance le traitement c
        # adéquat
        if flag_callback == True:
            process_ny_callback()
        pass
