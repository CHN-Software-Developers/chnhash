# chnhash

## Prerequisites
Windows users : [Download](https://www.python.org/downloads) and install python on your computer.

Linux users : Download and install the python and pip on your computer using the following commands.
> sudo apt-get install python3

> sudo apt-get install python3-pip

## Installation (Linux):
1. [Download](https://github.com/CHN-Software-Developers/chnhash/releases) and extract the "chnhash.zip" file. You can use wget and unzip commands in Linux.
2. Run the setup.sh file with administrative privileges to perform the installation.
> sudo sh setup.sh

## Installation (Windows):
1. [Download](https://github.com/CHN-Software-Developers/chnhash/releases) and extract the "chnhash.zip" file.
2. Start the command prompt with the administrative privileges (Run as administrator) and go to the downloaded chnhash folder through the command prompt and execute the setup.bat file.

>cd [downloaded chnhash folder]

>setup.bat

## Usage:
linux:
> /usr/bin/chnhash/chnhash.py \<TASK> \<ALGORITHM> \<FILE> \<RECEIVED HASH VALUE/FILE>

Windows:
> chnhash.py \<TASK> \<ALGORITHM> \<FILE> \<RECEIVED HASH VALUE/FILE>

Compare the hash values:
> chnhash.py -c \<ALGORITHM> \<FILE> \<RECEIVED HASH VALUE/FILE>

Generate a new hash value:
> chnhash.py -g \<ALGORITHM> \<FILE>

Example:
>chnhash.py -c sha512 test_files\File.txt test_files\received_hash.txt

>chnhash.py -g sha512 test_files\File.txt

## Troubleshoot:
- Linux:
If the tool fails to execute, try to run the chnhash tool using the following command,
> python3 /usr/bin/chnhash/chnhash.py \<TASK> \<ALGORITHM> \<FILE> \<RECEIVED HASH VALUE/FILE>

- If the issue cannot resolve, please [inform](https://github.com/CHN-Software-Developers/chnhash/issues) us: contact@chnsoftwaredevelopers.com

## Supported algorithms:

- sha1
- sha256
- sha512

> Other algorithms will be available soon.
