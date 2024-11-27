@echo off
echo File/Folder Decryption Tool
echo ------------------------
echo This will decrypt your files in place.
echo.
echo You can enter either:
echo  - A path to a single encrypted file
echo  - A path to a folder to decrypt all files inside it
echo.
set /p FILE_PATH="Enter the path of the encrypted file or folder: "
set /p PASSWORD="Enter the password: "

cd /d "%~dp0"
python file_encryptor.py decrypt "%FILE_PATH%" --password "%PASSWORD%"
if %ERRORLEVEL% EQU 0 (
    echo.
    echo Decryption completed! Your files have been decrypted in place.
)
pause
