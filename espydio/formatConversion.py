import os
import sox
import sys

################################################################
#                FORMAT CONVERSION TO WAV SISO                 #
################################################################
#MP3 and OGG are tested
def ConvertToWav(InputFilePath,OutputFilePath):
    if((os.path.splitext(OutputFilePath)[1] == '.wav') and (os.path.splitext(InputFilePath)[1] == '.mp3' or '.ogg')):
        tfm = sox.Transformer()
        tfm.set_output_format(file_type = 'wav', rate = 24000, bits = 8, channels = 1, encoding = 'unsigned-integer')
        try:
            tfm.build_file(InputFilePath, OutputFilePath)
        except OSError:
            print("ERROR : " + InputFilePath + " NOT FOUND!!")
            sys.exit()
        print(" SUCCESSFULLY CONVERTED "+ InputFilePath + " TO WAV! ")
    else:
        print("ERROR : Input or Output File is not in correct format!")
        sys.exit()

#-----------------------------------------------------------------#

################################################################
#                FORMAT CONVERSION TO WAV MIMO                 #
################################################################
#MP3 and OGG are tested
def allToWav(InputPath = '.'):
    mp3Files = []
    if(InputPath == '.'):
        InDirFiles = os.listdir(InputPath)
    else:
        try:
            InDirFiles = os.listdir(InputPath)
        except FileNotFoundError:
            print("ERROR : " + InputPath + " is not found!")
            sys.exit()
    if(InDirFiles == []):
        print("ERROR : THIS DIRECTORY IS EMPTY!")
        sys.exit()

    for i in InDirFiles:
        if(os.path.splitext(i)[1] == '.mp3'):
            mp3Files.append(i)

    if mp3Files == []:
        print("ERROR : No mp3 files found in the given directory!")
        sys.exit()

    try:
        os.mkdir("WAV files")
    except FileExistsError:
        print("WAV files directory already exists. Appending Files in it !")
    
    for j in mp3Files:
        ConvertToWav( InputPath + '/' + j, "WAV files/" + os.path.splitext(j)[0] + ".wav")
#-----------------------------------------------------------------#