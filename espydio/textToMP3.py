import requests
import os
import sys

####################################################################
#                  TEXT TO MP3 CONVERSION SISO                     #
####################################################################

def toMP3(TextToConvert,Language,OutputMP3File):
    if(os.path.splitext(OutputMP3File)[1] == '.mp3'):
        url = 'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=' + TextToConvert +\
              '&tl=' + Language + '&total=1&idx=0&textlen=9'
        try:
            r = requests.get(url, allow_redirects=True)
            open( OutputMP3File, 'wb').write(r.content)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit()
        print("TEXT TO SPEECH CONVERSION IS SUCCESSFUL !")
    else:
        print("ERROR : USE CORRECT EXTENSION !")
        sys.exit() 

#-------------------------------------------------------------------#

####################################################################
#               TEXT TO MP3 CONVERSION MISO STRING                 #
####################################################################
def allToMP3string(arr,lang):
    try:
        os.mkdir("MP3 files")
    except FileExistsError:
        print("MP3 files directory already exists. Appending Files in it !")
    
    for j in arr:
        toMP3(j, lang, "MP3 files/" + j + ".mp3")
#-----------------------------------------------------------------#

####################################################################
#               TEXT TO MP3 CONVERSION MISO NUMBERS                #
####################################################################
def allToMP3number(arr,lang):
    try:
        os.mkdir("MP3 files")
    except FileExistsError:
        print("MP3 files directory already exists. Appending Files in it !")
    
    for i in range(int(arr[0]),int(arr[1]) + 1, int(arr[2])):
        toMP3(str(i), lang, "MP3 files/" + str(i) + ".mp3")
#-----------------------------------------------------------------#

