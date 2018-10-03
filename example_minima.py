import RPi.GPIO as GPIO


def init():
    # configuration de la broche 7 en entree
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.IN)
    # definition de l'interruption
    GPIO.add_event_detect(7, GPIO.RISING, callback=my_callback, bouncetime=300)


def my_callback():
    # callback = function which call when a signal rising edge on pin 7
    print("Vous avez appuyez sur le bouton de la patte 7")


if __name__ == '__main__':

    # 1- initiation de la l'interruption
    init()
    # 2- boucle infini = tache principale
    while True:
        pass
