from flask import Flask, Response
import os
import sys

####################################################################
#                    STREAM AUDIO ON HTTP                          #
####################################################################

def Stream(RouteTo,FileToStream,FileType):
    if not os.path.isfile(FileToStream):
        print('ERROR : THE FILE DOES NOT EXIST !')
        sys.exit()
    else:
        if((os.path.splitext(FileToStream)[1] == '.wav') or (os.path.splitext(FileToStream)[1] == '.mp3')):
            app = Flask(__name__)
            if(FileType == '.mp3' or '.MP3'):
                @app.route('/'+RouteTo)
                def streammp3():
                    def generate():
                        with open(FileToStream, "rb") as fmp3:
                            data = fmp3.read(1024)
                            while data:
                                yield data
                                data = fmp3.read(1024)
                    return Response(generate(), mimetype="audio/mp3")

            if(FileType == '.wav'):
                @app.route('/'+RouteTo)
                def streamwav():
                    def generate():
                        with open(FileToStream, "rb") as fwav:
                            data = fwav.read(1024)
                            while data:
                                yield data
                                data = fwav.read(1024)
                    return Response(generate(), mimetype="audio/mpeg")  

            print("Streaming at : http://192.168.1.16:5000/" + RouteTo)
    
            app.run(
                debug=True,
                host='0.0.0.0',
                port='5000'
                )
        else:
            print("ERROR : Give file in MP3 or WAV format!")
            sys.exit()

#------------------------------------------------------------------#
