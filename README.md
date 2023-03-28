# chnhash
<div style="background-color:#ffcc00; color:black;padding:5px;">
    This project is still in development mode and will be available to the public soon...
</div>

## Installation:
1. Download and extract the suitable zip file. You can use wget and unzip commands in Linux.
2. Run the setup.sh file with administrative privileges to perform the installation.
> sudo sh setup.sh

## Usage:
> chnhash.py \<TASK> \<ALGORITHM> \<FILE> \<RECEIVED HASH VALUE/FILE>

Compare the hash values:
> chnhash.py -c \<ALGORITHM> \<FILE> \<RECEIVED HASH VALUE/FILE>

Generate a new hash value:
> chnhash.py -g \<ALGORITHM> \<FILE>


chnhash.py -c sha512 test_files\File.txt test_files\received_hash.txt
