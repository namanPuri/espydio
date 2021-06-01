# espydio

*A command line utility built using python to automate audio file conversions, thereby assisting audio playing on ESP32 (primarily for [Tactile Tricorder](temp)).*

## Installation

- This requires that [SoX](http://sox.sourceforge.net/) version 14.4.2 or higher is installed with required handlers for MP3 files (path for excecutable file must be added to environment variables).

- To install the most up-to-date release of this module via PyPi:

    ```pip install espydio```

- To install the master branch:

    ```pip install git+https://github.com/namanPuri/espydio.git```

    or, **Simply clone the git repository and install setup.py.**

    ```shell
    git clone https://github.com/namanPuri/espydio.git
    cd espydio
    python setup.py install
    ```

## USAGE

Once ***espydio*** is installed, open any command-line tool and run :

```shell
    >espydio
```

If everything is good upto here, this must be recognised and you will get this as output.

```shell
usage: espydio [-h] {info,toWav,toHex,tts,stream,allToWav,allToHex,allToMp3,tth} ...
espydio: error: the following arguments are required: command
```

i.e.,
![Installation test](https://github.com/namanPuri/espydio/raw/master/docs/images/espydio_check.PNG)

### espydio - List of Commands

---

1. [info](#info)
2. [toWav](#toWav)
3. [toHex](#toHex)
4. [tts](#tts)
5. [stream](#stream)
6. [allToWav](#allToWav)
7. [allTohex](#allToHex)
8. [allToMp3](#allToMp3)
9. [tth](#tth)

To get a list of commands, in command-line tool itself with short description, you can run

```shell
>espydio -h
```

![espydioHelp](https://github.com/namanPuri/espydio/raw/master/docs/images/help.PNG)

### Command Descriptions and Examples

---

To get the description of using a particular command you can run:

```shell
>espydio <name of command> -h
```

![Command Usage](https://github.com/namanPuri/espydio/raw/master/docs/images/command_usage.PNG)

It will output the command usage and decription of it's required parameters.

## 1. info <a name="info"></a>

---

**Description:** This command can be used to print the details of the given audio file.

**Usage:** espydio info [-h] -n NAME_OF_FILE

**Example:**

![info-usage](https://github.com/namanPuri/espydio/raw/master/docs/images/info_usage.PNG)

## 2. toWav <a name="toWav"></a>

---

**Description:** This command converts the given MP3 or OGG file to WAV format with a sampling rate of 24khz and with sample encoding as 8-bit unsigned-integer PCM.

**Usage:** espydio toWav [-h] -i INPUT_FILE_NAME -o OUTPUT_FILE_NAME

**Example:**

![toWav-usage](https://github.com/namanPuri/espydio/raw/master/docs/images/toWav_usage.PNG)

**Comparing the details of MP3 file and converted Wav file.**

![Comparison](https://github.com/namanPuri/espydio/raw/master/docs/images/comparison.PNG)

## 3. toHex <a name="toHex"></a>

---

**Description:** This command converts the given WAV file to arduino-ide supported C header file containing the hex codes of the samples stored in an array with the required type qualifier to store the array in flash memory of the controller and not in RAM.

**Usage:** espydio toHex [-h] -n WAV_FILE_NAME -a ARRAY_NAME -o HEX_FILE_NAME

**Example:**

![toHex-usage](https://github.com/namanPuri/espydio/raw/master/docs/images/toHex_usage.PNG)

**C header would like this.**

![C-Header](https://github.com/namanPuri/espydio/raw/master/docs/images/c-header.PNG)

## 4. tts <a name="tts"></a>

---

**Description:** This command converts the given text to speech(MP3 format), with the desired language settings.

**Usage:** espydio tts [-h] -t TEXT -l LANGUAGE -o OUTPUT_MP3_FILE_NAME

**Example:**

![tts-usage](https://github.com/namanPuri/espydio/raw/master/docs/images/tts_usage.PNG)

## 5. stream <a name="stream"></a>

---

**Description:** Using this command, you can make a server using python and host any MP3 or WAV files of any duration on it. ESP32 can then be programmed to take the data from the server and play the same. You can verify that the server is created by copying the address appended with page to route, and running that address on any browser on same or some different device provided it should be connected to the same network.

**Usage:** espydio stream [-h] -r PAGE_TO_ROUTE -f FILE_NAME -t FILE_TYPE

**Example:**

![stream-usage](https://github.com/namanPuri/espydio/raw/master/docs/images/stream_usage.PNG)

## 6. allToWav <a name="allToWav"></a>

---

**Description:** This command converts all the MP3 files in the given directory to the corresponding WAV files, and store them in a folder with name WAV files in the working directory. The converted WAV files would have a sampling rate of 24khz and sample encoding as 8-bit unsigned-integer PCM. The name of the converted WAV file will be same as that of the MP3 one.

**Usage:** espydio allToWav [-h] [-i PATH_TO_FOLDER]

**Example:**

![allToWav-usage](https://github.com/namanPuri/espydio/raw/master/docs/images/allToWav_usage.PNG)

## 7. allToHex <a name="allToHex"></a>

---

**Description:** This command converts all the WAV files in the given directory to their corresponding hex codes and save them in a C-header file. The C-header file generated would have names of all arrays which it contains, commented in the beginning.

**Usage:** espydio allToHex [-h] [-i PATH_TO_FOLDER] -n HEX_FILE_NAME

**Example:**

![allToHex-usage](https://github.com/namanPuri/espydio/raw/master/docs/images/allToHex_usage.PNG)

**C-header file would look like this:**

![C-header](https://github.com/namanPuri/espydio/raw/master/docs/images/MIMO_header.PNG)

## 8. allToMp3 <a name="allToMp3"></a>

---

**Description:** This command converts the given texts or a range of numbers with the given step size and with specified language settings to speech in Mp3 format. The arguments for text and for numbers are mutually exclusive. The files generated would be stored in a folder with name MP3 files in the working directory.

**Usage:** espydio allToMp3 [-h] (-t TEXT [TEXT ...] | -r   ) -l LANGUAGE

**Example:**

![allToMp3-usage](https://github.com/namanPuri/espydio/raw/master/docs/images/allToMp3_usage.PNG)

## 9. tth <a name="tth"></a>

---

**Description:** This command converts the given texts or a range of numbers with the given step size and with specified language settings to their corresponding hex codes and save them all in a C-header file. The arguments for text and for numbers are mutually exclusive here too. The hex file generated with the given name will save in the folder with name as Hex file in the working directory.

**Usage:** espydio tth [-h] (-t TEXT [TEXT ...] | -r   ) -l LANGUAGE -n HEX_FILE_NAME

**Example:**

![tth-usage](https://github.com/namanPuri/espydio/raw/master/docs/images/tth_usage.PNG)

**C-header would look like:**

![tth-header](https://github.com/namanPuri/espydio/raw/master/docs/images/tth_header.PNG)
