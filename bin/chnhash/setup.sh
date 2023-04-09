<<LICENSE
chnhash provides you with the functionalities of generating and comparing hash values.
Copyright (C) 2022-2023 Himashana Suraweera (Email : Himashana@chnsoftwaredevelopers.com)

This file is part of chnhash.

chnhash is free software: you can redistribute it and/or modify it under the terms of the GNU General
Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

chnhash is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with chnhash. If not, see
<https://www.gnu.org/licenses/>.

LICENSE

echo ------------------------------------------------------------------------------------
echo Copyright \(C\) 2022-2023 Himashana Suraweera \(https:\\\\\\\\chnsoftwaredevelopers.com\)
echo Licensed under the terms of the GNU GPLv3
echo ------------------------------------------------------------------------------------

echo Installing tool : chnhash ...
python3 -m pip install filehash
mkdir /usr/bin/chnhash

cp chnhash.py /usr/bin/chnhash
cp compareHash.py /usr/bin/chnhash
cp generateHash.py /usr/bin/chnhash
cp appUpdater.py /usr/bin/chnhash

cd /usr/bin/chnhash
chmod +x chnhash.py
echo Installation process completed.