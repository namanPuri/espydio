import binascii
import os
import sys
####################################################################
#                  WAV TO HEX CONVERSION SISO                      #
####################################################################

def toHex(InputWavFile,OutputHexFile,NameOfArray,appendmode = False):
    if(os.path.splitext(InputWavFile)[1] == '.wav'):
        fixed_n = 12
        try:
            file_stats = os.stat(InputWavFile)
        except FileNotFoundError:
            print("ERROR : " + InputWavFile + " NOT FOUND!!")
            sys.exit()
        if(appendmode == False):
            with open(OutputHexFile, "w") as f1:
                f1.write("/* This header contains these arrays -- " + NameOfArray + " */\n")
                f1.write("\nconst unsigned char PROGMEM " + NameOfArray +\
                        "["+str(file_stats.st_size)+"] = {\n\t")

                with open(InputWavFile, "rb") as f:
                    byte = f.read(1)
                    i = 1
                    j = 1
                    while byte:
                        if(i < file_stats.st_size):
                            f1.write('0x'+str(binascii.hexlify(byte).decode()) + ', ')
                        elif(i == file_stats.st_size):
                            f1.write('0x'+str(binascii.hexlify(byte).decode()) + '\n};')
                        if(j == fixed_n):
                            f1.write('\n\t')
                            j = 0
                        byte = f.read(1)
                        i += 1
                        j += 1
        elif(appendmode == True):
            with open(OutputHexFile, "a") as f1:
                f1.write("\nconst unsigned char PROGMEM " + NameOfArray +\
                        "["+str(file_stats.st_size)+"] = {\n\t")

                with open(InputWavFile, "rb") as f:
                    byte = f.read(1)
                    i = 1
                    j = 1
                    while byte:
                        if(i < file_stats.st_size):
                            f1.write('0x'+str(binascii.hexlify(byte).decode()) + ', ')
                        elif(i == file_stats.st_size):
                            f1.write('0x'+str(binascii.hexlify(byte).decode()) + '\n};')
                        if(j == fixed_n):
                            f1.write('\n\t')
                            j = 0
                        byte = f.read(1)
                        i += 1
                        j += 1
        print(" SUCCESSFULLY CONVERTED TO HEX FILE! ")
    else:
        print("ERROR : " + InputWavFile + " IS NOT A WAV FILE!!")
        sys.exit()

#----------------------------------------------------------------------------------#

####################################################################
#                  WAV TO HEX CONVERSION MISO                      #
####################################################################

def allToHex(NameHexFile, InputPathToWav = '.'):
    wavFiles = []
    if(InputPathToWav == '.'):
        DirFiles = os.listdir(InputPathToWav)
    else:
        try:
            DirFiles = os.listdir(InputPathToWav)
        except FileNotFoundError:
            print("ERROR : " + InputPathToWav + " is not found!")
            sys.exit()
    if(DirFiles == []):
        print("ERROR : THIS DIRECTORY IS EMPTY!")
        sys.exit()

    for i in DirFiles:
        if(os.path.splitext(i)[1] == '.wav'):
            wavFiles.append(i)

    if wavFiles == []:
        print("ERROR : No mp3 files found in the given directory!")
        sys.exit()

    try:
        os.mkdir("HEX file")
    except FileExistsError:
        print("HEX file directory already exists. Appending Files in it !")

    for k in os.listdir("HEX file"):
        if(k == os.path.basename(NameHexFile)):
            print("ERROR : " + NameHexFile + " already exists.")
            sys.exit()
    else:
        with open("HEX file/" + NameHexFile, "a") as f1:
            f1.write("/* This header contains these arrays --  */\n")
            for m in wavFiles:
                if(m[0].isdigit()):
                    p = '_' + m
                else:
                    p = m
                f1.write("// \t\t\t -- \t" + os.path.splitext(p)[0].replace(" ", "") + "\n")
            f1.close()

        for j in wavFiles:
            if(j[0].isdigit()):
                k = '_' + j
                print(os.path.splitext(j)[0] + " is not a valid C array name. Array will be named as: " + "_" + os.path.splitext(j)[0] )
            else:
                k = j
            toHex( InputPathToWav + '/' + j, "HEX file/" + NameHexFile, os.path.splitext(k)[0].replace(" ", ""), True)
    
#-----------------------------------------------------------------------------------------------------------------------------#