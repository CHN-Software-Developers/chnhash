@echo off

goto :start

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

:start

echo ------------------------------------------------------------------------------------
echo Copyright (C) 2022-2023 Himashana Suraweera (https://chnsoftwaredevelopers.com)
echo Licensed under the terms of the GNU GPLv3
echo ------------------------------------------------------------------------------------

echo Installing tool : chnhash ...

set current_dir=%cd%
set chn_root_dir=CHN Software Developers
set product_dir=chnhash

cd %ProgramFiles%

mkdir "%chn_root_dir%"
cd %chn_root_dir%
mkdir %product_dir%

cd %current_dir%

py -m pip install filehash

copy chnhash.py "%ProgramFiles%\%chn_root_dir%\%product_dir%"
copy chnhash.bat "%ProgramFiles%\%chn_root_dir%\%product_dir%"
copy compareHash.py "%ProgramFiles%\%chn_root_dir%\%product_dir%"
copy generateHash.py "%ProgramFiles%\%chn_root_dir%\%product_dir%"
copy appUpdater.py "%ProgramFiles%\%chn_root_dir%\%product_dir%"

setx PATH "%PATH%";"%ProgramFiles%\%chn_root_dir%\%product_dir%"

echo Installation process completed.