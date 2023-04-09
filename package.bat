@echo off

mkdir bin
mkdir bin\chnhash

copy chnhash.py bin\chnhash
copy chnhash.bat bin\chnhash
copy compareHash.py bin\chnhash
copy generateHash.py bin\chnhash
copy appUpdater.py bin\chnhash

copy setup.bat bin\chnhash
copy setup.sh bin\chnhash
copy uninstall.bat bin\chnhash
copy uninstall.sh bin\chnhash

copy LICENSE.txt bin\chnhash
copy README.md bin\chnhash

cd bin
tar.exe -a -cf chnhash.zip chnhash
cd ..