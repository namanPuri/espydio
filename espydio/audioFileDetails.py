import os
import subprocess
import sys
 
###########################################################
#                 AUDIO FILE DETAILS                      #
###########################################################

def PrintDetails(FilePath):
    if not os.path.isfile(FilePath):
        print('ERROR : THE FILE DOES NOT EXIST !')
        sys.exit()
    else:
        try:
            process = subprocess.run(["sox","--i",FilePath], capture_output=True, check =True)
        except:
            print("ERROR : GIVE AUDIO FILE AS INPUT !")
            sys.exit()
        print(process.stdout.decode())

#---------------------------------------------------------#