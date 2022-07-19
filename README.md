# timelapse_raspberrypI
Come creare animazioni time-lapse con la Pi Camera

Vediamo come scrivere un programma in python capace di scattare foto con una Pi Camera collegata ad un Raspberry Pi, quindi di incollare tutti gli scatti per creare una GIF.

I materiali da utilizzare sono i seguenti:

Raspbian
Raspberry Pi Board
Micro SD
Pi Camera
Connessione a internet
FASE PRELIMINARE

Aggiorniamo Raspberry Pi OS con i comandi


`sudo apt-get update`
`sudo apt-get upgrade`

INSTALLAZIONE RASPBERRY PI CAMERA

Ho scritto una guida approfondito a riguardo, per leggerla potete utilizzare il seguente link: [Come installare e configurare la Raspberry Pi Camera](https://www.moreware.org/wp/blog/2021/11/02/come-creare-animazioni-time-lapse-con-la-pi-camera/)

COSA INSTALLARE?

Dobbiamo installare il tool di animazione con il comando:

`sudo apt install imagemagick -y`

Dobbiamo installare la libreria pi camera con il comando:

`sudo pip3 install picamera`

CODICE PYTHON

Salviamo lo script con il nome timelapse.py.

[CODICE](https://github.com/SimoneMoreWare/timelapse_raspberrypI/blob/main/timelapse.py)

Spieghiamo il codice:

Importiamo le diverse librerie

`from picamera import PiCamera 
from os import system
from time import sleep`

Inizializziamo la PiCamera

`camera = PiCamera ()`
Impostiamo la risoluzione:

`camera.resolution = (1920, 1080)`
In questo ciclo for cosa facciamo? Scattiamo N foto ogni intervallo T di tempo. Quindi:

`for i in range(N): 
   camera.capture(‘/home/pi/Desktop/timelapse/image{0:04d}.jpg’.format(i)) 
   sleep(T)`

Questa istruzione permette di convertire tutte le immagini in gif: La gif sarà salvata sul desktop.


`system(‘convert -delay 1 -loop 0 home/pi/Desktop/timelapse/image*.jpg animation.gif’)`

TEST

Esegui il codice, dopo 40 secondi vedrai la tua gif sul desktop.
