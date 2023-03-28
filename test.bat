@echo off
mkdir Testing_env
copy test_files\* Testing_env
copy Testing\test.py Testing_env
copy compareHash.py Testing_env
copy generateHash.py Testing_env
cd Testing_env
py test.py
cd ..