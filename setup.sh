echo Installing tool : chnhash ...
python3 -m pip install filehash
mkdir /usr/bin/chnhash

cp chnhash.py /usr/bin/chnhash
cp compareHash.py /usr/bin/chnhash
cp appUpdater.py /usr/bin/chnhash

cd /usr/bin/chnhash
chmod +x chnhash.py
echo Installation process completed.