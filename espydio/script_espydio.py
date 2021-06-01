#!/usr/bin/env python
import argparse  
import textwrap
from espydio import audioFileDetails, formatConversion, streamAudio, textToMP3, wavToHex

def main():

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,prog="espydio",\
                                    description=textwrap.dedent('''\

                    .____ .___      .    __   __ .____  .       __   ___   .___  .          .____   ___   .___           
                    /     /   \    /|    |    |  /      /       |  .'   `. /   \ /   /      /     .'   `. /   \          
                    |__.  |__-'   /  \   |\  /|  |__.   |       |  |     | |__-' |_-'       |__.  |     | |__-'          
                    |     |  \   /---'\  | \/ |  |      |  /\   /  |     | |  \  |  \       |     |     | |  \           
                    /     /   \,'      \ /    /  /----/ |,'  \,'    `.__.' /   \ /   \      /      `.__.' /   \          
                                                                                                                        
        _______     .      ___   _______ _ .     .____        _______ .___  _   ___    ___   .___  .___   .____  .___ 
        '   /       /|    .'   \ '   /    | /     /           '   /    /   \ | .'   \ .'   `. /   \ /   `  /      /   \\
            |      /  \   |          |    | |     |__.            |    |__-' | |      |     | |__-' |    | |__.   |__-'
            |     /---'\  |          |    | |     |               |    |  \  | |      |     | |  \  |    | |      |  \ 
            /   ,'      \  `.__,     /    / /---/ /----/          /    /   \ /  `.__,  `.__.' /   \ /---/  /----/ /   \\
                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                               
            '''))
    subparser = parser.add_subparsers(dest = 'command',required=True)

    info_parser = subparser.add_parser("info", help = "Gives Details of given audio file.")
    info_parser.add_argument("-n", help="Write file name in string format", metavar = "NAME_OF_FILE", type = str, required = True)

    convertToWav_parser = subparser.add_parser("toWav", help = "Converts the MP3/OGG file to WAV")
    convertToWav_parser.add_argument("-i", help="Write Input file name in string format",\
                                        metavar = "INPUT_FILE_NAME", type = str, required = True)
    convertToWav_parser.add_argument("-o", help="Write Output file name in string format",\
                                        metavar = "OUTPUT_FILE_NAME", type = str, required = True)

    convertToHex_parser = subparser.add_parser("toHex", help = "Converts the WAV file to C/C++ header file")
    convertToHex_parser.add_argument("-n", help="Write WAV file name in string format",\
                                        metavar = "WAV_FILE_NAME", type = str, required = True)
    convertToHex_parser.add_argument("-a", help="Write array name in string format",\
                                        metavar = "ARRAY_NAME", type = str, required = True)
    convertToHex_parser.add_argument("-o", help="Write HEX file name in string format",\
                                        metavar = "HEX_FILE_NAME", type = str, required = True)

    convertToSpeech_parser = subparser.add_parser("tts", help = "Converts the Text to Speech")
    convertToSpeech_parser.add_argument("-t", help="Write the text to be converted in string format",\
                                        metavar = "TEXT", type = str, required = True)
    convertToSpeech_parser.add_argument("-l", help="Choose language(en/hi)", metavar = "LANGUAGE",\
                                        type = str, required = True, choices=['en','hi'])
    convertToSpeech_parser.add_argument("-o", help="Write Output MP3 file name", metavar = "OUTPUT_MP3_FILE_NAME",\
                                        type = str, required = True)

    stream_parser = subparser.add_parser("stream", help = "Streams the given MP3/WAV file using HTTP")
    stream_parser.add_argument("-r", help="Write page name to route", metavar = "PAGE_TO_ROUTE", type = str, required = True)
    stream_parser.add_argument("-f", help="Write MP3 or WAV file name to stream", metavar = "FILE_NAME", type = str, required = True)
    stream_parser.add_argument("-t", help="Write type of file", metavar = "FILE_TYPE", type = str, required = True, choices=['.mp3','.wav'])

    alltowav_parser = subparser.add_parser("allToWav", help = "Converts the MP3 files in the given path to WAV files")
    alltowav_parser.add_argument("-i", help="Provide path to folder containing MP3 files. Ignore if files are in same folder",\
                                metavar = "PATH_TO_FOLDER", type = str)

    alltohex_parser = subparser.add_parser("allToHex", help = "Converts the WAV files in the given path to HEX")
    alltohex_parser.add_argument("-i", help="Provide path to folder containing WAV files. Ignore if files are in same folder",\
                                metavar = "PATH_TO_FOLDER", type = str)
    alltohex_parser.add_argument("-n", help="Enter the name of Hex file",\
                                metavar = "HEX_FILE_NAME", type = str, required = True)


    alltoMP3_parser = subparser.add_parser("allToMp3", help = "Converts the text into MP3 files")
    group  = alltoMP3_parser.add_mutually_exclusive_group(required = True)
    group.add_argument("-t", help="ENTER ANY NO. OF TEXTS",\
                    metavar = "TEXT", nargs = '+')
    group.add_argument("-r", help="Enter first no. then last no. then step",\
                    metavar = "", nargs = 3)
    alltoMP3_parser.add_argument("-l", help="Choose language(en/hi)", metavar = "LANGUAGE",\
                                type = str, required = True, choices=['en','hi'])

    texttoHex_parser = subparser.add_parser("tth", help = "Converts the texts or given range to hex file")
    group2  = texttoHex_parser.add_mutually_exclusive_group(required = True)
    group2.add_argument("-t", help="ENTER ANY NO. OF TEXTS",\
                    metavar = "TEXT", nargs = '+')
    group2.add_argument("-r", help="Enter first no. then last no. then step",\
                    metavar = "", nargs = 3)
    texttoHex_parser.add_argument("-l", help="Choose language(en/hi)", metavar = "LANGUAGE",\
                                type = str, required = True, choices=['en','hi'])
    texttoHex_parser.add_argument("-n", help="Name of Hex file", metavar = "HEX_FILE_NAME",\
                                type = str, required = True)

    args = parser.parse_args()

    if(args.command == "info"):
        audioFileDetails.PrintDetails(args.n)
    elif(args.command == "toWav"):
        formatConversion.ConvertToWav(args.i,args.o)
    elif(args.command == "toHex"):
        wavToHex.toHex(args.n,args.o,args.a)
    elif(args.command == "tts"):
        textToMP3.toMP3(args.t,args.l,args.o)
    elif(args.command == "stream"):
        streamAudio.Stream(args.r,args.f,args.t)
    elif(args.command == "allToWav"):
        if(args.i == None):
            formatConversion.allToWav()
        else:
            formatConversion.allToWav(args.i)
    elif(args.command == "allToHex"):
        if(args.i == None):
            wavToHex.allToHex(args.n)
        else:
            wavToHex.allToHex(args.n,args.i)
    elif(args.command == "allToMp3"):
        if(args.t != None):
            textToMP3.allToMP3string(args.t,args.l)
        elif(args.r != None):
            textToMP3.allToMP3number(args.r,args.l)
    elif(args.command == "tth"):
        if(args.t != None):
            textToMP3.allToMP3string(args.t,args.l)
        elif(args.r != None):
            textToMP3.allToMP3number(args.r,args.l)
        
        formatConversion.allToWav("MP3 files")
        wavToHex.allToHex(args.n,"WAV files")